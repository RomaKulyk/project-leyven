from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
import time


class CatalogDropdown:
    """
    Constructs all the necessary attributes for the MainMenu object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the CatalogDropdown class
    catalog_dropdown
        This is a method to find and define Catalog Dropdown Container
    catalog_dropdown_items
        This is a method to find and define Catalog Dropdown Item
    """
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainMenu class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
    
    def catalog_dropdown(self):
        """This is a method to find and define Catalog Dropdown Container."""
        self.catalog_dropdown_container = self.driver.find_element(
            By.XPATH, CATALOG_DROPDOWN)
        
    def catalog_dropdown_items(self, locator):
        """This is a method to find and define Catalog Dropdown Item."""
        self.catalog_dropdown_item_link = self.driver.find_element(
            By.XPATH, locator)
        self.catalog_dropdown_item_link.click()
    
    def catalog_dropdown_ul(self):
        """This is a method to find and define Catalog Dropdown Item."""
        self.catalog_dropdown_ul_link = self.driver.find_element(
            By.XPATH, DROPDOWN_LIST)
        # Store all elements of dropdown in a list        
        self.catalog_dropdown_elements = list(self.driver.find_elements(
                By.XPATH, DROPDOWN_LIST_ITEMS))
        # Iterate the list using a for loop and click each options
        for e in self.catalog_dropdown_elements:
            e.click()
            time.sleep(0.5)


