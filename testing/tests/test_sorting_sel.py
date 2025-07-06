from testing.pages.main_page import MainPage
import time
from selenium.webdriver.support.ui import Select
from testing.lib.constants import MAIN_URL


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(3)
    
    # 2.Find and click GO_TO_CATEGORY_2 button
    main_page.find_go_to_category(3)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    main_page.click_go_to_category(3)

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

