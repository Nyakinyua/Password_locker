import random #to perform random generations
import string # to give various string constants which conain ASCII characters of all cases


class Credentials:
    """
    class to create account credentials
    """

    credentials_list = []
   

    def check_user(cls,sur_name,new_password):
        """
        method that checks if the password and name entered match entries in the user_list
        """
        current_user=""
        for user in User.user_list:
            if user.surname == sur_name and user.password == new_password:
                current_user = user.sur_name
            return current_user

    # def __init__(self, account, username, password):
    #     self.account_name=account
    #     self.username=username
    #     self.acc_password=password

    # def save_credentials(self):
    #     """
    #     function to save a newly created account instance
    #     """
    #     Credentials.credentials_list.append(self)

 
    # def generate_password(stringLength):
    #     """Generate a random string with the combination of lowercase and uppercase letters 
    #     """

    #     letters = string.ascii_letters
    #     return made_password(''.join(random.choice(letters) for i in range(stringLength)))
    # print ("your password  is ", made_password(8))

