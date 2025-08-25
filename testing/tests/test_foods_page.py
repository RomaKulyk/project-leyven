import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import FOODS_PAGE_HEADER, FOODS_PAGE_URL
from testing.pages.foods_page import FoodsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_foods_page(browser: object):
    driver = browser
    foods_page = FoodsPage(driver)


    # PRECONDITIONS: The Foods page is opened
    foods_page.open_page(FOODS_PAGE_URL)
    foods_page.check_if_page_is_loaded()
    logger.info(f"PRECONDITIONS: The Foods page: {FOODS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{FOODS_PAGE_HEADER}' header is displayed.")
    foods_page.find_the_h1_header()
    assert foods_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert foods_page.h1_header.text == FOODS_PAGE_HEADER, \
        f"H1 header text is '{foods_page.h1_header.text}'," \
        f" expected '{FOODS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{foods_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
