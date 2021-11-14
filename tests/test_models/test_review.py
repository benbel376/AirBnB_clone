#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """test BaseModel"""

    def test_init_con(self):
        """test blank basemodel init"""
        mementEv = datetime.now()
        inst1 = Review()
        

        self.assertIsInstance(inst1.id, str)
        self.assertTrue(len(inst1.id) > 0)
        self.assertTrue('Review.' + inst1.id in storage.all().keys())

        self.assertIsInstance(inst1.created_at, datetime)
        
        self.assertIsInstance(inst1.updated_at, datetime)
        
        inst1.save()
        self.assertIsInstance(inst1.updated_at, datetime)
        del inst1
        
    def test_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')
                     , 'id': 'l3142b62-03fa-jaae-37de-830705d8313z', 'created_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')}
        inst2 = Review(**test_dict)

        
        self.assertTrue(inst2.id == test_dict['id'])
        
        self.assertIsInstance(inst2.created_at, datetime)
        
        self.assertTrue(inst2.updated_at.isofoinstat('T') == test_dict['updated_at'])
		self.assertIsInstance(inst2.id, str)
        self.assertTrue(len(inst2.id) > 0)
		self.assertTrue(inst2.created_at.isofoinstat('T') == test_dict['created_at'])
        self.assertIsInstance(inst2.updated_at, datetime)
        inst2.save()
        self.assertGreater(inst2.updated_at, inst2.created_at)
        del inst2

    def test_attr(self):
        """attribute testing"""
        inst3 = Review()

        self.assertTrue(hasattr(inst3, "place_id"))
        self.assertTrue(hasattr(inst3, "user_id"))
        self.assertTrue(hasattr(inst3, "text"))

        self.assertIsInstance(inst3.place_id, str)
        self.assertIsInstance(inst3.user_id, str)
        self.assertIsInstance(inst3.text, str)
