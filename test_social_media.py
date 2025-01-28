import unittest
from test_idream_main_page import *
import time

class TestSocialMediaButtons(unittest.TestCase):

    def setUp(self):
        """Przygotowanie do testu: uruchomienie przeglądarki i wejście na stronę."""
        self.driver_path = "/usr/local/bin/chromedriver"
        self.browser = BrowserManager(self.driver_path)
        self.home_page = IDreamHomePage(self.browser.driver)

    def test_instagram_link(self):

        self.home_page.open_page()
        time.sleep(1)
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        instagram_link = self.home_page.instagram_button()
        instagram_link.click()

        self.browser.driver.switch_to.window(self.browser.driver.window_handles[-1])
        time.sleep(1)
        current_url = self.browser.driver.current_url
        expected_url = "https://www.instagram.com/idream_pl/"
        self.assertEqual(current_url, expected_url, "Odnośnik do Instagrama jest niepoprawny.")
        self.browser.driver.close()
        self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])

    def test_facebook_link(self):

        self.home_page.open_page()
        time.sleep(1)
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        instagram_link = self.home_page.facebook_button()
        instagram_link.click()

        self.browser.driver.switch_to.window(self.browser.driver.window_handles[-1])
        time.sleep(1)
        current_url = self.browser.driver.current_url
        expected_url = "https://www.facebook.com/iDreamPolska/"
        self.assertEqual(current_url, expected_url, "Odnośnik do Facebooka jest niepoprawny.")
        self.browser.driver.close()
        self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])

    def test_tiktok_link(self):

        self.home_page.open_page()
        time.sleep(1)
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        instagram_link = self.home_page.tiktok_button()
        instagram_link.click()

        self.browser.driver.switch_to.window(self.browser.driver.window_handles[-1])
        time.sleep(1)
        current_url = self.browser.driver.current_url
        expected_url = "https://www.tiktok.com/@idream_pl"
        self.assertEqual(current_url, expected_url, "Odnośnik do TikToka jest niepoprawny.")
        self.browser.driver.close()
        self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])

    def test_youtube_link(self):

        self.home_page.open_page()
        time.sleep(1)
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        instagram_link = self.home_page.youtube_button()
        instagram_link.click()

        self.browser.driver.switch_to.window(self.browser.driver.window_handles[-1])
        time.sleep(2)
        current_url = self.browser.driver.current_url
        expected_url = "https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2Fuser%2FiDreamPL%3Fcbrd%3D1&gl=PL&m=0&pc=yt&cm=2&hl=pl&src=1"
        self.assertEqual(current_url, expected_url, "Odnośnik do YouTuba jest niepoprawny.")
        self.browser.driver.close()
        self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser.close_browser()