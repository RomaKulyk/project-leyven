from testing.pages.main_page import MainPage
from testing.pages.category_page import CategoryPage
from testing.lib.constants import MAIN_URL
import time


def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    # 2.Find and click GO_TO_CATEGORY_2 button
    main_page.go_to_category_2()
    assert main_page.go_to_category_2.is_enabled()
    assert main_page.go_to_category_2.is_displayed()
    main_page.go_to_category_2.click()
    time.sleep(1)
    
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
