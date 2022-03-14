from optparse import Option
import unittest
from homework_logic import *

class TestScript(unittest.TestCase):
    
    def setUp(self):
        print("Running set up...")
        self.users = {}

    def test_sign_up_correct_input(self):
        print("Running test sign up correct input...")
        sign_up("Aleksander", "Banan123", self.users)
        self.assertIn("Aleksander", self.users)

    def test_sign_up_wrong_input(self):
        print("Running test sign up wrong input...")
        with self.assertRaises(ValueError):
            sign_up("Aleksander", "Banan", self.users)

    def test_sign_in_correct_input(self):
        print("Running test sign in correct input...")
        self.users = {"Aleksander": "Banan123"}
        self.assertTrue(sign_in("Aleksander", "Banan123", self.users))

    def test_sign_in_wrong_input(self):
        print("Running test sign in wrong input...")
        self.users = {"Aleksander": "Banan123"}
        self.assertFalse(sign_in("test", "truskawka", self.users))

unittest.main()

