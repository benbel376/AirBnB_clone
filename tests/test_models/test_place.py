#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """test BaseModel"""

    def test_init_con(self):
        """test blank basemodel init"""
        moment = datetime.now()
        PlaceAt1 = Place()

        self.assertIsInstance(PlaceAt1.id, str)
        self.assertTrue(len(PlaceAt1.id) > 0)
        self.assertTrue('Place.' + PlaceAt1.id in storage.all().keys())

        self.assertIsInstance(PlaceAt1.created_at, datetime)
        
        self.assertIsInstance(PlaceAt1.updated_at, datetime)
        
        PlaceAt1.save()
        self.assertIsInstance(PlaceAt1.updated_at, datetime)
        del PlaceAt1
        
    def test_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')
                     , 'id': 'l3142b62-03fa-jaae-37de-830705d8313z', 'created_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')}
        PlaceAt2 = Place(**test_dict)

        self.assertIsInstance(PlaceAt2.id, str)
        self.assertTrue(len(PlaceAt2.id) > 0)
		self.assertTrue(PlaceAt2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(PlaceAt2.updated_at, datetime)
        self.assertTrue(PlaceAt2.id == test_dict['id'])
        
        self.assertIsInstance(PlaceAt2.created_at, datetime)
       
        self.assertTrue(PlaceAt2.updated_at.isoformat('T') == test_dict['updated_at'])
        PlaceAt2.save()
        self.assertGreater(PlaceAt2.updated_at, PlaceAt2.created_at)
        del PlaceAt2

    def test_attribute(self):
        """asdad"""
        PlaceAt = Place()

        self.assertTrue(hasattr(PlaceAt, "city_id"))
        self.assertTrue(hasattr(PlaceAt, "user_id"))
        self.assertTrue(hasattr(PlaceAt, "name"))
        self.assertTrue(hasattr(PlaceAt, "description"))
        self.assertTrue(hasattr(PlaceAt, "number_rooms"))
        self.assertTrue(hasattr(PlaceAt, "number_bathrooms"))
        self.assertTrue(hasattr(PlaceAt, "max_guest"))
        self.assertTrue(hasattr(PlaceAt, "price_by_night"))
        self.assertTrue(hasattr(PlaceAt, "latitude"))
        self.assertTrue(hasattr(PlaceAt, "longitude"))
        self.assertTrue(hasattr(PlaceAt, "amenity_ids"))

        self.assertIsInstance(PlaceAt.city_id, str)
        self.assertIsInstance(PlaceAt.user_id, str)
        self.assertIsInstance(PlaceAt.name, str)
        self.assertIsInstance(PlaceAt.description, str)
        self.assertIsInstance(PlaceAt.number_rooms, int)
        self.assertIsInstance(PlaceAt.number_bathrooms, int)
        self.assertIsInstance(PlaceAt.max_guest, int)
        self.assertIsInstance(PlaceAt.price_by_night, int)
        self.assertIsInstance(PlaceAt.latitude, float)
        self.assertIsInstance(PlaceAt.longitude, float)
        self.assertIsInstance(PlaceAt.amenity_ids, list)

