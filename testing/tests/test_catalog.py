import pytest
from testing.pages.main_page import MainPage
from testing.pages.hm_form import HelpMeForm
from testing.pages.main_menu import MainMenu
from testing.pages.catalog_dropdown import CatalogDropdown
from testing.lib.constants import MAIN_URL, \
                                  AQUA_PAGE_TITLE, \
                                  VET_PAGE_TITILE, \
                                  FEED_PAGE_TITLE, \
                                  RODEN_PAGE_TITLE, \
                                  OUTLET_PAGE_TITLE, \
                                  DIFF_PAGE_TITLE, \
                                  CARE_PAGE_TITLE, \
                                  COMFORT_PAGE_TITLE, \
                                  TRAVEL_PAGE_TITLE                                                         
                                  
                                  
import logging
import time

logger = logging.getLogger('leyven_tests_logger')

page_titles = [AQUA_PAGE_TITLE,
               VET_PAGE_TITILE,
               FEED_PAGE_TITLE,
               RODEN_PAGE_TITLE,
               OUTLET_PAGE_TITLE,
               DIFF_PAGE_TITLE,
               CARE_PAGE_TITLE,
               COMFORT_PAGE_TITLE,
               TRAVEL_PAGE_TITLE]

@pytest.mark.with_logging
def test_main_menu(browser: object):
    """Test to ensure that catalog links are displayed and clickable."""
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)

    # PRECONDITIONS: The main page is opened
    main_page.open_page(MAIN_URL)
    logger.info(f"PRECONDITIONS: The main page: {MAIN_URL} is opened.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    # 1. Ensure that the 'Каталог' button is displayed and enabled.
    logger.info(f"1.1. Ensure that the 'Каталог' button is displayed "
                f"and enabled.")
    main_menu.catalog()
    assert main_menu.catalog_button.is_enabled(),\
            f"Main page 'Каталог' button is not enabled."
    assert main_menu.catalog_button.is_displayed(),\
            f"Main page 'Каталог' button is not displayed."
    logger.info(f"1.2. The 'Каталог' button is displayed "
                f"and enabled.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    catalog_dropdown = CatalogDropdown(driver)
    # 2.Ensure that Catalog Dropdown container is displayed
    logger.info(f"2.1. Ensure that the 'Каталог' dropdown container"
                f" is displayed and enabled.")
    
    catalog_dropdown.catalog_dropdown()
    assert catalog_dropdown.catalog_dropdown_container.is_enabled(),\
            f"Main page 'Каталог' dropdown container is not enabled."
    assert catalog_dropdown.catalog_dropdown_container.is_displayed(),\
            f"Main page 'Каталог' dropdown container is not displayed."
    
    logger.info(f"2.2. The 'Каталог' dropdown container is displayed "
                f"and enabled.")
    logger.info(f"[PASSED]\n{'=' * 200}")

    catalog_dropdown.catalog_dropdown_ul()
    for i in range(len(catalog_dropdown.catalog_dropdown_elements)):
            # 3.1-2. Find and click Catalog Dropdown link
            link_text = catalog_dropdown.catalog_dropdown_elements[i].text
            logger.info(f"3.{i+1}.1. Click the '{link_text}' Main page catalog "
                    f"dropdown link.")
            
            catalog_dropdown.catalog_dropdown_elements[i].click()
            assert catalog_dropdown.catalog_dropdown_elements[i].is_enabled(),\
            f"Main page catalog dropdown link {i} is not enabled."
            assert catalog_dropdown.catalog_dropdown_elements[i].is_displayed(),\
            f"Main page catalog dropdown link {i} is not displayed."

            logger.info(f"3.{i+1}.2. The '{link_text}' Main page catalog "
                    f"dropdown link is clicked.")

            # 3.3-4. Ensure that the page with the correct title is opened
            current_page_title = driver.title

            logger.info(f"3.{i+1}.3. Ensure that page with the title "
                        f"'{current_page_title}' is opened.")
            expected_title = page_titles[i]
            assert current_page_title == expected_title,\
            f"Expected title is '{expected_title}', but got '{current_page_title}'"

            logger.info(f"3.{i+1}.4. Expected title is '{expected_title}', "
                        f" and got '{current_page_title}'")
            logger.info(f"[PASSED]\n{'=' * 200}")
