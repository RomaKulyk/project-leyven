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

def test_main_page_categories(browser: object):
    """Test to ensure that the product categories on the main page
    are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    
    main_page.product_categories()
    assert len(main_page.product_categories_list) > 0, \
    "No product categories found on the main page."
    
    # 2.Ensure that each Product's category link is displayed, clickable,
    # and redirects to the correct URL
    for i in range(1, len(main_page.product_categories_list) + 1):
        main_page.product_category(i)
     
        logger.info(
            f"Click the '{page_titles[i - 1]}' product\'s category link.")
        assert main_page.product_category_n.is_enabled(),\
        f"Product category {page_titles[i - 1]} is not enabled."
        assert main_page.product_category_n.is_displayed(),\
        f"Product category {page_titles[i - 1]} is not displayed."        
        
        time.sleep(1)
        current_page_title = driver.title
        logger.info(f"Page with title '{current_page_title}' is opened.")
        expected_title = page_titles[i-1]
        logger.info(f"Expected title is '{expected_title}'," \
                     f"and got '{current_page_title}'\n{'=' * 200}")
        assert current_page_title == expected_title, \
            f"Expected title is '{expected_title}', but got '{current_page_title}'"
        main_menu.main_logo()

    # assert 1 == 0 # Uncomment to fail the test intentionally