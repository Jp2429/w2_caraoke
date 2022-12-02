import unittest
from src.room import *
from src.song import *
from src.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        song_1=('Song 1','John')
        song_2=('Song 2','Dave')
        song_3=('Song 3','Bob')

        songs=[song_1,song_2,song_3]
        self.instance_of_room=Room('Room 1',songs)

    def test_room_has_name(self):
        self.assertEqual('Room 1',self.instance_of_room.room_name)

    # def test_room_has_song(self):
    #     self.assertEqual('Song 1',self.instance_of_room.songs.name)

    def test_room_can_check_in(self):
        instance_of_guest=Guest('John',100)
        self.instance_of_room.check_in(instance_of_guest)
        self.assertEqual(1,self.instance_of_room.guest_count())
    
    def test_room_can_check_out(self):
        instance_of_guest=Guest('John',100)
        self.instance_of_room.check_in(instance_of_guest)
        self.instance_of_room.check_out(instance_of_guest)
        self.assertEqual(0,self.instance_of_room.guest_count())