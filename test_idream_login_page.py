from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class BrowserManager:
    """Zarządza przeglądarką."""
    def __init__(self, driver_path):

        self.service = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)

    def close_browser(self):

        self.driver.quit()

class IDreamLoginPage:
    """Reprezentuje stronę logowania idream.pl."""
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.url = "https://idream.pl/logowanie.html"  # Adres strony logowania
        self.email_field = (By.ID, "login_main_login")  # Lokator pola e-mail
        self.password_field = (By.ID, "psw_main_login")  # Lokator pola hasła
        self.login_button = (By.XPATH, "(//button[@name='dispatch[auth.login]'])[2]")  # Lokator przycisku logowania

    def open_page(self):
        self.driver.get(self.url)

    def login(self, email, password):
        # Znajdź pole e-mail i wpisz adres
        email_element = self.driver.find_element(*self.email_field)
        email_element.send_keys(email)

        # Znajdź pole hasła i wpisz hasło
        password_element = self.driver.find_element(*self.password_field)
        password_element.send_keys(password)

        # Kliknij przycisk logowania
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()


if __name__ == "__main__":
    # Ścieżka do WebDrivera
    DRIVER_PATH = "/usr/local/bin/chromedriver"  # Zmień na poprawną ścieżkę
    EMAIL = "mszylejko@eurotel.pl"        # Podaj swój e-mail
    PASSWORD = "rickandmorty"                # Podaj swoje hasło

    # Uruchomienie przeglądarki i logowanie
    try:
        browser = BrowserManager(DRIVER_PATH)
        login_page = IDreamLoginPage(browser.driver)

        # Otwórz stronę i zaloguj się
        login_page.open_page()
        time.sleep(2)
        login_page.login(EMAIL, PASSWORD)

        # Dodaj czas na interakcję lub sprawdzenie wyniku
        time.sleep(5)

    finally:
        browser.close_browser()