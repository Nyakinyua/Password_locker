import unittest #importing unittest module
from user import User #importing user class

class TestUser(unittest.TestCase):
    """
    class that tests functionality of the user class
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_user = User("Joyce","Nyakinyua","0721317715","joynya123") #new user object
    
    def test_init(self):
        """
        init test case in order to check whether object is initialized
        """
        self.assertEqual(self.new_user.first_name,"Joyce")
        self.assertEqual(self.new_user.sur_name,"Nyakinyua")
        self.assertEqual(self.new_user.mobile_number,"0721317715")
        self.assertEqual(self.new_user.new_password,"joynya123")

    def test_save_newuser(self):
        """
        test case to test a method that saves the new_user
        """
        self.new_user.save_user(self) #saving new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()


        