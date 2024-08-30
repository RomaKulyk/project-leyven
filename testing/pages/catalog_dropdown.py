from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class CatalogDropdown:
    """
    Constructs all the necessary attributes for the MainMenu object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the MainPage class
    catalog_dropdown
        This is a method to find and define Catalog Dropdown Container.
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
        """This is a method to find and define Catalog Dropdown Container"""
        self.catalog_dropdown_container = self.driver.find_element(
            By.XPATH, CATALOG_DROPDOWN)
