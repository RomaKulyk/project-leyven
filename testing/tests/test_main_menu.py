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

    # 8.Find and click Facebook button
    main_menu.facebook()
    assert main_menu.facebook_button.is_enabled()
    assert main_menu.facebook_button.is_displayed()
    time.sleep(3)

    # 9.Find and click Instagram button
    main_menu.instagram()
    assert main_menu.instagram_button.is_enabled()
    assert main_menu.instagram_button.is_displayed()
    time.sleep(3)

    # 10.Find and click Tiktok button
    main_menu.tiktok()
    assert main_menu.tiktok_button.is_enabled()
    assert main_menu.tiktok_button.is_displayed()
    time.sleep(3)

    # 11.Find and click Log In button
    main_menu.log_in()
    assert main_menu.log_in_button.is_enabled()
    assert main_menu.log_in_button.is_displayed()
    main_menu.log_in_button.click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

    # 12.Find and click Cart button
    main_menu.cart()
    assert main_menu.cart_button.is_enabled()
    assert main_menu.cart_button.is_displayed()
    time.sleep(3)


# TO_DO-1 - Check in step # 7 that appropriate tooltip is shown and that
# correct phone number is shown, and that phone number was copied after click

# TO_DO-2 - Return back to the Main Page after openin social medis pages