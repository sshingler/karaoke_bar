import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")
        self.song_1 = Song ("Back in Black", "ACDC", "Rock") 

    def test_room_has_name(self):
        expected = "Rock Room"
        actual = self.room.name
        self.assertEqual(expected, actual)

    def test_room_has_song_list(self):
        expected = []
        actual = self.room.song_list
        self.assertEqual(expected, actual)

    def test_add_song_to_song_list(self):
        expected = 1
        actual = self.room.song_list
        self.room.add_song_to_song_list(self.song_1)

    # def test_length_of_song_list (self):
    #     expected = 0
    #     actual = self.room.length_of_song_list
    #     self.assertEqual(expected, actual)
