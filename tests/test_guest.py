import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Back to black", "Amy Winehouse")
        self.guest = Guest("Peter Parker", 500, self.song)

    def test_guest_has_name(self):
        self.assertEqual("Peter Parker", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(500, self.guest.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Amy Winehouse", self.guest.favourite_song.artist)

if __name__ == "__main__":
    unittest.main()
