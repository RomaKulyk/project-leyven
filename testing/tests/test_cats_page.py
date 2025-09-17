import time
import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import CATS_PAGE_HEADER, CATS_PAGE_URL, SCREEN
from testing.pages.cats_page import CatsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_cats_page(browser: object):
    driver = browser
    cats_page = CatsPage(driver)


    # PRECONDITIONS: The Cats page is opened
    cats_page.open_page(CATS_PAGE_URL)
    cats_page.check_if_page_is_loaded()
    cats_page.scroll_to_bottom()
    logger.info(f"{SCREEN}")
    logger.info(f"PRECONDITIONS: The Cats page: {CATS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{CATS_PAGE_HEADER}' header is displayed.")
    cats_page.find_the_h1_header()
    assert cats_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert cats_page.h1_header.text == CATS_PAGE_HEADER, \
        f"H1 header text is '{cats_page.h1_header.text}'," \
        f" expected '{CATS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{cats_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
