from testing.pages.main_page import *
from testing.lib.constants import *
import time
import random


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)
    
    # 2.Ensure that Product Card Items in New Arrival is displayed
    # and clickable (Dynamic)
    main_page.new_arrival_cards()
    for e in range(1, len(main_page.new_arrival_cards_n), 2):    
            time.sleep(3)
            main_page.new_arrival_card(e)
            assert main_page.new_arrival_card_n.is_enabled()
            assert main_page.new_arrival_card_n.is_displayed()
            time.sleep(3)
            driver.back()

    # 3.Find and click SHOW_ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    main_page.show_all_button.click()
    time.sleep(3)

    # 4.Ensure that Product Card Items are displayed and clickable (Dynamic)
    main_page.product_cards()
    step = random.randint(1,8)
    print(step)
    # for e in range(len(main_page.product_cards_n), 1, -7):
    for e in range(1, len(main_page.product_cards_n), step):    
            time.sleep(3)
            main_page.product_card(e)
            assert main_page.product_card_n.is_enabled()
            assert main_page.product_card_n.is_displayed()
            time.sleep(3)
            driver.back()

    # 5.Ensure that Hot Proposal Product Card Items are displayed and clickable 
    # (Dynamic)
    main_page.hot_proposal_cards()
    step = random.randint(1,8)
    print(step)
    for e in range(1, len(main_page.hot_proposal_cards_n), step):    
            time.sleep(3)
            main_page.hot_proposal_card(e)
            assert main_page.hot_proposal_card_n.is_enabled()
            assert main_page.hot_proposal_card_n.is_displayed()
            time.sleep(3)
            driver.back()
