from selenium.webdriver.common.by import By
from testing.lib.constants import *
from testing.pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(MainPage):
    """
    Constructs all the necessary attributes for the InventoryPage object.
    Attributes:
    driver:obj
                It is an object of webdriver class.
    Methods:
    __init__
        This is a method to initialize instance of the LoginPage class.
    go_to_pdp_link
        This is a method to to to product page
    to_buy
        This is a method to add item to the cart
    """

    def __init__(self, driver):
        """
        This is a method to initialize instance of the InventoryPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        super().__init__(driver)

    def go_to_pdp_link(self, locator: str) -> None:
        """This is a method to define how to move to pdp."""
        self.inventory_item_name = self.driver.find_element(
            By.XPATH, locator)
        self.inventory_item_name.click()

    def to_buy(self, locator) -> None:
        """This method defines 'TO_BUY' button from pdp."""

        wait = WebDriverWait(self.driver, 10)
        self.to_buy_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, locator)))
        self.to_buy_button.click()
