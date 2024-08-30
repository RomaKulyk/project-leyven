import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.pages.main_menu import *
from testing.pages.catalog_dropdown import *
from testing.lib.constants import *
import time

def test_main_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    # 2.Find and click BUY_PRODUDCTS
    main_page.buy_products()
    assert main_page.buy_products_button.is_enabled()
    # assert main_page.buy_products_button.is_displayed()
    time.sleep(1)
    
    # 3.Find and click SHOW_ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    time.sleep(1)
    
    main_menu = MainMenu(driver)
    # 4.Find and click MAIN_LOGO button
    main_menu.main_logo()
    assert main_menu.main_logo_button.is_enabled()
    assert main_menu.main_logo_button.is_displayed()

    # 5.Hover mouse over Catalog button
    main_menu.catalog()
    assert main_menu.catalog_button.is_enabled()
    assert main_menu.catalog_button.is_displayed()
    time.sleep(1)

    catalog_dropdown = CatalogDropdown(driver)
    # 6.Ensure that Catalog Dropdown container is displayed
    catalog_dropdown.catalog_dropdown()
    assert catalog_dropdown.catalog_dropdown_container.is_enabled()
    assert catalog_dropdown.catalog_dropdown_container.is_displayed()
    
    # 7.Find and click MAIN_LOGO button
    main_menu.main_logo()
    time.sleep(1)

    # 8.Input some query into Search field
    main_menu.search('Simparica')
    assert main_menu.search_field.is_enabled()
    assert main_menu.search_field.is_displayed()
    
    
    time.sleep(3)
   
    # 9.Click Cross Button
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
    time.sleep(3)

    # 10.Hover mouse over Phone button
    main_menu.phone()
    assert main_menu.phone_button.is_enabled()
    assert main_menu.phone_button.is_displayed()
    time.sleep(3)
