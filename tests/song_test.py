import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Back in Black")

    def test_has_title(self):
        expected = "Back in Black"
        actual = self.song.title
        self.assertEqual (expected, actual)

