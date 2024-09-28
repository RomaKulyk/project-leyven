import pytest
from testing.pages.main_page import *
from testing.pages.cart import *
from testing.pages.main_menu import *
from testing.lib.constants import *
from testing.pages.page import *
import time


def test_cart_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    main_menu = MainMenu(driver)
    # 2.Find and click CART button
    main_menu.cart()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    time.sleep(1)

    cart_page = CartPage(driver)
    # 3.Find and click CONTINUE SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    time.sleep(1)

    # 4.Find and click CART button
    main_menu.cart()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    time.sleep(1)

    # 5.Find and click CLOSE CART button
    cart_page.close_cart()
    assert cart_page.close_cart_button.is_enabled()
    assert cart_page.close_cart_button.is_displayed()
    time.sleep(1)
    
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

    # 10.Remove product 1 from cart
    cart_page.remove_pdp(REMOVE_PDP_1)
    time.sleep(1)

    # 11.Find and click CHECKOUT button
    cart_page.checkout()
    assert cart_page.checkout_button.is_enabled()
    assert cart_page.checkout_button.is_displayed()
    time.sleep(1)
    
    # 12. Return back to the main page
    main_menu.main_logo()
    time.sleep(1)

    

