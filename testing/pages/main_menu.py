from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from testing.lib.constants import MAIN_LOGO,\
                                  CATALOG,\
                                  SEARCH_FIELD_OUT,\
                                  SEARCH_FIELD_INN,\
                                  PHONE,\
                                  CROSS_BUTTON,\
                                  FACEBOOK,\
                                  INSTAGRAM,\
                                  TIKTOK,\
                                  LOG_IN,\
                                  CART


class MainMenu:
    """
    Constructs all the necessary attributes for the MainMenu object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the MainPage class
    main_logo
        This is a method to define and click Main Logo button
    catalog
        This is a method to find catalog button
    search_out
        This is a method to invoke search field
    search_inn
        This is a method to clear and enter query into search field
    phone
        This is a method to find and define Phone button of Main Menu
    cross
        This is a method to define Cross Button of Search Field
    facebook
        This is a method to find and define Facebook button
    instagram
        This is a method to find and define Instagram button
    tiktok
        This is a method to find and define Tiktok button
    log_in
        This is a method to find and define Log In button
    cart
        This is a method to find and define Cart button
    """

    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainMenu class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def main_logo(self) -> None:
        """This is a method to define and click Main Logo button."""
        self.main_logo_button = self.driver.find_element(
            By.XPATH, MAIN_LOGO)
        self.main_logo_button.click()

    def catalog(self) -> None:
        action = ActionChains(self.driver)
        """This is a method to find catalog button."""
        self.catalog_button = self.driver.find_element(
            By.XPATH, CATALOG)
        action.move_to_element(self.catalog_button)
        action.perform()

    def search_out(self) -> None:
        """
        This is a method to invoke search field
        """
        self.search_field_out = self.driver.find_element(
            By.XPATH, SEARCH_FIELD_OUT)
        self.search_field_out.click()
        
    def search_inn(self, user_input: str) -> None:
        """
        This is a method to clear and enter query into search field.
        Parameters
        user_input:str
                   Product to find
        """
        self.search_field_inn = self.driver.find_element(
            By.XPATH, SEARCH_FIELD_INN)
        self.search_field_inn.clear()
        self.search_field_inn.send_keys(user_input)
        
    def phone(self) -> None:
        # action = ActionChains(self.driver)
        """This is a method to find and define Phone button of Main Menu."""
        self.phone_button = self.driver.find_element(
            By.XPATH, PHONE)
        # action.move_to_element(self.phone_button)
        # action.perform()

    def cross(self) -> None:
        """This is a method to define Cross Button of Search Field."""
        self.cross_button = self.driver.find_element(
            By.XPATH, CROSS_BUTTON)

    def facebook(self) -> None:
        """This is a method to find and define Facebook button."""
        self.facebook_button = self.driver.find_element(
            By.XPATH, FACEBOOK)
        self.facebook_button.click()

    def instagram(self) -> None:
        """This is a method to find and define Instagram button."""
        self.instagram_button = self.driver.find_element(
            By.XPATH, INSTAGRAM)
        self.instagram_button.click()

    def tiktok(self) -> None:
        """This is a method to find and define Tiktok button."""
        self.tiktok_button = self.driver.find_element(
            By.XPATH, TIKTOK)
        self.tiktok_button.click()

    def log_in(self) -> None:
        "This is a method to find and define Log In button."
        self.log_in_button = self.driver.find_element(
            By.XPATH, LOG_IN)

    def cart(self) -> None:
        """This is a method to find and define Cart button."""
        self.cart_button = self.driver.find_element(
            By.XPATH, CART)
        self.cart_button.click()
