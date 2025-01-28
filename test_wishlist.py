import unittest
from test_idream_main_page import *
from selenium.webdriver import ActionChains
import time

class TestWishlist(unittest.TestCase):

    def setUp(self):
        """Przygotowanie do testu: uruchomienie przeglądarki i wejście na stronę."""
        self.driver_path = "/usr/local/bin/chromedriver"
        self.browser = BrowserManager(self.driver_path)
        self.home_page = IDreamHomePage(self.browser.driver)

    def test_wishlist_button(self):

        self.home_page.open_page()
        time.sleep(1)
        hover_element = self.browser.driver.find_element(By.XPATH, "(//div[contains(@class,'ut2-gl__body')])[1]")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(2)

        add_product_to_wishlist = self.home_page.add_to_wish_button()
        add_product_to_wishlist.click()
        time.sleep(2)

        go_to_wishlist = self.browser.driver.find_element(By.CLASS_NAME, "ty-float-right")
        go_to_wishlist.click()
        time.sleep(1)

        wishlist_element = self.browser.driver.find_element(By.CLASS_NAME, "ut2-top-wishlist-count")
        wishlist_count = wishlist_element.text
        self.assertGreater(int(wishlist_count), 0, "Produkt nie został dodany do listy życzeń.")
        print(f"Produkty na liście: {wishlist_count}")

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser.close_browser()