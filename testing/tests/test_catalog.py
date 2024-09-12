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
    time.sleep(3)

    main_menu = MainMenu(driver)
    # 2.Hover mouse over Catalog button
    main_menu.catalog()
    assert main_menu.catalog_button.is_enabled()
    assert main_menu.catalog_button.is_displayed()
    time.sleep(3)

    catalog_dropdown = CatalogDropdown(driver)
    # 3.Ensure that Catalog Dropdown container is displayed
    catalog_dropdown.catalog_dropdown()
    assert catalog_dropdown.catalog_dropdown_container.is_enabled()
    assert catalog_dropdown.catalog_dropdown_container.is_displayed()

    # 4.Ensure that Catalog Dropdown Item is displayed and clickable
    catalog_dropdown_items = [CATALOG_DROPDOWN_ITEM_1,
                              CATALOG_DROPDOWN_ITEM_2,
                              CATALOG_DROPDOWN_ITEM_3,
                              CATALOG_DROPDOWN_ITEM_4,
                              CATALOG_DROPDOWN_ITEM_5,
                              CATALOG_DROPDOWN_ITEM_6,
                              CATALOG_DROPDOWN_ITEM_7,
                              CATALOG_DROPDOWN_ITEM_8,
                              CATALOG_DROPDOWN_ITEM_9]
    
    for item in catalog_dropdown_items:
        catalog_dropdown.catalog_dropdown_items(item)
        assert catalog_dropdown.catalog_dropdown_container.is_enabled()
        assert catalog_dropdown.catalog_dropdown_container.is_displayed()
        time.sleep(3)

