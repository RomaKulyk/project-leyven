from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
    find_go_to_category
        This is a method to define GO_TO_CATEGORY button
    click_go_to_category
        This is a method to find and click GO_TO_CATEGORY button
    help_me
       This is a method to define Help Me button
    hm_form
        This is a method to define Help Me Form
    sort_item
        This is a method to define sorting functionality
    sort_item_sel
        This is a method to define sorting functionality with Sorting module
    scroll_to_the_footer
        This is a method to scroll page to the Footer be visible
    product_card_price
        This is a method to find and define product price
    product_card
        This is a method to define Product card
    product_cards
        This is a method to find and define Product card item's list
    product_category
        This is a method to define Product category
    product_categories
        This is a method to find and define Product categories item's list
    to_buy
        This is a method to find and defint TO BUY button on Product Cards
    verify_the_page_title
        This is a method to verify the page title
    click_main_product_category
        This is a method to find and click main product category
    find_main_products_category
        This is a method to find main product category
    find_main_products_categories
        This is a method to find main products categories list
    """

    
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = MAIN_PAGE_TITLE

    def open_page(self, url) -> None:
        """This is a method to open a certain web page."""
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def find_go_to_category(self, index) -> None:
        """This is a method to define GO_TO_CATEGORY button."""
        wait = WebDriverWait(self.driver, 10)
        self.go_to_category_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{GO_TO_CATEGORY}[{index}]")))
        
    def click_go_to_category(self, index) -> None:
        """This is a method to find and click GO_TO_CATEGORY button."""
        wait = WebDriverWait(self.driver, 10)
        self.go_to_category_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{GO_TO_CATEGORY}[{index}]")))
        self.go_to_category_button.click()
        
    def help_me(self) -> None:
        """This is a method to define Help Me button."""
        self.help_me_button = self.driver.find_element(
            By.XPATH, HELP_ME)
        self.help_me_button.click()

    def hm_form(self) -> None:
        """This is a method to define Help Me Form."""
        self.help_me_form = self.driver.find_element(
            By.XPATH, HELP_ME_FORM)
        
    def click_product_category(self, index) -> None:
        """This is a method to find and click Product category."""
        wait = WebDriverWait(self.driver, 10)
        self.product_category_n = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{PRODUCT_CATEGORY}[{index}]")))
        self.product_category_n.click()

    def find_product_category(self, index) -> None:
        """This is a method to define Product category."""
        self.product_category_n = self.driver.find_element(
            By.XPATH, f"{PRODUCT_CATEGORY}[{index}]")
        
    def find_product_categories(self) -> None:
        """This is a method to find and define Product categories item's list."""
        # Store all elements of categories in a list
        self.product_categories_list = list(self.driver.find_elements(
            By.XPATH, PRODUCT_CATEGORIES))

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
    
    def scroll_to_the_footer(self) -> None:
        """This is a method to scroll page to the Footer be visible."""
        wait = WebDriverWait(self.driver, 15)
        self.footer = wait.until(EC.visibility_of_element_located((
            By.XPATH, FOOTER)))
        
        action = ActionChains(self.driver)        
        action.scroll_to_element(self.footer)
        action.perform()
        
    def verify_the_page_title(self, title: str) -> None:
        """This is a method to verify the page title."""
        self.title = self.driver.title
        assert self.title == title, f"Expected title: {title}, but got: {self.title}"

    def click_main_product_category(self, index: int) -> None:
        """This is a method to find and click main product category."""    
        wait = WebDriverWait(self.driver, 10)
        self.main_product_category_n = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{MAIN_PRODUCTS_CATEGORIES}[{index}]")))
        self.main_product_category_n.click()

    def find_main_products_category(self, index: int) -> None:
        """This is a method to find main product category."""
        wait = WebDriverWait(self.driver, 10)
        self.main_product_category_n = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"{MAIN_PRODUCTS_CATEGORIES}[{index}]")))
        
    def find_main_products_categories(self) -> None:
        """This is a method to find main products categories list."""
        self.main_products_categories_list = list(self.driver.find_elements(
            By.XPATH, MAIN_PRODUCTS_CATEGORIES))