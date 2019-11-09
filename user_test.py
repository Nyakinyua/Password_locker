import unittest #importing unittest module
from user import User #importing user class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_user = User("Joyce","Nyakinyua","0721317715","joynya123")

        