class User:
    """
    class that generates new instance of user
    """
    user_list = []  #list to store contacts
    first_name = ''
    sur_name = ''
    mobile_number = ''
    new_password = ''


    
    def __init__(self,first_name,sur_name,mobile_number,new_password):
        """
        __init__method to help us define the properties of class User
        """
        self.first_name= first_name
        self.sur_name=sur_name
        self.mobile_number=mobile_number
        self.new_password=new_password

    def get_firstname(self):
        return self.first_name

    def get_sur_name(self):
        return self.sur_name

    def get_mobile_number(self):
        return self.mobile_number

    def get_new_password(self):
        return self.new_password

    def save_user(self):

        """
        function to save a new instance of user
        """
        User.user_list.append(self)


