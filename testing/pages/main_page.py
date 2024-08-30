from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver

class MainPage:
    """
    Constructs all the necessary attributes for the MainPage object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the MainPage class
    open_page
        This is a method to open a certain web page
    buy_products
        This is a method to define Buy Products button
    show_all
        This is a method to define Show All button
    help_me
       This is a method to define Help Me button 
    hm_form
        This is a method to define Help Me Form    
    main_logo
        This is a method to define and click Main Logo button
    """
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def open_page(self, url) -> None:
        """This is a method to open a certain web page."""
        self.driver.get(url)
        self.driver.implicitly_wait(3)
    
    def buy_products(self) -> None:
        """This is a method to define Buy Products button."""
        self.buy_products_button = self.driver.find_element(
            By.XPATH, BUY_PRODUCTS)
        # self.buy_products_button.click()

    def show_all(self) -> None:
        """This is a method to define Show All button."""
        self.show_all_button = self.driver.find_element(
            By.XPATH, SHOW_ALL)
        self.show_all_button.click()
        
    def help_me(self) -> None:
        """This is a method to define Help Me button."""
        self.help_me_button = self.driver.find_element(
            By.XPATH, HELP_ME)
        self.help_me_button.click()
        
    def hm_form(self) -> None:
        """This is a method to define Help Me Form."""
        self.help_me_form = self.driver.find_element(
            By.XPATH, HELP_ME_FORM)
        
    def main_logo(self) -> None:
        """This is a method to define and click Main Logo button."""
        self.main_logo_button = self.driver.find_element(
            By.XPATH, MAIN_LOGO)
        self.main_logo_button.click()
