import unittest
from src.bar import Bar
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar ("Bar One", 1000)
        self.room_1 = Room ("Rock Room")
        self.room_2 = Room ("Dance Room") 
        self.song_1 = Song ("Back in Black", "ACDC", "Rock")
        self.song_2 = Song ("Dance Song", "MR DJ", "Dance")

    def test_bar_has_name(self):
        expected = "Bar One"
        actual = self.bar.name
        self.assertEqual(expected, actual)
        
    def test_bar_has_till(self):
        expected = 1000 
        actual = self.bar.till
        self.assertEqual(expected, actual)

    def test_bar_has_total_room_list(self):
        expected = []
        actual = self.bar.total_room_list
        self.assertEqual(expected, actual)

    def test_add_rooms_to_total_room_list(self): 
        self.bar.add_room_to_total_room_list(self.room_1)
        self.bar.add_room_to_total_room_list(self.room_2)
        expected = 2
        actual = self.bar.length_of_total_room_list()
        self.assertEqual (expected, actual)

    def test_add_song_to_total_song_list(self):
        self.bar.add_song_to_total_song_list(self.song_1)
        self.bar.add_song_to_total_song_list(self.song_2)
        expected = 2
        actual = self.bar.length_of_total_song_list()
        self.assertEqual (expected, actual)





