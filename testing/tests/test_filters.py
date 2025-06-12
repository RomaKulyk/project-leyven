from testing.pages.main_page import MainPage
from testing.pages.category_page import CategoryPage
from testing.lib.constants import MAIN_URL, FILTER_ITEM
from selenium.webdriver.common.by import By
import time
import random


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)

    # 2.Find and click go_to_category_2 button
    main_page.go_to_category_2()
    assert main_page.go_to_category_2_button.is_enabled()
    assert main_page.go_to_category_2_button.is_displayed()
    main_page.go_to_category_2_button.click()
    time.sleep(3)



    category_page = CategoryPage(driver) 
    # 3.Verify if menu bar persist on the page
    category_page.filters_menu()
    assert category_page.filters_menu_bar.is_enabled()
    # assert category_page.filters_menu_bar.is_displayed()
    time.sleep(3)
       
    driver.find_element(By.XPATH, FILTER_ITEM)

    category_page.filters_list()
    print(category_page.filters_list_item)
    print(len(category_page.filters_list_item))
    assert len(category_page.filters_list_item) != 0
    
    # assert False == True