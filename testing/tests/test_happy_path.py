from testing.pages.main_page import MainPage
from testing.pages.cart import CartPage
from testing.pages.checkout_page import CheckoutPage
from testing.pages.inventory_page import InventoryPage
from testing.lib.constants import MAIN_URL,\
                                  TO_BUY_1,\
                                  TO_BUY_2,\
                                  TO_BUY_5,\
                                  TO_BUY_6,\
                                  PHONE_NUMBER,\
                                  FIRST_NAME,\
                                  LAST_NAME,\
                                  EMAIL,\
                                  DELIVERY_CITY

import time


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1. Open MAIN_URL page
    main_page.open_page(MAIN_URL)

    # 2. Find and click GO_TO_CATEGORY_1 button
    main_page.find_go_to_category(2)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_1 button is not enabled."
    assert main_page.go_to_category_button.is_displayed()
    main_page.click_go_to_category(2)

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
    main_page.find_go_to_category(3)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    main_page.click_go_to_category(3)

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
    time.sleep(3)
    # cart_page.continue_shopping_button.click()
    cart_page.checkout()
     
    checkout_page = CheckoutPage(driver)
    checkout_page.check_if_page_is_loaded()
    checkout_page.find_the_h1_header()
    checkout_page.print_my_current_url()

    # 13. Fill in the checkout form
    # Fill in the contact phone number, first name, last name, email, city
    checkout_page.input_contact_phone(PHONE_NUMBER)
    checkout_page.input_first_name(FIRST_NAME)
    checkout_page.input_last_name(LAST_NAME)
    checkout_page.input_email(EMAIL)
    checkout_page.input_delivery_city(DELIVERY_CITY)
    time.sleep(3)

    # 14. Select delivery method "Новою поштою" (Postomat)
    checkout_page.click_delivery_radio_button_pm_np()
    assert checkout_page.click_delivery_radio_button_pm_np_rb.is_enabled()
    assert checkout_page.click_delivery_radio_button_pm_np_rb.is_displayed()
    time.sleep(3)

    # 15. Select delivery method "Новою поштою" (Warehouse)
    checkout_page.click_delivery_radio_button_wh_np()
    assert checkout_page.click_delivery_radio_button_wh_np_rb.is_enabled()
    assert checkout_page.click_delivery_radio_button_wh_np_rb.is_displayed()
    time.sleep(3)

    # 16. Select delivery method "Укрпоштою" (Warehouse)
    checkout_page.click_delivery_radio_button_wh_up()
    assert checkout_page.click_delivery_radio_button_wh_up_rb.is_enabled()
    assert checkout_page.click_delivery_radio_button_wh_up_rb.is_displayed()
    time.sleep(3)

    # 17. Select payment method "Оплата онлайн" (Payment by card)
    checkout_page.choose_payment_by_card()
    assert checkout_page.choose_payment_by_card_rb.is_enabled()
    assert checkout_page.choose_payment_by_card_rb.is_displayed()
    time.sleep(3)
    
    # 18. Select payment method "Оплата карткою за реквізитами" 
    # (Payment by bank details)
    checkout_page.choose_payment_by_bank_details()
    assert checkout_page.choose_payment_by_bank_details_rb.is_enabled()
    assert checkout_page.choose_payment_by_bank_details_rb.is_displayed()
    time.sleep(3)
    
    # 19. Select payment method "Готівкою або карткою: при отриманні" 
    # (Cash on delivery)
    checkout_page.choose_cash_on_delivery()
    assert checkout_page.choose_cash_on_delivery_rb.is_enabled()
    assert checkout_page.choose_cash_on_delivery_rb.is_displayed()
    time.sleep(3)
    
    # 20. Ensure the checkbox "Не зв'язуватися для додаткового підтвердження" is
    # not selected. Select the checkbox
    checkout_page.ensure_no_contact_checkbox_is_selected()
    assert not checkout_page.pick_no_contact_checkbox_cb.is_selected()

    checkout_page.pick_no_contact_checkbox()
    assert checkout_page.pick_no_contact_checkbox_cb.is_enabled()
    assert checkout_page.pick_no_contact_checkbox_cb.is_displayed()
    time.sleep(3)

    # 21. Go back to the previous page
    driver.back()

