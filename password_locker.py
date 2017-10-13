'''
Password Locker Module by Carol Wanjohi

Import random and string modules from Python for generating passwords
'''
import random
import string

'''
Global variables accessible to both classes

Args:
    user_name : name of a user
    user_password : password for a user
    user_list : list of User objects
'''

user_name = ''
user_password = ''
user_list = []

'''
User class : for creating a password locker account
'''

class User:
    '''
    Class that generates instances of user accounts
    '''
    # Accessing the global variables
    global user_name
    global user_password
    # global user_list

    # Empty list of users
    user_list = user_list

    def __init__(self, user_name, user_password):
        '''
        __init__ method to define the properties of a User object

        Args:
            user_name : name of a user
            user_password : password for a user
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
        Method that saves a user to user list
        '''
        User.user_list.append(self)

class Credential:
    '''
    Class that generates instances of a users credentials
    '''
    # Accessing the global variables
    global user_list

    # Empty list of credentials
    credential_list = []

    def __init__(self, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object

        Args:
            credential_name : name of an account
            credential_password : password for the account
        '''

        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        '''
        Method that saves a user's credentials to credential list
        '''
        Credential.credential_list.append(self)





