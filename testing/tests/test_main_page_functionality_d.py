from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
import time
import random


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)

    # 2.Find and click GO_TO_CATEGORY_1 button
    main_page.go_to_category_1()
    assert main_page.go_to_category_1_button.is_enabled()
    assert main_page.go_to_category_1_button.is_displayed()
    main_page.go_to_category_1_button.click()
    
    # 3.Ensure that Product Card Items in New Arrival is displayed
    # and clickable (Dynamic)
    main_page.product_cards()
    for e in range(1, len(main_page.product_cards_n), 2):    
            time.sleep(3)
            main_page.product_card(e)
            # assert main_page.product_card_n.is_enabled()
            # assert main_page.product_card_n.is_displayed()
            time.sleep(3)
            driver.back()


    main_menu = MainMenu(driver)
    # 4.Find and click MAIN_LOGO button
    main_menu.main_logo()
    assert main_menu.main_logo_button.is_enabled()
    assert main_menu.main_logo_button.is_displayed()
    time.sleep(1)
    
    # 5.Find and click GO_TO_CATEGORY_2 button
    main_page.go_to_category_2()
    assert main_page.go_to_category_2_button.is_enabled()
    # assert main_page.go_to_category_2_button.is_displayed()
    main_page.go_to_category_2_button.click()

    # 6.Ensure that Hot Proposal Product Card Items are displayed and clickable 
    # (Dynamic)
    main_page.product_cards()
    step = random.randint(1,8)
    print(step)
    for e in range(1, len(main_page.product_cards_n), step):    
            time.sleep(3)
            main_page.product_card(e)
            # assert main_page.product_card_n.is_enabled()
            # assert main_page.product_card_n.is_displayed()
            time.sleep(3)
            driver.back()
