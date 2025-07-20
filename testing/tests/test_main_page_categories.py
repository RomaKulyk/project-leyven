import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
from testing.lib.constants import DOGS_PAGE_TITLE, \
                                  BEDS_PAGE_TITLE, \
                                  BLOG_PAGE_TITLE, \
                                  BRANDS_PAGE_TITLE, \
                                  CATS_PAGE_TITLE, \
                                  DISCOUNTS_PAGE_TITLE, \
                                  FOODS_PAGE_TITLE, \
                                  NEW_ARRIVALS_PAGE_TITLE, \
                                  SIMPARICA_PAGE_TITLE
import time
import logging


logger = logging.getLogger('leyven_tests_logger')

page_titles = [DOGS_PAGE_TITLE,
               CATS_PAGE_TITLE,
               FOODS_PAGE_TITLE,
               SIMPARICA_PAGE_TITLE,
               BRANDS_PAGE_TITLE,
               BLOG_PAGE_TITLE,
               BEDS_PAGE_TITLE,
               DISCOUNTS_PAGE_TITLE,
               NEW_ARRIVALS_PAGE_TITLE]


@pytest.mark.with_logging
def test_main_page_categories(browser: object):
    """Test to ensure that the product categories on the main page
    are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)

    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: "
                f"{MAIN_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    main_page.find_product_categories()

    for i in range(1, len(main_page.product_categories_list) + 1):
        # 1.1-2. Find and click each Product's category link
        main_page.find_product_categories()
        main_page.find_product_category(i)

        assert main_page.product_category_n.is_enabled(), \
            f"Product category {page_titles[i - 1]} is not enabled."
        assert main_page.product_category_n.is_displayed(), \
            f"Product category {page_titles[i - 1]} is not displayed."
        time.sleep(1)

        link_text = main_page.product_categories_list[i - 1].text
        logger.info(f"{i}.1. Click the '{link_text}' product category link.")
        main_page.click_product_category(i)
        time.sleep(1)
        logger.info(f"{i}.2. The '{link_text}' product\'s category link" 
                    f"is clicked.")
        
        # 1.3-4. Ensure that the the page with the correct title is opened
        current_page_title = driver.title
        logger.info(f"{i}.3. Ensure that page with the title"
                    f" '{current_page_title}' is opened.")
        expected_title = page_titles[i-1]
        assert current_page_title == expected_title, \
            f"Expected title is '{expected_title}', but got "\
            f"'{current_page_title}'"
        logger.info(f"{i}.4. Expected title is '{expected_title}', "
                    f"and got '{current_page_title}'")
        logger.info(f"[PASSED]\n{'=' * 200}")
        
        # 2. Click the Main Logo button to return to the main page
        main_menu.click_main_logo()
        
