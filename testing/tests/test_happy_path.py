from testing.pages.main_page import *
from testing.lib.constants import *
from testing.pages.cart import *
from testing.pages.page import *
import time
import random


def test_main_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)


    cart_page = CartPage(driver)
    # 6.Find and click SHOW ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    main_page.show_all_button.click()
    time.sleep(1)

    page = InventoryPage(driver)
    # 7.Add product 1 to cart from product's category page
    page.to_buy(TO_BUY_1)
    time.sleep(1)
    
    # 8.Find and click CONTINUE_SHOPPING button
    cart_page.close_cart()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    time.sleep(1)
    
    # 9.Add product 2 to cart from product's category page
    page.to_buy(TO_BUY_2)
    time.sleep(1)






    #     # 2.1 Add product from Hot Proposal category to cart
#     main_page.mp_to_buy(1)
#     time.sleep(3)
#     cart_page.continue_shopping()

#     # 2.2 Add product from Hot Proposal category to cart
#     main_page.mp_to_buy(2)
#     time.sleep(3)
#     cart_page.continue_shopping()