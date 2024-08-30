from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
    search
        This is a method to find, clear and enter query into search field
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

    def search(self, user_input: str) -> None:
        """
        This is a method to find, clear and enter query into search field.
        Parameters
        user_input:str
                   Username to log in with
        """
        self.search_field = self.driver.find_element(
            By.XPATH, SEARCH_FIELD)
        self.search_field.clear()
        self.search_field.send_keys(user_input)
