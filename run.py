#!/usr/bin/env python3.6
'''
Run Module by Carol Wanjohi

This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module
'''
from user import User
from credential import Credential

def create_user(name, password):
    '''
    Function to create a user account

    Args:
        name : the name the user wants for the account
        password : the password the user want for the account
    '''

    new_user = User(name,password)

    return new_user

def save_users(user):
    '''
    Function to save a user account

    Args:
        user : the user account to be saved
    '''

    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists

    Args:
        name : the user account name
    '''

    return User.user_exist(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account

    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''

    return User.log_in(name, password)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()

def create_credentail(name, password):
    '''
    Function to create a credential 

    Args:
        name : the name of the account 
        password : the password for the account
    '''

    new_credentail = Credential(user_name,user_password)

    return new_credentail

def save_credentials(credential):
    '''
    Function to save a credential

    Args:
        credential : the credential to be saved
    '''

    user.save_user()

def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists

    Args:
        name : the credential name
    '''

    return Credential.credential_exist(name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential()

def create_generated_password(name):
    '''
    Function that generates a password for the user 

    Args:
        name : the name of the account
    '''
    password = Credential.generate_password()

    new_credentail = Credential(name, password)

    return new_credentail

def main():
    '''
    Function running the Password Locker app
    '''

    print('''Welcome to Password Locker \n
Use these short codes to get around''')

    while True:

        print('''   Short codes:
        cu - create a Password Locker account \n
        du - display names of current Password Locker users \n
        lg - log into your Password Locker account \n
        ex - exit the Password Locker account''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'cu':

            '''
            Creating a Password Locker account
            '''

            print("New Password Locker Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            user_password = input()

            # Create and save new user
            save_users( create_user( user_name, user_password) )

            print("\n")
            print(f"{user_name} welcome to Password Locker")
            print("\n")

        elif short_code == 'du':
            '''
            Display the names of the current users 
            '''
            if display_users():
                print("Here are the current users of Password Locker")
                print("\n")

                for user in display_users():
                    print(f"{user.user_name}")
                    print("\n")
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")

        elif short_code == 'ex':
            '''
            Exit Password Locker
            '''

            print("Bye .....")

            break

        else:
            print("Come again. Please use the short codes")

if __name__ == '__main__':
    main()


