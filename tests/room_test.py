import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")

    def test_room_has_name(self):
        expected = "Rock Room"
        actual = self.room.name
        self.assertEqual(expected, actual)
        