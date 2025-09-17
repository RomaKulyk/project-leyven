import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import SIMPARICA_PAGE_HEADER,\
                                  SIMPARICA_PAGE_URL,\
                                  SCREEN
from testing.pages.simparica_page import SimparicaPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_simparica_page(browser: object):
    driver = browser
    simparica_page = SimparicaPage(driver)


    # PRECONDITIONS: The Simparica page is opened
    simparica_page.open_page(SIMPARICA_PAGE_URL)
    simparica_page.check_if_page_is_loaded()
    simparica_page.scroll_to_bottom()
    logger.info(f"{SCREEN}")
    logger.info(
        f"PRECONDITIONS: The Simparica page: {SIMPARICA_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{SIMPARICA_PAGE_HEADER}' header is displayed.")
    simparica_page.find_the_h1_header()
    assert simparica_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert simparica_page.h1_header.text == SIMPARICA_PAGE_HEADER, \
        f"H1 header text is '{simparica_page.h1_header.text}'," \
        f" expected '{SIMPARICA_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{simparica_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
