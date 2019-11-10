import unittest #importing unittest module
from user import User #importing user class
from credentials import Credentials #importing credentials class

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
        self.assertEqual(len(User.user_list),1)

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
        self.new_credentials = Credentials("Instagram", "wanjirunya","nyakinyua254")  

    def test_init(self):
        """
        Test to check if initialization of credentiantil instances is done
        """
        self.assertEqual(self.new_credentials.account_name,'Instagram')
        self.assertEqual(self.new_credentials.username,'wanjirunya')
        self.assertEqual(self.new_credentials.acc_password,'nyakinyua254')

    def test_save_credentials(self):
        """
        Test to check if new credential created is appended to credentials list
        """
        self.new_credentials.save_credentials()
        cred2 = Credentials("Snapchat","Johndoe","snp100")
        cred2.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
            """
            Function to clear the credentials list after a test
            """
            Credentials.credentials_list=[]
            User.user_list=[]

    def test_display_credentials(self):
        self.new_credentials.save_credentials()
        cred2 = Credentials("Snapchat","Johndoe","snp100")
        cred2.save_credentials()
        gmail = Credentials('Gmail','maryjoe','pswd200')
        gmail.save_credentials()
        self.assertEqual(len(Credentials.display_credentials(cred2.username)),3)


    def test_find_credential_by_account(self):
        '''
        Test to check if the find_credential_by_account method returns the correct credential
        '''
        self.new_credentials.save_credentials()
        cred2 = Credentials("Snapchat","Johndoe","snp100")
        cred2.save_credentials()
        credential_exists = Credentials.find_by_account('Snapchat')
        self.assertEqual(credential_exists,cred2)
    # def test_copy_credential(self):
    #     '''
    #     Test to check if the copy a credential method copies the correct credential
    #     '''
    #     self.new_credential.save_credentials()
    #     twitter = Credential('Jane','Twitter','maryjoe','pswd100')
    #     twitter.save_credentials()
    #     find_credential = None
    #     for credential in Credential.user_credentials_list:
    #             find_credential =Credential.find_by_site_name(credential.site_name)
    #             return pyperclip.copy(find_credential.password)
    #     Credential.copy_credential(self.new_credential.site_name)
    #     self.assertEqual('pswd100',pyperclip.paste())
    #     print(pyperclip.paste())


     
    # def test_delete_credential(self):
    
    #     self.new_credential.save_credential()
    #     test_credential = Credential("Test","user")
    #     test_credential.save_credential()
        
    #     self.new_credential.delete_credential()
    #     self.assertEqual(len(Credential.credential_list),1)

            




if __name__ == '__main__':
    unittest.main()


        