'''
User Test by Carol Wanjohi

import uniittest to create uniittests for User Module
import User Module to be tested
'''
import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create user object
        self.new_user = User("John","doe")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        User.user_list = []

    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "John" )
        self.assertEqual( self.new_user.user_password, "doe" )

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

        # Saving the new user
        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):
        '''
        Test case to test if you can save multiple objects to user list
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Jane","doey")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)

    # def test_log_in(self):
    #     '''
    #     Test case to test if a user can log into their credentials
    #     '''
    #     # Save the new user
    #     self.new_user.save_user()

    #     found_credential = self.new_user.log_in("John", "doe")

    #     self.assertEqual( found_credential,  )

if __name__ == '__main__':
    unittest.main(verbosity=2)
