import time
import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import BEDS_PAGE_HEADER, BEDS_PAGE_URL
from testing.pages.beds_page import BedsPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
@pytest.mark.main_category
def test_beds_page(browser: object):
    driver = browser
    beds_page = BedsPage(driver)
    
    
    # PRECONDITIONS: The Beds page is opened
    beds_page.open_page(BEDS_PAGE_URL)
    beds_page.check_if_page_is_loaded()
    # Save screenshot of the page to the pages_screenshots directory
    driver.save_screenshot('pages_screenshots/beds_page_0.png')

    for i in range(5):  # Scroll down five times
        driver.execute_script(f"window.scrollBy(0, window.innerHeight);")
        time.sleep(1)  # Optional pause for visibility or loading
        driver.save_screenshot(f'pages_screenshots/beds_page_{i + 1}.png')

    logger.info(f"PRECONDITIONS: The Beds page: {BEDS_PAGE_URL} is opened.")

    # Press the browser's back button
    driver.back()
    logger.info("Press the browser's back button.")
    # Press the browser's forward button
    driver.forward()
    logger.info("Press the browser's forward button.")
    # Press browser's refresh button
    driver.refresh()
    logger.info("Page was reloaded using browser's refresh button.")
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
    logger.info(
        f"1.3. The H1 '{beds_page.style}' header style is correct.")
    logger.info(f"[PASSED]\n{'=' * 200}")

