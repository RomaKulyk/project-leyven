import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import BRANDS_PAGE_HEADER, BRANDS_PAGE_URL, SCREEN
from testing.pages.brands_page import BrandsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_brands_page(browser: object):
    driver = browser
    brands_page = BrandsPage(driver)


    # PRECONDITIONS: The Brands page is opened
    brands_page.open_page(BRANDS_PAGE_URL)
    brands_page.check_if_page_is_loaded()
    brands_page.scroll_to_bottom()
    logger.info(f"{SCREEN}")
    logger.info(f"PRECONDITIONS: The Brands page: {BRANDS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{BRANDS_PAGE_HEADER}' header is displayed.")
    brands_page.find_the_h1_header()
    assert brands_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert brands_page.h1_header.text == BRANDS_PAGE_HEADER, \
        f"H1 header text is '{brands_page.h1_header.text}'," \
        f" expected '{BRANDS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{brands_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
