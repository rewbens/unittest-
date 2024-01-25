import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Pyramid song", "Radio Head")
    
    def test_song_has_title(self):
        self.assertEqual("Pyramid song", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Radio Head", self.song.artist)


if __name__== "__main__":
    unittest.main()
    