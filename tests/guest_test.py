import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Rockin Ralph", 100, "Back in Black")


    def test_guest_has_name(self):
        expected = "Rockin Ralph"
        actual = self.guest.name
        self.assertEqual (expected, actual)

    def test_guest_has_wallet(self):
        expected = 100
        actual = self.guest.wallet
        self.assertEqual (expected, actual)

    def test_guest_has_fave_song(self):
        expected = "Back in Black"
        actual = self.guest.fave_song
        self.assertEqual (expected, actual)

        

