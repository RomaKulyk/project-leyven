import pytest
from testing.pages.main_page import MainPage
from testing.pages.hm_form import HelpMeForm
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
import time


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    
    # 2.Find and click GO_TO_CATEGORY_1 button
    main_page.find_go_to_category(2)
    assert main_page.go_to_category_button.is_enabled()
    assert main_page.go_to_category_button.is_displayed()
    main_page.click_go_to_category(2)

    main_menu = MainMenu(driver)
    # 3.Find and click MAIN_LOGO button
    main_menu.click_main_logo()
    assert main_menu.main_logo_button.is_enabled()
    assert main_menu.main_logo_button.is_displayed()

    # 4.Find and click GO_TO_CATEGORY_2 button
    main_page.find_go_to_category(3)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    main_page.click_go_to_category(3)

    main_page.product_cards()
    # 5.Find and click first Product Card in the list
    main_page.product_card(5)
    # assert main_page.product_card_n.is_enabled()
    # assert main_page.product_card_n.is_displayed()
    time.sleep(1)
    driver.back()
   
    # 6.Find and click 18th Product Card in the list
    main_page.product_card(18)
    assert main_page.product_card_n.is_enabled()
    assert main_page.product_card_n.is_displayed()
    time.sleep(1)
    driver.back()
    
    # 7.Find and click 18th Product Card in the list
    main_page.product_card(36)
    assert main_page.product_card_n.is_enabled()
    assert main_page.product_card_n.is_displayed()
    time.sleep(1)
    driver.back()
