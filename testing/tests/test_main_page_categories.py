import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
import time
import logging


logger = logging.getLogger('leyven_tests_logger')

page_titles = ["Собаки | Лейвен",
              "Коти | Лейвен",
              "Сухий корм | Лейвен",
              "Сімпаріка | Інтернет-зоомагазин Лейвен",
              "Бренди | Лейвен - Інтернет-зоомагазин",
              "Лейвен Блог",
              "Будиночки, лежанки, м'які місця | Лейвен",
              "Акції | Інтернет-зоомагазин Лейвен",
              "Новинки | Інтернет-зоомагазин Лейвен"]

@pytest.mark.with_logging
def test_main_page_categories(browser: object):
    """Test to ensure that the product categories on the main page
    are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)
    
    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL} is opened.\n{'=' * 200}")
    main_page.product_categories()
    
    for i in range(1, len(main_page.product_categories_list) + 1):
        # 1. Find and click each Product's category link 
        main_page.product_category(i)
        assert main_page.product_category_n.is_enabled(),\
        f"Product category {page_titles[i - 1]} is not enabled."
        assert main_page.product_category_n.is_displayed(),\
        f"Product category {page_titles[i - 1]} is not displayed."
        logger.info(
            f"{i}.1. Click the '{page_titles[i - 1]}' product\'s category link.")    
        time.sleep(1)

        # 2. Ensure that the the page with the correct title is opened
        current_page_title = driver.title
        logger.info(f"{i}.2. Ensure that page with the title '{current_page_title}' is opened.")
        expected_title = page_titles[i-1]
        
        # 3. Check that the page title is correct
        assert current_page_title == expected_title, \
            f"Expected title is '{expected_title}', but got '{current_page_title}'"
        logger.info(f"{i}.3. Expected title is '{expected_title}', " \
                     f"and got '{current_page_title}'\n{'=' * 200}")
        main_menu.main_logo()
