from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from testing.lib.constants import MAIN_LOGO,\
                                  CATALOG,\
                                  SEARCH_FIELD_OUT,\
                                  SEARCH_FIELD_INN,\
                                  SOCIAL_MEDIA_BUTTONS_LIST_ITEMS,\
                                  PHONE,\
                                  CROSS_BUTTON,\
                                  FACEBOOK,\
                                  INSTAGRAM,\
                                  TIKTOK,\
                                  LOG_IN,\
                                  LANGUAGE_BUTTON,\
                                  CART,\
                                  SEARCH_FOUND_ITEMS,\
                                  SEARCH_FOUND_ITEM


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
    search_list
        This is a method to define list of founded items by search
    search_item
        This is a method to define every founded items by search
    phone
        This is a method to find and define Phone button of Main Menu
    cross
        This is a method to define Cross Button of Search Field
    find_social_media_buttons
        This is a method to find and define Social Media buttons list
    click_social_media_button
        This is a method to find and click Social Media button
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
        wait = WebDriverWait(self.driver, 10)
        self.main_logo_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, MAIN_LOGO)))
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

    def search_list(self):
        """
        This is a method to define list of founded items by search.
        """
        self.search_found_list = list(self.driver.find_elements(
            By.XPATH, SEARCH_FOUND_ITEMS))
        
    def search_item(self, index):
        """
        This is a method to define every founded items by search.
        """
        self.search_found_item = self.driver.find_element(
            By.XPATH, f"{SEARCH_FOUND_ITEM}[{index}]")
        text = self.search_found_item.text
        return text

    def cross(self) -> None:
        """This is a method to define Cross Button of Search Field."""
        wait = WebDriverWait(self.driver, 10)
        self.cross_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, CROSS_BUTTON)))
        
    def phone(self) -> None:
        # action = ActionChains(self.driver)
        """This is a method to find and define Phone button of Main Menu."""
        self.phone_button = self.driver.find_element(
            By.XPATH, PHONE)
        # action.move_to_element(self.phone_button)
        # action.perform()

    def click_social_media_button(self, index: int) -> None:
        """This is a method to find and click Social Media button."""
        self.social_media_button_n = self.driver.find_element(
            By.XPATH, f"{SOCIAL_MEDIA_BUTTONS_LIST_ITEMS}[{index}]")
        self.social_media_button_n.click()

    def find_social_media_buttons(self) -> None:
        """This is a method to find and define Social Media buttons list."""
        self.social_media_buttons_list =  list(self.driver.find_elements(
            By.XPATH, SOCIAL_MEDIA_BUTTONS_LIST_ITEMS))
    
    def language_switcher(self) -> None:
        """This is a method to find and define Language button."""
        self.language_button = self.driver.find_element(
            By.XPATH, LANGUAGE_BUTTON)
        # self.language_button.click()

    def log_in(self) -> None:
        "This is a method to find and define Log In button."
        self.log_in_button = self.driver.find_element(
            By.XPATH, LOG_IN)

    def cart(self) -> None:
        """This is a method to find and define Cart button."""
        self.cart_button = self.driver.find_element(
            By.XPATH, CART)
        self.cart_button.click()
