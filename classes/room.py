class Room:

    def __init__(self, room_name, room_capacity):
        self.name = room_name
        self.checked_in_guests = []
        self.songs = []
        self.room_capacity = room_capacity

    def check_in(self, guest):
        if len(self.checked_in_guests) <= self.room_capacity:
            guest.is_checked_in = True
            self.checked_in_guests.append(guest)

    def check_out(self, guest):
        guest.is_checked_in = False 
        self.checked_in_guests.remove(guest)

    def add_song(self, song, room):
        self.room.songs.append(song)



    
        


