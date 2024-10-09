from testing.pages.main_page import *
from testing.lib.constants import *
import time
from selenium.webdriver.support.ui import Select


def test_main_page(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)
    
    # 2.Find and click SHOW_ALL button
    main_page.show_all()
    assert main_page.show_all_button.is_enabled()
    assert main_page.show_all_button.is_displayed()
    main_page.show_all_button.click()
    time.sleep(3)

    # 3.Find and click SORTING dropdown list    
    # list of available options in dropdown    
    sort_options = ['price_asc', 'price_desc', 'popular']
    for i in sort_options:
        main_page.sort_item_sel()
        time.sleep(2)
        assert main_page.dropdown_list_sel.is_displayed()
        main_page.dropdown_list_sel.click()
        time.sleep(2)
        # Create an object of the select class
        drop = Select(main_page.dropdown_list_sel)
        # Select by value
        drop.select_by_value(i)
        time.sleep(2)

