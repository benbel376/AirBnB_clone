#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.state import State


class TestState(unittest.TestCase):
    """test BaseModel"""

    def test_init_con(self):
        """test blank basemodel init"""
        moment = datetime.now()
        instance1 = State()

        self.assertIsInstance(instance1.id, str)
        self.assertTrue(len(instance1.id) > 0)
        self.assertTrue('State.' + instance1.id in storage.all().keys())

        self.assertIsInstance(instance1.created_at, datetime)
        
        self.assertIsInstance(instance1.updated_at, datetime)
        
        instance1.save()
        self.assertIsInstance(instance1.updated_at, datetime)
        del instance1
        
    def test_dict(self):
        """dictionarry"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        instance2 = State(**test_dict)

        self.assertIsInstance(instance2.id, str)
        self.assertTrue(len(instance2.id) > 0)
        self.assertTrue(instance2.id == test_dict['id'])
        
        self.assertIsInstance(instance2.created_at, datetime)
        self.assertTrue(instance2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(instance2.updated_at, datetime)
        self.assertTrue(instance2.updated_at.isoformat('T') == test_dict['updated_at'])
        instance2.save()
        self.assertGreater(instance2.updated_at, instance2.created_at)
        del instance2

    def test_attr(self):
        """attribute testing"""
        instance3 = State()

        self.assertTrue(hasattr(instance3, "name"))
        self.assertIsInstance(instance3.name, str)
