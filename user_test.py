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

    def test_save_user(self):
        """
        test case to test a method that saves the new_user
        """
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list),3)

class TestCredentials(unittest.TestCase):
    """
    Test class that tests the functionality of credentials class
    Args:
        unittest.TestCase: helps in creating test cases
    
    """
    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User("Joyce","Nyakinyua","0721317715","joynya123")
        self.new_user.save_user()
        user2 = User("James", "muriuki", "0716259321","jaymo@ms123")
        user2.save_user()

        for user in User.user_list:
            if user.sur_name == user2.sur_name and user.new_password == user2.new_password:
                current_user = user.sur_name
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.new_password,user2.sur_name))

    def setUp(self):
        """
        function to set up a method to be used in running each testcase
        """
        self.new_credentials = credentials("Instagram", "wanjirunya","nyakinyua254")  

    def test_init(self):
        """
        Test to check if initialization of credentiantil instances is done
        """




if __name__ == '__main__':
    unittest.main()


        