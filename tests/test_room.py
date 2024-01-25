import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        """instances of..."""
        self.song = Song ("Pyramid song", "Radio Head"),
        self.song1 = Song ("Back to Black", "Amy Winehouse"),
        self.song2 = Song ("The knife", "Heartbeats"),
        self.room = Room ("Jazzmataz room")
        self.guest = Guest("Elfred", 50, self.song1)

    def test_room_has_name(self):
        self.assertEqual("Jazzymataz room", self.room.name)

    def test_guest_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, len(self.room.checked_in_guests))
        self.assertEqual(True, self.guest.is_checked_in)
        self.assertEqual(90, self.guest.cash)

    def test_guest_check_out(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, len(self.room.checked_in_guests))
        self.assertEqual(False, self.guest.is_checked_in)

if __name__ == "__main__":
    unittest.main()

          

    