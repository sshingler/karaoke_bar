import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Rockin Ralph")


    def test_has_name(self):
        expected = "Rockin Ralph"
        actual = self.guest.name
        self.assertEqual (expected, actual)

