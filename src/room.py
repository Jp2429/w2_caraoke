class Room:
    def __init__(self,room_name,songs):
        self.room_name=room_name
        self.songs=songs
        self.num_guests=[]

    def check_in(self,guest):
        self.num_guests.append(guest)

    def check_out(self,guest):
        self.num_guests.remove(guest)

    def guest_count(self):
        return len(self.num_guests)

    