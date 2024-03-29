import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        """instances of..."""
        self.song0 = Song ("Pyramid song", "Radio Head"),
        self.song1 = Song ("Back to Black", "Amy Winehouse"),
        self.song2 = Song ("The knife", "Heartbeats"),
        self.room1 = Room ("Jazzmataz room", 3)
        self.room2 = Room ("Alt rock", 10)
        self.room3 = Room ("Electropop", 20)
        self.rooms = [self.room1, self.room2, self.room3]
        self.guest0 = Guest("Elfred", 50, self.song0)
        self.guest1 = Guest("Tom", 25, self.song1)
        self.guest2 = Guest("Adam", 5, self.song2)
        self.guests = [self.guest0, self.guest1, self.guest2]

        

    def test_room_has_name(self):
        self.assertEqual("Jazzmataz room", self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room1.room_capacity)

    def test_guest_check_in(self):
        self.room1.check_in(self.guest0, self.rooms)
        self.assertEqual(1, len(self.room1.checked_in_guests))
        self.assertEqual(True, self.guest0.is_checked_in)
        self.assertEqual(50, self.guest0.cash)

    def test_guest_check_out(self):
        self.room1.check_in(self.guest2, self.rooms)
        self.room1.check_out(self.guest2)
        self.assertEqual(0, len(self.room1.checked_in_guests))
        self.assertEqual(False, self.guest0.is_checked_in)

    def test_check_in_full_room(self):
        #filling up room1
        for _ in range(self.room1.room_capacity):
            self.room1.check_in(Guest("Guest", 50, self.song1), self.rooms)
        message = self.room1.check_in(self.guest0, self.rooms)
        self.assertEqual(message, f"Sorry, {self.room1.name} is full. Would you like to visit {self.room2.name} room instead?")

if __name__ == "__main__":
    unittest.main()

          

    