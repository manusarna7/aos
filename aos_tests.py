import unittest
import aos_methods as methods
import aos_locators as locators



class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_account(): # test_ in the name is mandatory
        methods.setUp()
        methods.create_new_account()
        methods.validate_new_account()
        methods.log_out()
        methods.log_in()
        methods.log_out()
        methods.tearDown()
