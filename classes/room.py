class Room:

    def __init__(self, room_name, room_capacity):
        self.name = room_name
        self.checked_in_guests = []
        self.songs = []
        self.room_capacity = room_capacity

    def check_in(self, guest, rooms):
        if len(self.checked_in_guests) < self.room_capacity:
            guest.is_checked_in = True
            self.checked_in_guests.append(guest)
        else:
            for room in rooms:
                if room != self and len(room.checked_in_guests) < room.room_capacity:
                    return f"Sorry, {self.name} is full. Would you like to visit {room.name} room instead?"
            return "Sorry, all rooms are full."

    def check_out(self, guest):
        guest.is_checked_in = False 
        self.checked_in_guests.remove(guest)

    def add_song(self, song):
        self.room.songs.append(song)





    
        


