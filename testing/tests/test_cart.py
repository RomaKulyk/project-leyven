import pytest
from testing.pages.main_page import MainPage
from testing.pages.cart import CartPage
from testing.pages.main_menu import MainMenu
from testing.pages.inventory_page import InventoryPage
from testing.lib.constants import MAIN_URL,\
                                  TO_BUY_1,\
                                  TO_BUY_2,\
                                  REMOVE_PDP_1
import logging


logger = logging.getLogger('leyven_tests_logger')

@pytest.mark.with_logging
def test_cart_page(browser: object):
    """Test to ensure that Cart functionality works correctly."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)

    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 2.Find and click CART button
    logger.info(f"2.1. Find and click Cart button.")
    main_menu.click_cart_button()
    assert main_menu.cart_button.is_enabled(), \
        "Cart button is not enabled."
    assert main_menu.cart_button.is_displayed(), \
        "Cart button is not displayed."
    logger.info(f"2.2. The Cart button is clicked.")

    main_menu.find_cart_popup()
    # 2.1 Ensure that Cart popup is displayed
    logger.info(f"2.3. Ensure that Cart popup is opened.")
    assert main_menu.cart_popup.is_enabled(), \
        "Cart popup is not enabled."
    assert main_menu.cart_popup.is_displayed(), \
        "Cart popup is not displayed."
    


    
    logger.info(f"2.4. Cart popup is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    cart_page = CartPage(driver)
    # 3.Find and click CONTINUE SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()

    # 4.Find and click CART button
    main_menu.click_cart_button()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()

    # 5.Find and click CLOSE CART button
    cart_page.close_cart()
    assert cart_page.close_cart_button.is_enabled()
    # assert cart_page.close_cart_button.is_displayed()
    
    # 6.Find and click GO_TO_CATEGORY_1 button
    main_page.find_go_to_category(2)
    assert main_page.go_to_category_button.is_enabled()
    assert main_page.go_to_category_button.is_displayed()
    main_page.click_go_to_category(2)

    page = InventoryPage(driver)
    # 7.Add product 1 to cart from product's category page
    page.to_buy(TO_BUY_1)
            
    # 8.Find and click CONTINUE_SHOPPING button
    cart_page.close_cart()
    assert cart_page.continue_shopping_button.is_enabled()
    # assert cart_page.continue_shopping_button.is_displayed()
        
    # 9.Add product 2 to cart from product's category page
    page.to_buy(TO_BUY_2)
        
    # 10.Remove product 1 from cart
    cart_page.remove_pdp(REMOVE_PDP_1)
    
    # 11.Find and click CHECKOUT button
    cart_page.checkout()
    assert cart_page.checkout_button.is_enabled()
    # assert cart_page.checkout_button.is_displayed()
        
    # 12. Return back to the main page
    main_menu.click_main_logo()


