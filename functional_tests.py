__author__ = 'vcholak'

from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # Selenium will now wait up to three seconds before it tries to do anything

    def tearDown(self):
        """
        It will run even if there’s an error during the test itself.
        The only exception is if you have an exception inside setUp, then tearDown doesn’t run.
        """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Products App', self.browser.title)


        # She is invited to enter a to-do item straight away
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')