import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import DISCOUNTS_PAGE_HEADER, DISCOUNTS_PAGE_URL
from testing.pages.discounts_page import DiscountsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_discounts_page(browser: object):
    driver = browser
    discounts_page = DiscountsPage(driver)


    # PRECONDITIONS: The Discounts page is opened
    discounts_page.open_page(DISCOUNTS_PAGE_URL)
    discounts_page.check_if_page_is_loaded()
    logger.info(f"PRECONDITIONS: The Discounts page: {DISCOUNTS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{DISCOUNTS_PAGE_HEADER}' header is displayed.")
    discounts_page.find_the_h1_header()
    assert discounts_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert discounts_page.h1_header.text == DISCOUNTS_PAGE_HEADER, \
        f"H1 header text is '{discounts_page.h1_header.text}'," \
        f" expected '{DISCOUNTS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{discounts_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
