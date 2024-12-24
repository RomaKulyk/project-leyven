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

    # 2.Find and click GO_TO_CATEGORY_1 button
    main_page.go_to_category_1()
    assert main_page.go_to_category_1.is_enabled()
    assert main_page.go_to_category_1.is_displayed()
    main_page.go_to_category_1.click()
    time.sleep(3)



    category_page = CategoryPage(driver) 
    # 3.Verify if menu bar persist on the page
    category_page.filters_menu()
    assert category_page.filters_menu_bar.is_enabled()
    assert category_page.filters_menu_bar.is_displayed()
    time.sleep(3)
       
    driver.find_element(By.XPATH, FILTER_ITEM)

    # category_page.filters_list()
    # # print(category_page.filters_list_item)
    # print(len(category_page.filters_list_item))
    # assert len(category_page.filters_list_item) != 0
 
    # category_page.filter(2)
    # # category_page.filters_menu()
    # # category_page.filters_list()
    # category_page.filter(2)
    
    # category_page.filter(3)
    
    # category_page.filter(4)
    
    # category_page.filter(5)

    # step = random.randint(1,5)
    # print(step)

    # for e in range(1, len(category_page.filters_list_item), step):
    #     time.sleep(3)
    #     print(e)
    #     category_page.filter(e)
        
    #     assert category_page.filter_n.is_displayed()
    #     assert category_page.filter_n.is_enabled()
        
    # assert False == True