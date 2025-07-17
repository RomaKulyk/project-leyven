import pytest
from testing.pages.main_page import MainPage
from testing.pages.category_page import CategoryPage
from testing.lib.constants import MAIN_URL, DRY_FOOD_PAGE_TITLE
import logging
import time


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

    
    # 1. Ensure that the 'GO_TO_CATEGORY_2' button is displayed and enabled.
    logger.info(f"1.1. Ensure that the 'GO_TO_CATEGORY_2' button is displayed "
                f"and enabled.")
    
    main_page.find_go_to_category(3)

    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    
    logger.info(f"1.2. The 'GO_TO_CATEGORY_2' button is displayed "
                f"and enabled.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    

    # 2.1-2 Find and click the 'GO_TO_CATEGORY_2' button to navigate to
    # the category page.
    logger.info(f"2.1. Click the 'GO_TO_CATEGORY_2' button. "
                f"to navigate to the category page.")
    
    main_page.click_go_to_category(3)

    logger.info(f"2.2. The 'GO_TO_CATEGORY_2' button is clicked.")
    time.sleep(3)

    
    # 2.3-4. Ensure that the page with the correct title is opened
    current_page_title = driver.title

    logger.info(f"2.3. Ensure that page with the title "
                f"'{current_page_title}' is opened.")
    expected_title = DRY_FOOD_PAGE_TITLE
    assert current_page_title == expected_title,\
    f"Expected title is '{expected_title}', but got '{current_page_title}'"

    logger.info(f"2.4. Expected title is '{expected_title}', "
                f" and got '{current_page_title}'")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 3. Scroll page until the SHOW_MORE_BUTTON will be visible
    # using ActionChain
    logger.info(f"3.1. Scroll the page until the 'SHOW_MORE_BUTTON' "
                f"will be visible.")
    for _ in range(2):
        
        category_page = CategoryPage(driver)
        category_page.scroll_to_show_more()
        
        logger.info(f"Iteration {_} is completed")

    logger.info(f"3.2. The page is scrolled until the "
                    f"'SHOW_MORE_BUTTON' is visible.")
    logger.info(f"[PASSED]\n{'=' * 200}")


    # 4.1-2 Find and click the 'Показати більше' button.
    logger.info(f"4.1. Click the 'Показати більше' button.")
    
    category_page.click_show_more()
    assert category_page.show_more_button.is_displayed(), \
    f"'Показати більше' button is not displayed."
    assert category_page.show_more_button.is_enabled(), \
    f"'Показати більше' button is not enabled."

    logger.info(f"4.2. The 'Показати більше' button is clicked ")

    # 4.3-4.Ensure that the page with the correct title is opened
    current_page_title = driver.title

    logger.info(f"4.3. Ensure that page with the title "
                f"'{current_page_title}' is opened.")
    expected_title = DRY_FOOD_PAGE_TITLE
    assert current_page_title == expected_title,\
    f"Expected title is '{expected_title}', but got '{current_page_title}'"

    logger.info(f"4.4. Expected title is '{expected_title}', "
                f" and got '{current_page_title}'")
    logger.info(f"[PASSED]\n{'=' * 200}")

