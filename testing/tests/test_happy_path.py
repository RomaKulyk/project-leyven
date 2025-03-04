from testing.pages.main_page import MainPage
from testing.pages.cart import CartPage
from testing.pages.inventory_page import InventoryPage
from testing.lib.constants import MAIN_URL,\
                                  TO_BUY_1,\
                                  TO_BUY_2,\
                                  TO_BUY_5,\
                                  TO_BUY_6
import time


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1. Open MAIN_URL page
    main_page.open_page(MAIN_URL)

    # 2. Find and click GO_TO_CATEGORY_1 button
    main_page.go_to_category_1()
    assert main_page.go_to_category_1_button.is_enabled()
    assert main_page.go_to_category_1_button.is_displayed()
    main_page.go_to_category_1_button.click()

    page = InventoryPage(driver)
    time.sleep(3)
    # 3. Add product 1 to cart from product's category page
    page.to_buy(TO_BUY_1)
    
    cart_page = CartPage(driver)
    # 4. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    
    page = InventoryPage(driver)
    # 5. Add product 2 to cart from product's category page
    page.to_buy(TO_BUY_2)

    # 6. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    driver.back()
    
    main_page = MainPage(driver)

    # 7. Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    main_page = MainPage(driver)
    # 8. Find and click GO_TO_CATEGORY_2 button
    main_page.go_to_category_2()
    assert main_page.go_to_category_2_button.is_enabled()
    assert main_page.go_to_category_2_button.is_displayed()
    main_page.go_to_category_2_button.click()

    page = InventoryPage(driver)
    time.sleep(3)
    # 9. Add product 1 to cart from product's category page
    page.to_buy(TO_BUY_5)
    
    cart_page = CartPage(driver)
    # 10. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    
    page = InventoryPage(driver)
    # 11. Add product 2 to cart from product's category page
    page.to_buy(TO_BUY_6)

    # 12. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_enabled()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    driver.back()
