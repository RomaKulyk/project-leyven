from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
            By.XPATH, FRAME)

    # def buy_products(self) -> None:
    #     """This is a method to define Buy Products button."""
    #     # self.driver.switch_to.frame(FRAME)
    #     wait = WebDriverWait(self.driver, 10)
    #     self.buy_products_button = wait.until(EC.element_to_be_clickable((
    #         By.XPATH, FRAME)))
        
    # def show_all(self) -> None:
    #     """This is a method to define Show All button."""
    #     self.show_all_button = self.driver.find_element(
    #         By.XPATH, SHOW_ALL)
    #     self.show_all_button.click()
    
    def show_all(self) -> None:
        """This is a method to define Buy Products button."""
        wait = WebDriverWait(self.driver, 10)
        # self.show_all_button = wait.until(EC.presence_of_element_located((
        #     By.XPATH, SHOW_ALL)))
        self.show_all_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, SHOW_ALL)))
                
    def help_me(self) -> None:
        """This is a method to define Help Me button."""
        self.help_me_button = self.driver.find_element(
            By.XPATH, HELP_ME)
        self.help_me_button.click()
        
    def hm_form(self) -> None:
        """This is a method to define Help Me Form."""
        self.help_me_form = self.driver.find_element(
            By.XPATH, HELP_ME_FORM)

    def product_card(self, locator) -> None:
        """This is a method to define Product card."""
        self.product_card_n = self.driver.find_element(
            By.XPATH, locator)
        self.product_card_n.click()



