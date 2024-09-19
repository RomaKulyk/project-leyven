from selenium import webdriver
import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.pages.main_menu import *
from testing.lib.constants import *
import time


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
    # for e in range(1,len(main_page.product_cards_n)):
    # for e in range(len(main_page.product_cards_n), 1, -7):
    for e in range(1, len(main_page.product_cards_n), 3):    
            time.sleep(3)
            main_page.product_card(e)
            assert main_page.product_card_n.is_enabled()
            assert main_page.product_card_n.is_displayed()
            time.sleep(3)
            driver.back()
