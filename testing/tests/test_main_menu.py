import pytest
from testing.pages.main_page import MainPage
from testing.pages.hm_form import HelpMeForm
from testing.pages.main_menu import MainMenu
from testing.pages.catalog_dropdown import CatalogDropdown
from testing.lib.constants import MAIN_URL
import time


def test_main_menu(browser: object):
    driver = browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    main_menu = MainMenu(driver)
    # 2.Hover mouse over Catalog button
    main_menu.catalog()
    assert main_menu.catalog_button.is_enabled()
    assert main_menu.catalog_button.is_displayed()
    time.sleep(1)

    catalog_dropdown = CatalogDropdown(driver)
    # 3.Ensure that Catalog Dropdown container is displayed
    catalog_dropdown.catalog_dropdown()
    assert catalog_dropdown.catalog_dropdown_container.is_enabled()
    assert catalog_dropdown.catalog_dropdown_container.is_displayed()

    # 4.Find and click MAIN_LOGO button
    main_menu.main_logo()
    assert main_menu.main_logo_button.is_enabled()
    assert main_menu.main_logo_button.is_displayed()
    time.sleep(1)

    # 5.Input some query into Search field
    main_menu.search_out()
    assert main_menu.search_field_out.is_enabled()
    assert main_menu.search_field_out.is_displayed()
    main_menu.search_inn("dog")
    time.sleep(3)

    # 6.Click Cross Button
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
    time.sleep(3)

    # 7.Hover mouse over Phone button
    main_menu.phone()
    assert main_menu.phone_button.is_enabled()
    assert main_menu.phone_button.is_displayed()
    time.sleep(3)
    
    # 8.Find and click social media buttons
    main_menu.find_social_media_buttons()
    print(len(main_menu.social_media_buttons_list))
    print(main_menu.social_media_buttons_list)
    for i in range((len(main_menu.social_media_buttons_list) + 1) // 2):
        main_menu.click_social_media_button(i + 1)
        assert main_menu.social_media_button_n.is_enabled(), \
            f"Social media button {i} is not enabled."
        assert main_menu.social_media_button_n.is_displayed(), \
            f"Social media button {i} is not displayed."
        time.sleep(1)
        
        # It goes to the social media page close it and returns back 
        # to the Main Page 
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        driver.close()
        driver.switch_to.window(window_handles[0])
        
    # 9.Find and click Language Switcher button
    main_menu.language_switcher()
    assert main_menu.language_button.is_enabled()
    assert main_menu.language_button.is_displayed()
    time.sleep(3)
    # main_menu.main_logo()

    # 10.Find and click Log In button
    main_menu.log_in()
    assert main_menu.log_in_button.is_enabled()
    assert main_menu.log_in_button.is_displayed()
    main_menu.log_in_button.click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

    # 11.Find and click Cart button
    main_menu.cart()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    time.sleep(3)


# TO_DO-1 - Check in step # 7 that appropriate tooltip is shown and that
# correct phone number is shown, and that phone number was copied after click

# TO_DO-2 - Return back to the Main Page after opening social media pages - DONE
# TO_DO-3 - Check that Log In button redirects to the Log In page
# TO_DO-4 - Check that Cart button redirects to the Cart page
# TO_DO-5 - Check the Main Menu language switcher functionality
# TO_DO-6 - Check the "Кошик" button functionality

# TO_DO-7 - add the following steps for logging:
# # 4. Click on the main logo to return to the main page
#     logger.info(f"4.1. Click on the main logo to return to the main page.")
#     main_menu = MainMenu(driver)
#     main_menu.main_logo()
#     logger.info(f"4.2. The main logo is clicked.")
#     current_page_title = driver.title
#     logger.info(f"4.3. Ensure that page with the title "
#                 f"'{current_page_title}' is opened.")
#     expected_title = MAIN_PAGE_TITLE
#     assert current_page_title == expected_title,\
#     f"Expected title is '{expected_title}', but got '{current_page_title}'"
#     time.sleep(3)
#     logger.info(f"4.4. Expected title is '{MAIN_PAGE_TITLE}', "
#                 f"and got '{current_page_title}'\n{'=' * 200}")

