from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver


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
    facebook
        This is a method to find and define Facebook button
    instagram
        This is a method to find and define Instagram button
    tiktok
        This is a method to find and define Tiktok button
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
        self.main_logo_button = self.driver.find_element(
            By.XPATH, MAIN_LOGO_FL)
        self.main_logo_button.click()

    def facebook_fl(self) -> None:
        """This is a method to find and define Facebook link."""
        self.facebook_link = self.driver.find_element(
            By.LINK_TEXT, FACEBOOK_FL)
        
    def instagram_fl(self) -> None:
        """This is a method to find and define Instagram link."""
        self.instagram_link = self.driver.find_element(
            By.LINK_TEXT, INSTAGRAM_FL)
        
    def tiktok_fl(self) -> None:
        """This is a method to find and define Tiktok link."""
        self.tiktok_link = self.driver.find_element(
            By.LINK_TEXT, TIKTOK_FL)
    
    def about_us(self) -> None:
        """This is a method to find and define About Us link."""
        self.about_us_link = self.driver.find_element(
            By.XPATH, ABOUT_US)
        
    def contacts(self) -> None:
        """This is a method to find and define Contacts link."""
        self.contacts_link = self.driver.find_element(
            By.XPATH, CONTACTS)
        
    def payment(self) -> None:
        """This is a method to find and define Payment link."""
        self.payment_link = self.driver.find_element(
            By.XPATH, PAYMENT)
    
    def public_oferta(self) -> None:
        """This is a method to find and define Public Oferta link."""
        self.public_oferta_link = self.driver.find_element(
            By.XPATH, PUBLIC_OFERTA)
        
    def privacy_policy(self) -> None:
        """This is a method to find and define Privacy Policy link."""
        self.privacy_policy_link = self.driver.find_element(
            By.XPATH, PRIVACY_POLICY)
        
    def facebook_fb(self) -> None:
        """This is a method to find and define Facebook button."""
        self.facebook_fb_button = self.driver.find_element(
            By.XPATH, FACEBOOK_FB)
        self.facebook_fb_button.click()

    def instagram_fb(self) -> None:
        """This is a method to find and define Instagram button."""
        self.instagram_fb_button = self.driver.find_element(
            By.XPATH, INSTAGRAM_FB)
        self.instagram_fb_button.click()
        
    def tiktok_fb(self) -> None:
        """This is a method to find and define Tiktok button."""
        self.tiktok_fb_button = self.driver.find_element(
            By.XPATH, TIKTOK_FB)
        self.tiktok_fb_button.click()


    



    
