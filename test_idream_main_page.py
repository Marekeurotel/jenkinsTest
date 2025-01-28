from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class BrowserManager:
    """Zarządza przeglądarką."""

    def __init__(self, driver_path):
        # Inicjalizacja przeglądarki Chrome
        self.service = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)

    def close_browser(self):
        """Zamyka przeglądarkę."""
        self.driver.quit()


class IDreamHomePage:
    """Reprezentuje stronę główną idream.pl."""

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.url = "https://www.idream.pl/"  # Adres strony głównej

    def open_page(self):
        """Otwiera stronę główną."""
        self.driver.get(self.url)

    def get_title(self):
        """Zwraca tytuł strony."""
        return self.driver.title

    def search_input(self):
        return self.driver.find_element(By.NAME, "q")

    def instagram_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='https://www.instagram.com/idream_pl/']")

    def facebook_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/iDreamPolska/']")

    def tiktok_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='https://www.tiktok.com/@idream_pl']")

    def youtube_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com/user/iDreamPL/']")

    def cart_content_button(self):
        return self.driver.find_element(By.XPATH, "//div[@class=' ut2-top-cart-content ']")

    def my_account_button(self):
        return self.driver.find_element(By.XPATH, "//div[@class=' ut2-top-my-account ']")

    def wishlist_button(self):
        return self.driver.find_element(By.XPATH, "//a[@class='cm-tooltip ty-wishlist__a ']")

    def compared_products_button(self):
        return self.driver.find_element(By.XPATH, "//div[@id='abt__ut2_compared_products']")

    def add_to_wish_button(self):
        return self.driver.find_element(By.CLASS_NAME, "ut2-add-to-wish.cm-submit.cm-tooltip")


class IDreamProductPage:

    def __init__(self, driver):
        self.driver = driver

    def product_cart(self):
        add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "ty-btn__add-to-cart")
        add_to_cart_button.click()

        time.sleep(2)

        cashbox_button = self.driver.find_element(By.CLASS_NAME, "ty-float-left")
        cashbox_button.click()

        time.sleep(1)


if __name__ == "__main__":
    # Ścieżka do WebDrivera
    DRIVER_PATH = "/usr/local/bin/chromedriver"  # Zmień na poprawną ścieżkę

    browser = None

    # Uruchomienie przeglądarki i wejście na stronę główną
    try:
        browser = BrowserManager(DRIVER_PATH)
        home_page = IDreamHomePage(browser.driver)

        # Otwórz stronę główną
        home_page.open_page()
        time.sleep(2)

        # Pobierz tytuł strony i wyświetl go w konsoli
        print(f"Tytuł strony: {home_page.get_title()}")
    finally:
        # Zawsze zamykaj przeglądarkę, nawet w przypadku błędów
        if browser:
            browser.close_browser()
