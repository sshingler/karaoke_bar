import unittest
from src.bar import Bar
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar ("Bar One", 1000)

    def test_bar_has_name(self):
        expected = "Bar One"
        actual = self.bar.name
        self.assertEqual(expected, actual)
        
    def test_bar_has_till(self):
        expected = 1000 
        actual = self.bar.till
        self.assertEqual(expected, actual)



