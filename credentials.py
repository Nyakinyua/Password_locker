import random #to perform random generations
import string # to give various string constants which conain ASCII characters of all cases
import pyperclip

class Credentials:
        """
        class to create account credentials
        """

        credentials_list = []
        user_credentials_list = []

        @classmethod
        def check_user(cls,sur_name,new_password):
            '''
            Method that checks if the name and password entered match entries in the users_list
            '''
            current_user = ''
            for user in User.user_list:
                if (user.sur_name == sur_name and user.new_password == new_password):
                    current_user = user.sur_name
            return current_user
   

   

        def __init__(self, account, username, password):
            self.account_name=account
            self.username=username
            self.acc_password=password

        def save_credentials(self):
            """
            function to save a newly created account instance
            """
            Credentials.credentials_list.append(self)

        @classmethod
        def display_credentials(cls,account):
            	 
            return cls.credentials_list

        def find_by_account(cls,account):
            """
            Method that takes in account name and returns the credentials
            """
       
            for credentials in cls.credentials_list:
                if credentials.account_name == account:
                    return credentials



        # @classmethod
	    # def copy_credential(cls,account):
        #     '''
        #     Class method that copies a credential's info after the credential's aaccount name is entered
        #     '''
        #     find_credential = Credentials.find_by_account(account)
        #     return pyperclip.copy(find_credential.password)

        def delete_credentials(self):

            '''
            A method that  deletes a saved credential from the credentials_list
            '''

            Credentials.credentials_list.remove(self)

 
        def generate_password(stringLength):
            """Generate a random string with the combination of lowercase and uppercase letters 
            """

            letters = string.ascii_letters
            made_password =''.join(random.choice(letters) for i in range(stringLength))
            return made_password

