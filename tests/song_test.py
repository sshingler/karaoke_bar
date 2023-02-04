import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Back in Black", "ACDC", "Rock" )

    def test_song_has_title(self):
        expected = "Back in Black"
        actual = self.song.title
        self.assertEqual (expected, actual)

    def test_song_has_artist(self):
        expected = "ACDC"
        actual = self.song.artist
        self.assertEqual (expected,actual)

    def test_song_has_genre(self):
        expected = "Rock"
        actual = self.song.genre
        self.assertEqual (expected, actual)

    

