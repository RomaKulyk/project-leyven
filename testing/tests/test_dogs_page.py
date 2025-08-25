import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import DOGS_PAGE_HEADER, DOGS_PAGE_URL
from testing.pages.dogs_page import DogsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_dogs_page(browser: object):
    driver = browser
    dogs_page = DogsPage(driver)


    # PRECONDITIONS: The Dogs page is opened
    dogs_page.open_page(DOGS_PAGE_URL)
    dogs_page.check_if_page_is_loaded()
    logger.info(f"PRECONDITIONS: The Dogs page: {DOGS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{DOGS_PAGE_HEADER}' header is displayed.")
    dogs_page.find_the_h1_header()
    assert dogs_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert dogs_page.h1_header.text == DOGS_PAGE_HEADER, \
        f"H1 header text is '{dogs_page.h1_header.text}'," \
        f" expected '{DOGS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{dogs_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
