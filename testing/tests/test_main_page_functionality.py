import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.lib.constants import *
import time

def test_main_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    # 2.Find and click BUY_PRODUDCTS
    main_page.buy_products()
    assert main_page.buy_products_button.is_enabled()
    # assert main_page.buy_products_button.is_displayed()
    time.sleep(1)
    
    # 3.Find and click SHOW_ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    time.sleep(1)
    driver.back()

