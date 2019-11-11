#!/usr/bin/env python3.6
import pyperclip
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
    print('Hello, Welcome to Password Locker.')

        
    while True:
        print(' ')
        print("-"*20)
        Print('Kindly use the short codes to navigate: \n ca-create account \n li-login \n ex-exit')
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
            print('\n')
            print(f"New Account created for {first_name} {sur_name} using the password {password}")
            print('\n')
        elif short_code == 'li':

			print('To login, enter your account details:')
			user_name = input('Enter your Sur name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(sur_name,password)
			if user_exists == sur_name:
				print(" ")
				print(f'Welcome {sur_name}. Please choose an option to continue.')
				print(' ')    
        
                while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n cp-Copy Account \n \n dt-Delete Credentials ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {sur_name}')
						break
                    elif short_code == 'cc':
						print(' ')
						print('Enter the credential details:')
						account = input('Enter the Account name- ').strip()
						username = input('Enter your preferred user name - ').strip()
						while True:
                            print(' ')
							print("-"*60)
							print('Please make a selection whether you want a password generated for you or input our own password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
                            else:
								print('Could not process your selection,Try again.')
                        save_credential(add_credentials(account,username,password))
                        print(' ')
                    elif short_code == "dc":
                        print(' ')
                        if display_credentials(account):
                            print("List of your credentials")
                            print(' ')
                            for credentials in display_credentials(account):
                                print(f"Account:{credentials.account} Username {credentials.username}  Password{credentials.password}")
                                print(' ')
                        else:
                            print(' ')
                            Print(f"You do not seem to have any saved credentials")
                            print(' ')
                    elif short_code == "cp":
                        print(' ')
                        copy_account = input('Enter account name you want to copy')
                        copy_credentials(copy_account)
                        print(' ')
                    else:
                        print("Wrong selection! Try again")

                    elif short_code == "dt":
                        print(' ') 
                        if remove in credentials_list:  
                            credentials_list.pop(credentials_list.index(remove))
                        print("Credential removed from credential list")
                        else:
						print('Oops! Wrong option entered. Try again.')

			        else: 
				    print(' ')
				    print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
		print("-"*60)
		print(' ')
		print('Oops! Wrong option entered. Try again.')

                


if __name__ == '__main__': 
	main()







