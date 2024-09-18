import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.pages.main_menu import *
from testing.lib.constants import *
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_main_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)
    
    # 2.Find and click SHOW_ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    main_page.show_all_button.click()
    time.sleep(3)

    # 3.Ensure that Product Card Items 1-36 is displayed and clickable (Dynamic)
    main_page.product_cards()
    for e in range(1,len(main_page.product_cards_n)):
            time.sleep(3)
            main_page.product_card(e)
            time.sleep(3)
            driver.back()
    
    # # 3.Ensure that Product Card Items 1-36 is displayed and clickable (Dynamic)
    # main_page.product_cards()
    # for e in main_page.product_cards_n:
    #         # Iterate the list using a for loop and click each options
    #         # wait = WebDriverWait(driver, 10)
    #         # e = wait.until(EC.element_to_be_clickable((
    #         # By.XPATH, PRODUCT_CARDS)))
    #         time.sleep(3)
    #         e.click()
    #         assert e.is_enabled()
    #         assert e.is_displayed()
    #         driver.back()
