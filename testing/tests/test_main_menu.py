import pytest
from testing.pages.main_page import MainPage
from testing.pages.hm_form import HelpMeForm
from testing.pages.main_menu import MainMenu
from testing.pages.catalog_dropdown import CatalogDropdown
from testing.pages.cart import CartPage
from testing.lib.constants import MAIN_URL, \
                                  MAIN_PAGE_TITLE, \
                                  CONTACT_PHONE_NUMBER, \
                                  DISCOUNT_5, \
                                  DISCOUNT_MESSAGE
import time
import logging


logger = logging.getLogger('leyven_tests_logger')

@pytest.mark.with_logging
def test_main_menu(browser: object):
    driver = browser
    main_page = MainPage(driver)

    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    time.sleep(1)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    main_menu = MainMenu(driver)
    # 1.1. Hover mouse over Catalog button
    logger.info(f"1.1. Hover mouse over Catalog button.")
    main_menu.catalog()
    assert main_menu.catalog_button.is_enabled()
    assert main_menu.catalog_button.is_displayed()
    time.sleep(1)
    

    catalog_dropdown = CatalogDropdown(driver)
    # 1.2. Ensure that Catalog Dropdown container is displayed
    catalog_dropdown.catalog_dropdown()
    assert catalog_dropdown.catalog_dropdown_container.is_enabled()
    assert catalog_dropdown.catalog_dropdown_container.is_displayed()
    logger.info(f"1.2. Catalog Dropdown container appears.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 2. Click the Main Logo to return to the main page
    
    main_menu = MainMenu(driver)

    logger.info(f"2.1. Click the Main Logo to return to the main page.")
    main_menu.click_main_logo()
    assert main_menu.main_logo_button.is_enabled(), \
        "Main logo button is not enabled."
    assert main_menu.main_logo_button.is_displayed(), \
        "Main logo button is not displayed."
    logger.info(f"2.2. The main logo is clicked.")
    

    current_page_title = driver.title
    logger.info(f"2.3. Ensure that page with the title "
                f"'{current_page_title}' is opened.")
    expected_title = MAIN_PAGE_TITLE
    assert current_page_title == expected_title,\
    f"Expected title is '{expected_title}', but got '{current_page_title}'"
    time.sleep(3)

    logger.info(f"2.4. Expected title is '{MAIN_PAGE_TITLE}', "
                f"and got '{current_page_title}'")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 3.Input some query into Search field
    logger.info(f"3.1. Input some query into Search field.")
    main_menu.search_out()
    assert main_menu.search_field_out.is_enabled()
    assert main_menu.search_field_out.is_displayed()
    main_menu.search_inn("dog")
    time.sleep(3)
    logger.info(f"3.2. Search query is inputted and shown in the search field.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 4.Click Cross Button
    logger.info(f"4.1. Click Cross Button.")
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
    time.sleep(3)
    logger.info(f"4.2. Cross Button is clicked and hidden the search field.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 5.Hover mouse over Phone button
    logger.info(f"5.1. Hover mouse over Phone button.")
    main_menu.hover_over_phone()
    assert main_menu.phone_button.is_enabled()
    assert main_menu.phone_button.is_displayed()
    logger.info(f"5.2. Phone button is hovered and tooltip is displayed.")
    
    tooltip_text = main_menu.tooltip.text
    logger.info(f"5.3. Ensure that Tooltip is visible and has correct text.")
    assert main_menu.tooltip.is_enabled(), "Tooltip is not enabled."
    assert main_menu.tooltip.is_displayed(), "Tooltip is not displayed."
    assert main_menu.tooltip.text == "Натисніть, щоб скопіювати"
    logger.info(f"5.4. Tooltip is visible and has correct '{tooltip_text}' text.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    time.sleep(3)

    # 6.Find and click social media buttons
    main_menu.find_social_media_buttons()
    for i in range((len(main_menu.social_media_buttons_list) + 1) // 2):
        logger.info(f"6.{i + 1}.1. Click Social Media Button {i + 1}.")
        main_menu.click_social_media_button(i + 1)
        assert main_menu.social_media_button_n.is_enabled(), \
            f"Social media button {i} is not enabled."
        assert main_menu.social_media_button_n.is_displayed(), \
            f"Social media button {i} is not displayed."
        time.sleep(1)
        logger.info(f"6.{i + 1}.2. Social Media Button {i + 1} is clicked.")
       

        # It goes to the social media page close it and returns back 
        # to the Main Page 
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        driver.close()
        driver.switch_to.window(window_handles[0])
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 7.Find and click Language Switcher button
    logger.info(f"7.1. Find and click Language Switcher button.")
    main_menu.find_language_switcher()
    assert main_menu.language_button.is_enabled()
    # assert main_menu.language_button.is_displayed()
    time.sleep(3)
    logger.info(f"7.2. Language Switcher button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 8.Find and click Log In button
    main_menu.log_in()

    logger.info(f"8.1. Find and click Log In button.")
    assert main_menu.log_in_button.is_enabled(), \
        "Log In button is not enabled."
    assert main_menu.log_in_button.is_displayed(), \
        "Log In button is not displayed."
    main_menu.log_in_button.click()
    logger.info(f"8.2. Log In button is clicked.")

    logger.info(f"8.3. Ensure that Sign In form is opened.")
    main_menu.find_sign_in_button()
    assert main_menu.sign_in_button.is_enabled(), \
        "Sign In button is not enabled."
    assert main_menu.sign_in_button.is_displayed(), \
        "Sign In button is not displayed."

    logger.info(f"8.4. 'Sign In' form is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    time.sleep(3)
    driver.back()
    time.sleep(3)

    cart_page = CartPage(driver)
    # 9.Find and click Cart button
    logger.info(f"9.1. Find and click Cart button.")
    main_menu.click_cart_button()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    time.sleep(3)
    logger.info(f"9.2. The Cart button is clicked.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    logging.info(f"9.3. Find and click Close Cart button.")
    cart_page.close_cart()
    # assert cart_page.close_cart_button.is_enabled()
    # assert cart_page.close_cart_button.is_displayed()
    logging.info(f"9.4. Cart is closed.")
    logging.info(f"[PASSED]\n{'=' * 200}")

    # 10.Ensure the phone number is correct
    logger.info(f"10.1. Ensure that the phone number is correct.")
    main_menu.find_the_phone_number()
    assert main_menu.phone_number_text.is_enabled(), "Phone button is not enabled."
    assert main_menu.phone_number_text.is_displayed(), \
        "Phone button is not displayed."
    assert main_menu.phone_text == CONTACT_PHONE_NUMBER, \
        (f"Expected phone number is {CONTACT_PHONE_NUMBER}, "
         f"but got {main_menu.phone_text}")

    logger.info(f"10.2. Expected phone is {CONTACT_PHONE_NUMBER} and got "
                f"{main_menu.phone_text}.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 11.Enasure that the greeting message is correct
    logger.info(f"11.1. Ensure that the greeting message is correct.")
    main_menu.find_greeting_message()
    assert main_menu.greeting_message.is_enabled(), "Greeting message is not enabled."
    assert main_menu.greeting_message.is_displayed(), "Greeting message is not displayed."
    assert main_menu.greeting_text == DISCOUNT_MESSAGE, \
        (f"Expected greeting message is {DISCOUNT_MESSAGE}, "
         f"but got {main_menu.greeting_text}")
    logger.info(f"11.2. Expected greeting is '{DISCOUNT_MESSAGE}' and got "
                f"'{main_menu.greeting_text}'.")
    logger.info(f"[PASSED]\n{'=' * 200}")
