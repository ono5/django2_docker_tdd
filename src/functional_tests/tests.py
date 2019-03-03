import socket
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    # https://stackoverflow.com/questions/44240139/run-liveservertestcase-from-docker-selenium-with-django-1-11
    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(NewVisitorTest, cls).setUpClass()

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                assert row_text in [row.text for row in rows]
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.browser.get_screenshot_as_file('test.png')

        header_text = self.browser.find_element_by_tag_name('h1').text
        assert 'To-Do' in header_text

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.browser.get_screenshot_as_file('test.png')

        table = self.browser.find_element_by_id('id_list_table')
        self.browser.get_screenshot_as_file('test2.png')

        rows = table.find_elements_by_tag_name('tr')

        assert any(row.text == '1: Buy peacock feathers' for row in rows), \
            f"New to-do item did not appear in table. Contents were:\n{table.text}"

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Another Person access into Site
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        assert 'Buy peacock feathers' not in page_text
        assert 'make a fly' not in page_text

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        assert francis_list_url not in edith_list_url

        page_text = self.browser.find_element_by_tag_name('body').text
        assert 'Buy peacock feathers' not in page_text
        assert 'Buy milk' in page_text

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
