import unittest
from test_idream_main_page import *
from selenium.webdriver.common.keys import Keys
import time


class TestSearchBar(unittest.TestCase):

    def setUp(self):
        """Przygotowanie do testu: uruchomienie przeglądarki i wejście na stronę."""
        self.driver_path = "/usr/local/bin/chromedriver"
        self.browser = BrowserManager(self.driver_path)
        self.home_page = IDreamHomePage(self.browser.driver)

    def test_search_bar(self):

        self.home_page.open_page()
        time.sleep(1)
        search_box = self.home_page.search_input()
        search_term = "słuchawki bezprzewodowe"
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        results = self.browser.driver.find_elements(By.CSS_SELECTOR, ".product-title")
        if results:
            for result in results:
                print(f"Wynik wyszukiwania: {result.text}")
                self.assertIn(search_term.lower(), result.text.lower(), "Słowo nie znalezione w wynikach!")
        else:
            self.fail("Brak wyników wyszukiwania.")

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser.close_browser()