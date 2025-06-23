from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Footer:
    """
    Constructs all the necessary attributes for the Footer object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the MainPage class
    main_logo_fb
        This is a method to define and click Main Logo button
    click_footer_social_media_button
        This is a method to find and click footer's Social Media button
    find_footer_social_media_button
        This is a method to find footer's Social Media link
    find_footer_social_media_buttons
        This is a method to find footer's Social Media buttons list
    click_footer_social_media_link
        This is a method to find and click footer's Social Media link
    find_footer_social_media_link
        This is a method to find footer's Social Media link
    find_footer_social_media_links
        This is a method to find footer's Social Media links list
    click_footer_legal_link
        This is a method to find and click footer's Legal link
    find_footer_legal_link
        This is a method to find footer's Legal link
    find_footer_legal_links
        This is a method to find footer's Legal links list
    click_footer_about_us_link
        This is a method to find and click footer's About Us link
    find_footer_about_us_link
        This is a method to find footer's About Us link
    find_footer_about_us_links
        This is a method to find footer's About Us links list
    """

    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainMenu class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def main_logo_fb(self) -> None:
        """This is a method to define and click Main Logo button."""
        wait = WebDriverWait(self.driver, 10)
        self.main_logo_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, MAIN_LOGO_FL)))
        self.main_logo_button.click()

    def click_footer_social_media_link(self, index: int) -> None:
        """This is a method to find and click footer's Social Media link."""
        self.footer_social_media_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_SOCIAL_MEDIA_LINKS_LIST_ITEMS}[{index}]")
        self.footer_social_media_link_n.click()

    def find_footer_social_media_link(self, index: int) -> None:
        """This is a method to find footer's Social Media link."""
        self.footer_social_media_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_SOCIAL_MEDIA_LINKS_LIST_ITEMS}[{index}]")

    def find_footer_social_media_links(self) -> None:
        """This is a method to find footer's Social Media links list."""
        self.footer_social_media_links_list =  list(self.driver.find_elements(
            By.XPATH, FOOTER_SOCIAL_MEDIA_LINKS_LIST_ITEMS))
        
    def click_footer_about_us_link(self, index: int) -> None:
        """This is a method to find and click footer's About Us link."""
        self.footer_about_us_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_ABOUT_US_LINKS_LIST_ITEMS}[{index}]")
        self.footer_about_us_link_n.click()
        
    def find_footer_about_us_link(self, index: int) -> None:
        """This is a method to find footer's About Us link."""
        self.footer_about_us_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_ABOUT_US_LINKS_LIST_ITEMS}[{index}]")
        
    def find_footer_about_us_links(self) -> None:
        """This is a method to find footer's About Us links list."""
        self.footer_about_us_links_list =  list(self.driver.find_elements(
            By.XPATH, FOOTER_ABOUT_US_LINKS_LIST_ITEMS))

    def click_footer_legal_link(self, index: int) -> None:
        """This is a method to find and click footer's Legal link."""
        self.footer_legal_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_LEGAL_LINKS_LIST_ITEMS}[{index}]")
        self.footer_legal_link_n.click()

    def find_footer_legal_link(self, index: int) -> None:
        """This is a method to find footer's Legal link."""
        self.footer_legal_link_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_LEGAL_LINKS_LIST_ITEMS}[{index}]")
          
    def find_footer_legal_links(self) -> None:
        """This is a method to find footer's Legal links list."""
        self.footer_legal_links_list =  list(self.driver.find_elements(
            By.XPATH, FOOTER_LEGAL_LINKS_LIST_ITEMS))
        
    def click_footer_social_media_button(self, index: int) -> None:
        """This is a method to find and click footer's Social Media button."""
        self.footer_social_media_button_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS}[{index}]")
        self.footer_social_media_button_n.click()

    def find_footer_social_media_button(self, index: int) -> None:
        """This is a method to find footer's Social Media link."""
        self.footer_social_media_button_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS}[{index}]")
        
    def find_footer_social_media_buttons(self) -> None:
        """This is a method to find footer's Social Media buttons list."""
        self.footer_social_media_buttons_list =  list(self.driver.find_elements(
            By.XPATH, FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS))
