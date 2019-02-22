from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
        )

    def tearDown(self):
        self. browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://app:8000')

        assert 'Django' in self.browser.title, "Browser title was " + self.browser.title
