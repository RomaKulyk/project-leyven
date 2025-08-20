import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import NEW_ARRIVALS_PAGE_HEADER, NEW_ARRIVALS_PAGE_URL
from testing.pages.new_arrivals_page import NewArrivalsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
def test_new_arrivals_page(browser: object):
    driver = browser
    new_arrivals_page = NewArrivalsPage(driver)


    # PRECONDITIONS: The New Arrivals page is opened
    new_arrivals_page.open_page(NEW_ARRIVALS_PAGE_URL)
    logger.info(f"PRECONDITIONS: The New Arrivals page: {NEW_ARRIVALS_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{NEW_ARRIVALS_PAGE_HEADER}' header is displayed.")
    new_arrivals_page.find_the_h1_header()
    assert new_arrivals_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert new_arrivals_page.h1_header.text == NEW_ARRIVALS_PAGE_HEADER, \
        f"H1 header text is '{new_arrivals_page.h1_header.text}'," \
        f" expected '{NEW_ARRIVALS_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{new_arrivals_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
