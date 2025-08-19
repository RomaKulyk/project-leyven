import pytest
from testing.pages.category_page import CategoryPage
from testing.lib.constants import BLOG_PAGE_HEADER, BLOG_PAGE_URL
from testing.pages.blog_page import BlogPage
import logging


logger = logging.getLogger('leyven_tests_logger')   

@pytest.mark.with_logging
def test_blog_page(browser: object):
    driver = browser
    blog_page = BlogPage(driver)


    # PRECONDITIONS: The Blog page is opened
    blog_page.open_page(BLOG_PAGE_URL)
    logger.info(f"PRECONDITIONS: The Blog page: {BLOG_PAGE_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")
    
    # 1. Ensure that the H1 header is displayed
    logger.info(
        f"1.1. Ensure that the H1 '{BLOG_PAGE_HEADER}' header is displayed.")
    blog_page.find_the_h1_header()
    assert blog_page.h1_header.is_displayed(), "H1 header is not displayed"
    assert blog_page.h1_header.text == BLOG_PAGE_HEADER, \
        f"H1 header text is '{blog_page.h1_header.text}'," \
        f" expected '{BLOG_PAGE_HEADER}'."
    logger.info(
        f"1.2. The H1 '{blog_page.h1_header.text}' header is displayed.")
    logger.info(f"[PASSED]\n{'=' * 200}")
