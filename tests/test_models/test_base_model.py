#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel"""

    def test_init_con(self):
        """test blank basemodel init"""
        moment = datetime.now()
        instBaseM = BaseModel()

        self.assertIsInstance(instBaseM.id, str)
        self.assertTrue('BaseModel.' + instBaseM.id in storage.all().keys())

        self.assertIsInstance(instBaseM.created_at, datetime)
        self.assertIsInstance(instBaseM.updated_at, datetime)
        
        instBaseM.save()
        self.assertIsInstance(instBaseM.updated_at, datetime)
        del instBaseM
        
    def test_dict(self):
        """testing dictionary"""
        test_dict = {'updated_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')
                     , 'id': 'l3142b62-03fa-jaae-37de-830705d8313z', 'created_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')}
        instBaseM2 = BaseModel(**test_dict)

        self.assertIsInstance(instBaseM2.id, str)
        self.assertTrue(len(instBaseM2.id) > 0)
		self.assertTrue(instBaseM2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(instBaseM2.updated_at, datetime)
        self.assertTrue(instBaseM2.updated_at.isoformat('T') == test_dict['updated_at'])
        self.assertTrue(instBaseM2.id == test_dict['id'])
        
        self.assertIsInstance(instBaseM2.created_at, datetime)
       
        instBaseM2.save()
        self.assertGreater(instBaseM2.updated_at, instBaseM2.created_at)
        del instBaseM2
