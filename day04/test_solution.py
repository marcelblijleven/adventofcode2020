from unittest import TestCase
from day04.solution import (
    dob_check, issue_check, expiration_check,
    height_check, hair_color_check, eye_color_check, pid_check
)


class Test(TestCase):
    def test_dob_check(self):
        self.assertTrue(dob_check('1920'))
        self.assertTrue(dob_check('2002'))
        self.assertFalse(dob_check('1919'))
        self.assertFalse(dob_check('2003'))
        self.assertFalse(dob_check('a'))

    def test_issue_check(self):
        self.assertTrue(issue_check('2010'))
        self.assertTrue(issue_check('2020'))
        self.assertFalse(issue_check('2009'))
        self.assertFalse(issue_check('2021'))
        self.assertFalse(issue_check('a'))

    def test_expiration_check(self):
        self.assertTrue(expiration_check('2020'))
        self.assertTrue(expiration_check('2030'))
        self.assertFalse(expiration_check('2019'))
        self.assertFalse(expiration_check('2031'))
        self.assertFalse(expiration_check('a'))

    def test_height_check(self):
        self.assertTrue(height_check('150cm'))
        self.assertTrue(height_check('193cm'))
        self.assertTrue(height_check('59in'))
        self.assertTrue(height_check('76in'))
        self.assertFalse(height_check('149cm'))
        self.assertFalse(height_check('194cm'))
        self.assertFalse(height_check('58in'))
        self.assertFalse(height_check('77in'))
        self.assertFalse(height_check('150db'))

    def test_hair_color_check(self):
        self.assertTrue(hair_color_check('#c0ffee'))
        self.assertTrue(hair_color_check('#000000'))
        self.assertTrue(hair_color_check('#ababab'))
        self.assertFalse(hair_color_check('#fg0000'))
        self.assertFalse(hair_color_check('1234567'))

    def test_eye_color_check(self):
        self.assertTrue(eye_color_check('amb'))
        self.assertTrue(eye_color_check('blu'))
        self.assertTrue(eye_color_check('brn'))
        self.assertTrue(eye_color_check('gry'))
        self.assertTrue(eye_color_check('grn'))
        self.assertTrue(eye_color_check('hzl'))
        self.assertTrue(eye_color_check('oth'))
        self.assertFalse(eye_color_check('abc'))

    def test_pid_check(self):
        self.assertTrue(pid_check('000000001'))
        self.assertTrue(pid_check('123456789'))
        self.assertFalse(pid_check('12345678'))
        self.assertFalse(pid_check('1234567890'))
        self.assertFalse(pid_check('12345678a'))
