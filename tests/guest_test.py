import unittest
from src.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.instance_of_guest=Guest("John",100)

    def test_guest_has_name(self):
        self.assertEqual("John",self.instance_of_guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100,self.instance_of_guest.wallet)