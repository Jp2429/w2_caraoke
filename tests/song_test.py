import unittest
from src.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.instance_of_song=Song('Country Roads','John Denver')

    def test_song_has_name(self):
        self.assertEqual('Country Roads',self.instance_of_song.name)

    def test_song_has_artist(self):
        self.assertEqual('John Denver',self.instance_of_song.artist)
        