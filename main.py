#!/usr/bin/env python3.6
from user import user
from credentials import Credentials


    def create_user(fname,sname,number,password):
        """
        function to create new user
        """
        new_user=User(fname,sname,number,password)
        return new_user

    def save_user(user):
        """
        function to save a new user account
        """
        User.save_user(user)

    def verify_user(sur_name,password):
        """
        function that verifies existence of user
        """
        check_the_user = Credentials.check_user(sur_name,new_password)
        return check_the_user

    def generate_password():
        """
        function to automatically generate passwords
        """
        generate_password = Credentials.generate_password()
        return generate_password

    def  add_credentials(account, username, password):
        """
        Function that creates a new credential
        """
        new_credential = Credentials(account,username,password)
        return new_credential

    def save_credential(credentials):
        """
        function to save the newly created credentials
        """
        Credentials.save_credential(credential)

    def display_credentials(account):

        """ 
        function to display saved credentials
        """
        return Credentials.display_credentials(account)

    def copy_credentials(account):
        """
        function to copy credential details to the clipboard
        """
        return Credentials.copy_detential(account)

    def del_credentials(credentials):
        """
        function to delete a credential from credentials list
        """
        credentials.delete_ceredentials()

    def find_credentials(account):
        """
        function that finds a credential by account and returns the credential
        """
        return Credentials.find_by_account(account)

def main():
    print(' ')
    print('Hello, Welcome to Password Locker.What is your name')
        name = input()
        print('.\n')
    while True:
        print(' ')
        print("-"*20)
        Print('{name}, Kindly use the short codes to navigate: \n ca-create account \n li-login \n ex-exit')
        short_code = input().lower().strip()
        if short_code == 'ex':
            break
        elif short_code == "ca":
            print("Create Account")
            print("-"*20)

            print("First Name ...")
            f_name=input()

            print("Sur Name ...")
            s_name=input()

            print("Phone Number ...")
            p_number = input()

            print("Password ...")
            p_word = input()
            save_user(create_user(first_name,sur_name,password))
            print(' ')
            print(f"New Account created for {sur_name}")










