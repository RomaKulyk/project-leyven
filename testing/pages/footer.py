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
    main_logo
        This is a method to define and click Main Logo button
    facebook_fl
        This is a method to find and define Facebook link
    instagram_fl
        This is a method to find and define Instagram link
    tiktok_fl
        This is a method to find and define Tiktok link
    about_us
        This is a method to find and define About Us link
    contacts
        This is a method to find and define Contacts link
    payment
        This is a method to find and define Payment link
    public_oferta
        This is a method to find and define Public Oferta link
    privacy_policy
        This is a method to find and define Privacy Policy link
    click_footer_social_media_button
        This is a method to find and click footer's Social Media button
    find_footer_social_media_buttons
        This is a method to find footer's Social Media buttons list
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

    def facebook_fl(self) -> None:
        """This is a method to find and define Facebook link."""
        wait = WebDriverWait(self.driver, 10)
        self.facebook_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, FACEBOOK_FL)))
        
    def instagram_fl(self) -> None:
        """This is a method to find and define Instagram link."""
        wait = WebDriverWait(self.driver, 10)
        self.instagram_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, INSTAGRAM_FL)))
        
    def tiktok_fl(self) -> None:
        """This is a method to find and define Tiktok link."""
        wait = WebDriverWait(self.driver, 10)
        self.tiktok_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, TIKTOK_FL)))
    
    def about_us(self) -> None:
        """This is a method to find and define About Us link."""
        wait = WebDriverWait(self.driver, 10)
        self.about_us_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, ABOUT_US)))
        
    def contacts(self) -> None:
        """This is a method to find and define Contacts link."""
        wait = WebDriverWait(self.driver, 10)
        self.contacts_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, CONTACTS)))
                 
    def payment(self) -> None:
        """This is a method to find and define Payment link."""
        wait = WebDriverWait(self.driver, 10)
        self.payment_link = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, PAYMENT)))
    
    def public_oferta(self) -> None:
        """This is a method to find and define Public Oferta link."""
        wait = WebDriverWait(self.driver, 10)
        self.public_oferta_link= wait.until(EC.element_to_be_clickable((
            By.XPATH, PUBLIC_OFERTA)))
        
    def privacy_policy(self) -> None:
        """This is a method to find and define Privacy Policy link."""
        wait = WebDriverWait(self.driver, 10)
        self.privacy_policy_link = wait.until(EC.element_to_be_clickable((
            By.XPATH, PRIVACY_POLICY)))
    
    def click_footer_social_media_button(self, index: int) -> None:
        """This is a method to find and click footer's Social Media button."""
        self.footer_social_media_button_n = self.driver.find_element(
            By.XPATH, f"{FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS}[{index}]")
        self.footer_social_media_button_n.click()

    def find_footer_social_media_buttons(self) -> None:
        """This is a method to find footer's Social Media buttons list."""
        self.footer_social_media_buttons_list =  list(self.driver.find_elements(
            By.XPATH, FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS))
