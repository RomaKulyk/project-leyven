from testing.pages.main_page import *
from testing.lib.constants import *
import time
import random
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
    sort_options = [SORT1, SORT2, SORT3]
    for options in sort_options:
        main_page.sort_item(options)
        main_page.dropdown_list.is_enabled()
        main_page.dropdown_list.is_displayed()
        # verify if certain options is enabled and displayed
        assert main_page.sort_menu_item.is_displayed()
        assert main_page.sort_menu_item.is_enabled()
        time.sleep(3)
    
 