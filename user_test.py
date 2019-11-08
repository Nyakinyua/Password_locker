class User:
    """
    class that generate new instance of user
    """
    def __init__(self,first_name,sur_name,mobile_number,new_password):
        """
        __init__method to help us define the properties of class User
        """
        self.first_name= first_name
        self.sur_name=sur_name
        self.mobile_number=mobile_number
        self.new_password=new_password
