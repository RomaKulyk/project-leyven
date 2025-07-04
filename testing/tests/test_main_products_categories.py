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

def test_main_products_categories(browser: object):
    """Test to ensure that the main product categories on the main page
    are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)

     # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    main_menu = MainMenu(driver)
    main_page.find_main_products_categories()
    
    for i in range(1, len(main_page.main_products_categories_list) + 1):
        # 2.1.Find the main product category
        main_page.find_main_products_categories()
        main_page.find_main_products_category(i)  
        assert main_page.main_product_category_n.is_enabled(), \
            f"Main page main product category link {i} is not enabled."
        assert main_page.main_product_category_n.is_displayed(), \
            f"Main page main product category link {i} is not displayed."
        
        # 2.2.Click the social media link
        time.sleep(3)
        link_text = main_page.main_products_categories_list[i - 1].text
        main_page.click_main_product_category(i)
        logger.info(
            f"Click the Main page main product category link '{link_text}'.")
        time.sleep(3)

        current_page_title = driver.title
        logger.info(f"Page with title '{current_page_title}' is opened.")
        expected_title = page_titles[i-1]
        logger.info(f"Expected title is '{expected_title}'," \
                     f"and got '{current_page_title}'\n{'=' * 200}")
        assert current_page_title == expected_title, \
        f"Expected title is '{expected_title}', but got '{current_page_title}'"
        main_menu.main_logo()
        
    # assert 1 == 0 # Uncomment to fail the test intentionally
# TO-DO_1 - Update login functionality in conftest.py to be able to add 
# timestamps to the log.