from testing.pages.main_page import MainPage
from testing.lib.constants import MAIN_URL, TO_BUY_1, TO_BUY_2
from testing.pages.cart import CartPage
from testing.pages.inventory_page import InventoryPage
from selenium.webdriver.common.action_chains import ActionChains


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1. Open MAIN_URL page
    main_page.open_page(MAIN_URL)

    cart_page = CartPage(driver)
    # 2. Find and click GO_TO_CATEGORY_1 button
    main_page.go_to_category_1()
    assert main_page.go_to_category_1_button.is_enabled()
    assert main_page.go_to_category_1_button.is_displayed()
    main_page.go_to_category_1_button.click()

    page = InventoryPage(driver)
    # 3. Add product 1 to cart from product's category page
    page.to_buy(TO_BUY_1)
    
    # 4. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_displayed()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    
    page = InventoryPage(driver)
    # 5. Add product 2 to cart from product's category page
    page.to_buy(TO_BUY_2)

    # 6. Find and click CONTINUE_SHOPPING button
    cart_page.continue_shopping()
    assert cart_page.continue_shopping_button.is_displayed()
    assert cart_page.continue_shopping_button.is_displayed()
    cart_page.continue_shopping_button.click()
    driver.back()
    
    # # 7. Add product from Hot Proposal category to cart
    # main_page.mp_to_buy(1)
    # time.sleep(3)
    # cart_page.continue_shopping()
    # assert cart_page.continue_shopping_button.is_displayed()
    # assert cart_page.continue_shopping_button.is_displayed()
    # 
    # cart_page.continue_shopping_button.click()
    # time.sleep(3)
    # # 8. Add product from Hot Proposal category to cart
    # main_page.mp_to_buy(2)
    # time.sleep(3)
    # cart_page.continue_shopping()
    # assert cart_page.continue_shopping_button.is_displayed()
    # assert cart_page.continue_shopping_button.is_displayed()
    # 
    # cart_page.continue_shopping_button.click()

    # time.sleep(3)

    # main_page.new_arrivals()
    # action = ActionChains(driver)        
    # # action.scroll_to_element(main_page.show_all_button)
    # action.scroll_to_element(main_page.new_arrival_span)
    # action.perform()
    # # driver.execute_script("window.scrollTo(300, document.body.scrollHeight);")
    # # time.sleep(3)
    

    # # 9. Add product from New Arrival category to cart
    # main_page.hp_to_buy(1)
    # time.sleep(3)
    # cart_page.continue_shopping()
    # assert cart_page.continue_shopping_button.is_displayed()
    # assert cart_page.continue_shopping_button.is_displayed()
    # time.sleep(3)
    # cart_page.continue_shopping_button.click()
    # time.sleep(3)

    # # 10. Add product from New Arrival category to cart
    # main_page.hp_to_buy(6)
    # time.sleep(3)
    # cart_page.continue_shopping()
    # assert cart_page.continue_shopping_button.is_displayed()
    # assert cart_page.continue_shopping_button.is_displayed()
    # time.sleep(3)
    # cart_page.continue_shopping_button.click()
    # time.sleep(3)

    driver.back()
