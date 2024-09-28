from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CartPage:
    """
    Constructs all the necessary attributes for the CartPage object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the CartPage class
    cart
        This is a method to find and define Cart button
    continue_shopping
        This is a method to define continue shopping button
    checkout
        This is a method to define checkout button
    close_cart
        This is a method to define close cart button
    remove_pdp
        This method defines removing item from cart through pdp
    """

    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainMenu class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def continue_shopping(self) -> None:
        """This is a method to define continue shopping button."""
        self.continue_shopping_button = self.driver.find_element(
            By.XPATH, CONTINUE_SHOPPING)
        
    def checkout(self) -> None:
        """This is a method to define checkout button."""
        wait = WebDriverWait(self.driver, 10)
        self.checkout_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, CHECKOUT)))
        self.checkout_button.click()

    def close_cart(self) -> None:
        """This is a method to define close cart button."""
        self.close_cart_button = self.driver.find_element(
            By.XPATH, CLOSE_CART)
        self.close_cart_button.click()

    def remove_pdp(self, locator) -> None:
        """This method defines removing item from cart through pdp."""
        remove_button = self.driver.find_element(By.XPATH, locator)
        remove_button.click()
