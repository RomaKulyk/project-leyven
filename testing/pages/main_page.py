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
    go_to_category_1
        This is a method to define GO_TO_CATEGORY_1 button
    go_to_category_2
        This is a method to define GO_TO_CATEGORY_2 button
    help_me
       This is a method to define Help Me button
    hm_form
        This is a method to define Help Me Form
    sort_item
        This is a method to define sorting functionality
    sort_item_sel
        This is a method to define sorting functionality with Sorting module
    product_card_price
        This is a method to find and define product price
    product_card
        This is a method to define Product card
    product_cards
        This is a method to find and define Product card item's list
    to_buy
        This is a method to find and defint TO BUY button on Product Cards
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

    def go_to_category_1(self) -> None:
        """This is a method to define GO_TO_CATEGORY_1 button."""
        wait = WebDriverWait(self.driver, 10)
        self.go_to_category_1_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, GO_TO_CATEGORY_1)))
        
    def go_to_category_2(self) -> None:
        """This is a method to define GO_TO_CATEGORY_2 button."""
        wait = WebDriverWait(self.driver, 10)
        self.go_to_category_2_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, GO_TO_CATEGORY_2)))
        
    def help_me(self) -> None:
        """This is a method to define Help Me button."""
        self.help_me_button = self.driver.find_element(
            By.XPATH, HELP_ME)
        self.help_me_button.click()

    def hm_form(self) -> None:
        """This is a method to define Help Me Form."""
        self.help_me_form = self.driver.find_element(
            By.XPATH, HELP_ME_FORM)

    def sort_item(self, locator: str) -> None:
        """This is a method to define sorting functionality."""
        self.dropdown_list = self.driver.find_element(By.XPATH, SORT)
        self.dropdown_list.click()
        self.sort_menu_item = self.driver.find_element(By.XPATH, locator)
        self.sort_menu_item.click()

    def sort_item_sel(self) -> None:
        """This is a method to define sorting functionality with Select module."""
        self.dropdown_list_sel = self.driver.find_element(By.XPATH, SORT)
        assert self.dropdown_list_sel.is_displayed()
        self.dropdown_list_sel.click()

    def product_card_price(self) -> int:
        """This is a method to find and define product price."""
        self.product_card_price_value = self.driver.find_element(
            By.XPATH, PR_CARD_PRICE)
        text = self.product_card_price_value.text
        return int(text[0:-2])

    def product_card(self, index) -> None:
        """This is a method to define Product card."""
        wait = WebDriverWait(self.driver, 10)
        self.product_card_n = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{PR_CARD}[{index}]")))
        self.product_card_n.click()

    def product_cards(self) -> None:
        """This is a method to find and define Product card item's list."""
        # Store all elements of dropdown in a list
        self.product_cards_n = list(self.driver.find_elements(
            By.XPATH, PRODUCT_CARDS))
