import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
import time
import logging


logger = logging.getLogger('leyven_tests_logger')

page_titles = ["Годування домашніх тварин і птахів | Лейвен",
               "Ветеринарні засоби та препарати | Лейвен",
               "Товари для комфорту домашніх тварин | Лейвен",
               "Товари для прогулянок і подорожей з тваринами | Лейвен"]

@pytest.mark.with_logging
def test_main_products_categories(browser: object):
    """Test to ensure that the main product categories on the main page
    are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)

    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL}" \
                f" is opened.\n{'=' * 200}")
    main_page.find_main_products_categories()
    
    for i in range(1, len(main_page.main_products_categories_list) + 1):
        # 1. Find and click the main product category link
        main_page.find_main_products_categories()
        main_page.find_main_products_category(i)  
        assert main_page.main_product_category_n.is_enabled(), \
            f"Main page main product category link {i} is not enabled."
        assert main_page.main_product_category_n.is_displayed(), \
            f"Main page main product category link {i} is not displayed."
        time.sleep(1)
        link_text = main_page.main_products_categories_list[i - 1].text
        main_page.click_main_product_category(i)
        logger.info(f"{i}.1. Click the '{link_text}' Main page main product " \
                    f"category link.")
        time.sleep(1)

        # 2. Ensure that the page with the correct title is opened
        current_page_title = driver.title
        logger.info(f"{i}.2. Ensure that page with the title" \
                    f"'{current_page_title}' is opened.")
        expected_title = page_titles[i-1]

        # 3. Check that the page title is correct
        assert current_page_title == expected_title, \
        f"Expected title is '{expected_title}', but got '{current_page_title}'"
        logger.info(f"{i}.3. Expected title is '{expected_title}', " \
                    f" and got '{current_page_title}'\n{'=' * 200}")
        main_menu.main_logo()

# TO-DO_1 - Update login functionality in conftest.py to be able to add 
# timestamps to the log.