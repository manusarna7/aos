import unittest
import aos_methods as methods
import aos_locators as locators



class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_validate_homepage(): # test_ in the name is mandatory
        methods.setUp()
        methods.validate_homepage_texts_links()
        methods.tearDown()
