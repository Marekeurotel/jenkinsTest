import unittest
from selenium.webdriver.common.by import By
from test_idream_main_page import IDreamHomePage, IDreamProductPage, BrowserManager
import time

class TestIDreamAddToCart(unittest.TestCase):

    def setUp(self):
        """Przygotowanie do testu: uruchomienie przeglądarki i wejście na stronę."""
        self.driver_path = "/usr/local/bin/chromedriver"  # Zmień na poprawną ścieżkę
        self.browser = BrowserManager(self.driver_path)
        self.home_page = IDreamHomePage(self.browser.driver)
        self.product_page = IDreamProductPage(self.browser.driver)

    def test_add_product_to_cart(self):

        self.home_page.open_page()

        # Dodaj produkt do koszyka
        self.product_page.product_cart()

        time.sleep(1)

        # Sprawdź, czy produkt został dodany (np. sprawdzając obecność koszyka)
        # Sprawdzamy, czy w koszyku jest co najmniej 1 produkt

        cart_element = self.browser.driver.find_element(By.CLASS_NAME, "ty-minicart-count")
        cart_count = cart_element.text
        self.assertGreater(int(cart_count), 0, "Produkt został dodany do koszyka.")
        print(f"Produkty w koszyku: {cart_count}")

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser.close_browser()

