#! /usr/bin/env python3
import pyperclip
from user import User
from credentials import Credentials

def create_user(fname,sname,pnumber,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = credentials.check_user(sur_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(account,username,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credentials(account,username,password)
	return new_credential

def save_credential(credentials):
	'''
	Function to save a newly created credential
	'''
	Credentials.save_credentials(credential)

def display_credentials(account):
	'''
	Function to display credentials saved by a user
	'''
	return Credentials.display_credentials(account)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential(site_name)

def find_credentials(account):
    """
    function that finds a credential by account and returns the credential
    """
    return Credentials.find_by_account(account)

def del_credentials(credentials):
    """
    function to delete a credential from credentials list
    """
    credentials.delete_ceredentials()

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
        # print('-'*10)
        # print('Use these short codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':

			print(" Please fill the details to create a new Account")
            # print("-"*10)

            print("First name ...")
            f_name = input()

            print("sur name ...")
            s_name = input()

            print("Phone number ...")
            p_number = input()

            print("Password ...")
            p_word = input()
			save_user(create_user(f_name,s_name,p_number,p_word))
			print(" ")
			print(f'New Account Created for: {f_name} {s_name} using password: {p_word}')
            print('\n')
        elif short_code == 'li':
			print("-"*10)
			print(' ')
			print('To login, enter your account details:')
			sur_name = input('Enter your sur name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(sur_name,password)
			if user_exists == sur_name:
				print(" ")
				print(f'Welcome {sur_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy account details \n dt-Delete credentials \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'thanks for signing up with us {sur_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						Account_name = input('Enter the Account\'s name- ').strip()
						user_name = input('Enter your Username - ').strip()
						while True:
							print(' ')
							print("-"*10)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*10)
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
								print('Incorrect/ Wrong option entered. Try again.')
						save_credential(create_credential(Account_name,user_name,password))
						print(' ')
						print(f'Credential Created: Account Name: {Account_name} - User Name: {user_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credentials in display_credentials(user_name):
								print(f'Account name {credentials.Account_name} - User Name: {credentials.user_name} - Password: {credentials.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Incorrect/ Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Incorrect/ Wrong details entered. Try again or Create an Account.')		
		
	else:
		print("-"*60)
		print(' ')
		print('Incorrect/ Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()
