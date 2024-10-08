from selenium.webdriver.common.by import By
from testing.lib.constants import *
from selenium import webdriver

class HelpMeForm:
    """
    Constructs all the necessary attributes for the HelpMeForm object.
    Attributes:
    webdriver:object
                It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the MainPage class
    enter_username
        This is a method to find, clear and enter username into form
    enter_phone
        This is a method to find, clear and enter phone into form
    enter_your_question
        This is a method to find, clear and enter password into form
    click_send
        This is a method to find and click Send button on form
    """
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def enter_username(self, user_input: str) -> None:
        """
        This is a method to find, clear and enter username into form.
        Parameters
        user_input:str
                   Username to log in with
        """
        self.user_name_input = self.driver.find_element(
            By.XPATH, ENTER_USERNAME)
        self.user_name_input.clear()
        self.user_name_input.send_keys(user_input)

    def enter_phone(self, phone: str) -> None:
        """
        This is a method to find, clear and enter phone into form.
        Parameters
        phone:str
                 Phone to log in with
        """
        phone_input = self.driver.find_element(
            By.XPATH, ENTER_PHONE)
        phone_input.clear()
        phone_input.send_keys(phone)

    def enter_your_question(self, question: str) -> None:
        """
        This is a method to find, clear and enter question into form.
        Parameters
        question:str
                 Question you have
        """
        e_y_q_input = self.driver.find_element(
            By.XPATH, ENTER_YOUR_QUESTION)
        e_y_q_input.clear()
        e_y_q_input.send_keys(question)
   
    def click_send(self) -> None:
        """This is a method to find and click Send button on form."""
        self.send_button = self.driver.find_element(
            By.XPATH, CLICK_SEND)
        self.send_button.click()