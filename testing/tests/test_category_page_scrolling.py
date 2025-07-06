import pytest
from testing.pages.main_page import MainPage
from testing.pages.category_page import CategoryPage
from testing.lib.constants import MAIN_URL
import logging


logger = logging.getLogger('leyven_tests_logger')

@pytest.mark.with_logging
def test_main_page(browser: object):
    """Test to ensure that the category page scrolling works correctly."""
    driver = browser
    main_page = MainPage(driver)
    
    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL}"
                f" is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 1.Find and click GO_TO_CATEGORY_2 button
    main_page.find_go_to_category(3)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    main_page.click_go_to_category(3)
    
    for _ in range(2):
        # 2.Scroll page until the SHOW_MORE_BUTTON will be visible
        # using ActionChain
        category_page = CategoryPage(driver)
        category_page.scroll_to_show_more()
        print(f"Iteration {_} is completed")
        assert category_page.show_more_button.is_displayed()
        assert category_page.show_more_button.is_enabled()
        # 2.1.Click SHOW_MORE_BUTTON 
        category_page.show_more_button.click()

