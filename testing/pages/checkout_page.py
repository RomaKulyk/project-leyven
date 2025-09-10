from selenium.webdriver.common.by import By
from testing.pages.category_page import CategoryPage
from testing.lib.constants import CHECKOUT_PHONE,\
                                  CHECKOUT_FIRST_NAME,\
                                  CHECKOUT_LAST_NAME,\
                                  CHECKOUT_EMAIL, \
                                  CHECKOUT_DELIVERY_CITY,\
                                  RB_WH_NP,\
                                  RB_PM_NP,\
                                  RB_WH_UP,\
                                  RB_CARD,\
                                  RB_PAYMENT_BY_BANK_DETAILS,\
                                  RB_CASH_ON_DELIVERY,\
                                  CHECKBOX_NO_CONTACT

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage(CategoryPage):
    """
    Constructs all the necessary attributes for the CheckoutPage object.
    Attributes:
    webdriver:object
        It is an object of webdriver class
    Methods:
    __init__
        This is a method to initialize instance of the CheckoutPage class
    input_contact_phone
        This is a method to enter contact phone into form
    input_first_name
        This is a method to enter first name into form
    input_last_name
        This is a method to enter last name into form
    input_email
        This is a method to enter email into form
    input_delivery_city
        This is a method to enter city into form
    click_delivery_radio_button_wh_np
        This is a method to find and click radio button
    click_delivery_radio_button_pm_np
        This is a method to find and click radio button
    click_delivery_radio_button_wh_up
        This is a method to find and click radio button
    choose_payment_by_card
        This is a method to choose payment by card radio button
    choose_payment_by_bank_details
        This is a method to choose payment by bank details radio button
    choose_cash_on_delivery
        This is a method to choose cash on delivery radio button
    ensure_no_contact_checkbox_is_selected
        This is a method to ensure "No contact" checkbox is selected
    pick_no_contact_checkbox
        This is a method to find and click "No contact" checkbox
    """
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the CheckoutPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver

    def input_contact_phone(self, phone: str) -> None:
        """
        This is a method to find, clear and enter phone into form.
        Parameters
        phone:str
            Phone to log in with
        """
        phone_input = self.driver.find_element(By.XPATH, CHECKOUT_PHONE)
        phone_input.clear()
        phone_input.send_keys(phone)

    def input_first_name(self, first_name: str) -> None:
        """
        This is a method to find, clear and enter first name into form.
        Parameters
        first_name:str
            First name to log in with
        """
        first_name_input = self.driver.find_element(
            By.XPATH, CHECKOUT_FIRST_NAME)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def input_last_name(self, last_name: str) -> None:
        """
        This is a method to find, clear and enter last name into form.
        Parameters
        last_name:str
            Last name to log in with
        """
        last_name_input = self.driver.find_element(
            By.XPATH, CHECKOUT_LAST_NAME)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def input_email(self, email: str) -> None:
        """
        This is a method to find, clear and enter email into form.
        Parameters
        email:str
            Email to log in with
        """
        email_input = self.driver.find_element(By.XPATH, CHECKOUT_EMAIL)
        email_input.clear()
        email_input.send_keys(email)

    def input_delivery_city(self, city: str) -> None:
        """
        This is a method to find, clear and enter city into form.
        Parameters
        city:str
            City to log in with
        """
        wait = WebDriverWait(self.driver, 10)
        self.input_delivery_city = wait.until(EC.element_to_be_clickable((
            By.XPATH, CHECKOUT_DELIVERY_CITY)))
        self.input_delivery_city.clear()
        self.input_delivery_city.send_keys(city)

    def click_delivery_radio_button_wh_np(self) -> None:
        """
        This is a method to find and click radio button.
        """
        self.click_delivery_radio_button_wh_np_rb = self.driver.find_element(
            By.XPATH,  RB_WH_NP)
        self.click_delivery_radio_button_wh_np_rb.click()

    def click_delivery_radio_button_pm_np(self) -> None:
        """
        This is a method to find and click radio button.
        """
        self.click_delivery_radio_button_pm_np_rb = self.driver.find_element(
            By.XPATH,  RB_PM_NP)
        self.click_delivery_radio_button_pm_np_rb.click()

    def click_delivery_radio_button_wh_up(self) -> None:
        """
        This is a method to find and click radio button.
        """
        self.click_delivery_radio_button_wh_up_rb = self.driver.find_element(
            By.XPATH,  RB_WH_UP)
        self.click_delivery_radio_button_wh_up_rb.click()

    def choose_payment_by_card(self) -> None:
        """
        This is a method to choose payment by card radio button.
        """
        self.choose_payment_by_card_rb = self.driver.find_element(
            By.XPATH,  RB_CARD)
        self.choose_payment_by_card_rb.click()

    def choose_payment_by_bank_details(self) -> None:
        """
        This is a method to choose payment by bank details radio button.
        """
        self.choose_payment_by_bank_details_rb = self.driver.find_element(
            By.XPATH,  RB_PAYMENT_BY_BANK_DETAILS)
        self.choose_payment_by_bank_details_rb.click()

    def choose_cash_on_delivery(self) -> None:
        """
        This is a method to choose cash on delivery radio button.
        """
        self.choose_cash_on_delivery_rb = self.driver.find_element(
            By.XPATH,  RB_CASH_ON_DELIVERY)
        self.choose_cash_on_delivery_rb.click()

    def ensure_no_contact_checkbox_is_selected(self) -> None:
        # Find checkbox element
        self.pick_no_contact_checkbox_cb = self.driver.find_element(
            By.XPATH, CHECKBOX_NO_CONTACT)

        # Check if checkbox is selected
        if self.pick_no_contact_checkbox_cb.is_selected():
            print(f"{self.pick_no_contact_checkbox_cb.get_attribute('value')}" 
                  f"checkbox is selected.")
        else:
            print(f"{self.pick_no_contact_checkbox_cb.get_attribute('value')}"
                  f"checkbox is not selected.")
    
    def pick_no_contact_checkbox(self) -> None:
        """
        This is a method to find and click "No contact" checkbox.
        """
        self.pick_no_contact_checkbox_cb = self.driver.find_element(
            By.XPATH, CHECKBOX_NO_CONTACT)
        self.pick_no_contact_checkbox_cb.click()