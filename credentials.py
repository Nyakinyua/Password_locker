import random #to perform random generations
import string # to give various string constants which conain ASCII characters of all cases
import pyperclip

class Credentials:
        """
        class to create account credentials
        """

        credentials_list = []
        user_credentials_list = []

        
   

   

        def __init__(self, account, username, password):
            self.account=account
            self.username=username
            self.password=password

        def save_credentials(self):
            """
            function to save a newly created account instance
            """
            Credentials.credentials_list.append(self)

        def generate_password():
            """
            Generate a random string with the combination of lowercase and uppercase letters 
            """
            letters = string.ascii_letters
            get_pass= ''.join(random.choice(letters) for i in range(8))
            return get_pass

        @classmethod
        def display_credentials(cls):
            	 
            return cls.credentials_list
        
        @classmethod
        def find_by_account(cls, account):
            """
            Method that takes in account name and returns the credentials
            """
       
            for credential in cls.credentials_list:
                if credential.account == account:
                    return credential




        
        def delete_credentials(self):
    
            '''
            A method that  deletes a saved credential from the credentials_list
            '''

            Credentials.credentials_list.remove(self)

 
       
