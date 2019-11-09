class Credential:
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
            if(user.surname == sur_name and user.password == new_password):
                current_user = user.sur_name
            return current_user

     def __init__(self, account, username, password):
        self.account_name=account
        self.username=username
        self.acc_password=password
