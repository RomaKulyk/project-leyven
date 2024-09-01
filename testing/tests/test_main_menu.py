import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.pages.main_menu import *
from testing.pages.catalog_dropdown import *
from testing.lib.constants import *
import time


def test_main_menu(chrome_browser: object):
    driver = chrome_browser
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
    main_menu.search('Simparica')
    assert main_menu.search_field.is_enabled()
    assert main_menu.search_field.is_displayed()
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
