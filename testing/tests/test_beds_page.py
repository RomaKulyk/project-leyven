import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import BEDS_PAGE_HEADER, BEDS_PAGE_URL
from testing.pages.beds_page import BedsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
def test_beds_page(browser: object):
    driver = browser
    beds_page = BedsPage(driver)
    
    
    # PRECONDITIONS: The Beds page is opened
    beds_page.open_page(BEDS_PAGE_URL)
    logger.info(f"PRECONDITIONS: The main page: {BEDS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{BEDS_PAGE_HEADER}' header is displayed.")
    beds_page.find_the_h1_header()
    assert beds_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert beds_page.h1_header.text == BEDS_PAGE_HEADER, \
        f"H1 header text is '{beds_page.h1_header.text}'," \
        f" expected '{BEDS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{beds_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
