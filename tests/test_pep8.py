#!/usr/bin/python3
"""test pep8"""
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """test pep8 class"""
    def test_review(self):
        """test review.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/review.py'])
        self.assertEqual(chck_res.total_errors, 0)

    def test_place(self):
        """test place.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/place.py'])
        self.assertEqual(chck_res.total_errors, 0)

	
	def test_base_model(self):
        """base.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/base_model.py'])
        self.assertEqual(chck_res.total_errors, 0)

    def test_user(self):
        """test user.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/user.py'])
        self.assertEqual(chck_res.total_errors, 0)

    def test_state(self):
        """test state.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/state.py'])
        self.assertEqual(chck_res.total_errors, 0)
	
	def test_amenity(self):
        """amenity.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/amenity.py'])
        self.assertEqual(chck_res.total_errors, 0)

    def test_city(self):
        """test city.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/city.py'])
        self.assertEqual(chck_res.total_errors, 0)

    
    def test_file_storage(self):
        """file storage.py"""
        the_style = pep8.StyleGuide(quiet=True)
        chck_res = the_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(chck_res.total_errors, 0)
