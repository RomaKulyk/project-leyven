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
    
    # 1. Find and click CART button
    logger.info(f"1.1. Find and click Cart button.")
    main_menu.click_cart_button()
    assert main_menu.cart_button.is_enabled(), \
        "Cart button is not enabled."
    assert main_menu.cart_button.is_displayed(), \
        "Cart button is not displayed."
    logger.info(f"1.2. The Cart button is clicked.")

    main_menu.find_cart_popup()
    # 1.1 Ensure that Cart popup is displayed
    logger.info(f"1.3. Ensure that Cart popup is opened.")
    assert main_menu.cart_popup.is_enabled(), \
        "Cart popup is not enabled."
    assert main_menu.cart_popup.is_displayed(), \
        "Cart popup is not displayed."    
    logger.info(f"1.4. Cart popup is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    cart_page = CartPage(driver)
    # 2.Find and click CONTINUE SHOPPING button
    logger.info(f"2.1. Find and click Continue Shopping button.")
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    logger.info(f"2.2. Continue Shopping button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 3.Find and click CART button
    logger.info(f"3.1. Find and click Cart button.")
    main_menu.click_cart_button()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    logger.info(f"3.2. The Cart button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 4.Find and click CLOSE CART button
    logger.info(f"4.1. Find and click Close Cart button.")
    cart_page.close_cart()
    assert cart_page.close_cart_button.is_enabled()
    # assert cart_page.close_cart_button.is_displayed()
    logger.info(f"4.2. Close Cart button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 5.Find and click GO_TO_CATEGORY_1 button
    logger.info(f"5.1. Find and click Go to Category button.")
    main_page.find_go_to_category(2)
    assert main_page.go_to_category_button.is_enabled()
    assert main_page.go_to_category_button.is_displayed()
    main_page.click_go_to_category(2)
    logger.info(f"5.2. Go to Category button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")


    page = InventoryPage(driver)
    # 6.Add product 1 to cart from product's category page
    logger.info(f"6.1. Click on product 1 to add to cart.")
    page.to_buy(TO_BUY_1)
    logger.info(f"6.2. Product 1 is added to cart.")
    logger.info(f"[PASSED]\n{'=' * 200}")


    # 7.Find and click CONTINUE_SHOPPING button
    logger.info(f"7.1. Find and click Continue Shopping button.")
    cart_page.close_cart()
    assert cart_page.continue_shopping_button.is_enabled()
    # assert cart_page.continue_shopping_button.is_displayed()
    logger.info(f"7.2. Continue Shopping button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 8.Add product 2 to cart from product's category page
    logger.info(f"8.1. Click on product 2 to add to cart.")
    page.to_buy(TO_BUY_2)
    logger.info(f"8.2. Product 2 is added to cart.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 9.Remove product 1 from cart
    logger.info(f"9.1. Find and click Remove button for product 1.")
    cart_page.remove_pdp(REMOVE_PDP_1)
    logger.info(f"9.2. Remove button for product 1 is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 10.Find and click CHECKOUT button
    logger.info(f"10.1. Find and click Checkout button.")
    cart_page.checkout()
    assert cart_page.checkout_button.is_enabled()
    # assert cart_page.checkout_button.is_displayed()
    logger.info(f"10.2. Checkout button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 11. Return back to the main page
    logger.info(f"11.1. Return back to the main page.")
    main_menu.click_main_logo()
    logger.info(f"11.2. Main logo is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")
