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
    
    for _ in range(4):
        # 3.Scroll page until the SHOW_MORE_BUTTON will be visible
        # using ActionChain
        category_page = CategoryPage(driver)
        category_page.show_more()
        print(1)
        assert category_page.show_more_button.is_displayed()
        assert category_page.show_more_button.is_enabled()

        # 3.1.Click SHOW_MORE_BUTTON 
        category_page.show_more()
        time.sleep(3)
        assert category_page.show_more_button.is_enabled()
        assert category_page.show_more_button.is_displayed()
        time.sleep(3)
