from testing.pages.main_page import *
from testing.pages.category_page import *
from testing.lib.constants import *
import time


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

    category_page = CategoryPage(driver) 
    # 3.Verify if menu bar persist on the page
    category_page.filters_menu()
    assert category_page.filters_menu_bar.is_enabled()
    assert category_page.filters_menu_bar.is_displayed()
    time.sleep(3)
    
    category_page.filters_list()
    # print(category_page.filters_list_item)
    print(len(category_page.filters_list_item))

    assert len(category_page.filters_list_item) != 0

    category_page.filter(1)
    assert category_page.filter_n.is_displayed()
    assert category_page.filter_n.is_enabled()
    assert False == True