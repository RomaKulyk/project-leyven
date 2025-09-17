from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from testing.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import inspect


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
    find_the_h1_header
        This is a method to find and define the H1 header on the page.
    print_my_current_url
        This is a method to print the current URL of the page.
    check_if_page_is_loaded
        This is a method to check if the page is loaded.
    scroll_to_bottom
        This method scrolls to the bottom of the page, taking screenshots
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

    def find_the_h1_header(self) -> None:
        """This is a method to find and define the H1 header on the page."""
        self.h1_header = self.driver.find_element(By.TAG_NAME, "h1")
        self.style = self.h1_header.get_attribute("class")

    def print_my_current_url(self) -> None:
        """This is a method to print the current URL of the page."""
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")

    def check_if_page_is_loaded(self) -> None:
        """This is a method to check if the page is loaded."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def scroll_to_bottom(self) -> None:
        """ This method scrolls to the bottom of the page, taking screenshots 
        at each step.
        """
        # Get the current vertical scroll position
        last_height = self.driver.execute_script("return window.pageYOffset;")
        i = 0
        while True:
            # Get the filename of the caller file (the file from which the 
            # method is called)
            caller_frame = inspect.stack()[1]
            caller_filename = os.path.basename(
                caller_frame.filename).split('.')[0]
            # Save a screenshot of the current page view
            self.driver.save_screenshot(
                f"pages_screenshots/{caller_filename[5:]}_{i}.png")
            # Scroll down by one viewport height
            self.driver.execute_script(
                "window.scrollBy(0, window.innerHeight);")
            # Wait for the page to load new content (if any)
            time.sleep(1)
            # Get the new vertical scroll position
            new_height = self.driver.execute_script(
                "return window.pageYOffset;")
            # If the scroll position hasn't changed, we've reached the bottom
            if new_height == last_height:
                break
            last_height = new_height
            i += 1