__author__ = 'vcholak'

# LiveServerTestCase will automatically create a test database,
# and start up a development server for the functional tests to run against.
# StaticLiveServerTestCase additionally can find static files as well.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # Selenium will now wait up to three seconds before it tries to do anything

    def tearDown(self):
        """
        It will run even if there’s an error during the test itself.
        The only exception is if you have an exception inside setUp, then tearDown doesn’t run.
        """
        self.browser.quit()

    def test_home_view(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Products Store', self.browser.title)