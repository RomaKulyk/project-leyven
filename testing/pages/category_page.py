from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from testing.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class CategoryPage(MainPage):
    """
    Constructs all the necessary attributes for the CategoryPage object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the CategoryPage class
    filters_menu
        This is a method to find and define Filters Menu
    filters_list
        This is a method to find and define filters list
    filter
        This is a method to find and define filter itself
    scroll_to_show_more
        This is a method to scroll page until the  SHOW MORE button will
    be visible.    
    find_show_more
        This is a method to define SHOW_MORE_BUTTON.
    click_show_more
        This is a method to find and click SHOW_MORE_BUTTON.
    """

    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the CategoryPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def filters_menu(self) -> None:
        """This is a method to find and define Filters Menu."""
        self.filters_menu_bar = self.driver.find_element(
            By.XPATH, FILTER_MENU_BAR)
  
    def filters_list(self) -> None:
        """This is a method to find and define filters list."""
        self.filters_list_item = list(self.driver.find_elements(
            By.XPATH, FILTERS_LIST)) 
   
    def filter(self, index) -> None:
        """This is a method to find and define filter itself."""
        self.filter_n = self.driver.find_element(
            By.XPATH, f"{FILTER_ITEM}[{index}]")
        
    def scroll_to_show_more(self) -> None:
        """This is a method to scroll page until the  SHOW MORE button will
        be visible."""
        wait = WebDriverWait(self.driver, 10)
        self.show_more_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, SHOW_MORE_BUTTON )))
        
        action = ActionChains(self.driver)        
        action.scroll_to_element(self.show_more_button)
        action.perform()

    def find_show_more(self) -> None:
            """This is a method to define SHOW_MORE_BUTTON."""
            wait = WebDriverWait(self.driver, 10)
            self.show_more_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, SHOW_MORE_BUTTON)))
            
    def click_show_more(self) -> None:
        """This is a method to find and click SHOW_MORE_BUTTON."""
        wait = WebDriverWait(self.driver, 10)
        self.show_more_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, SHOW_MORE_BUTTON)))
        self.show_more_button.click()