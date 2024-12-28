import pytest
from testing.pages.main_page import *
from testing.pages.main_menu import *
from testing.lib.constants import *
import time

@pytest.mark.parametrize('user_input',[('Simparica'),('Sim'),
                         ('Сім'),('10024337'),(10022531)])
def test_main_menu(browser: object, user_input: str):
    driver = browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)
    
    main_menu = MainMenu(driver)
    # 2.Click on search field to start search
    main_menu.search_out()
    assert main_menu.search_field_out.is_enabled()
    assert main_menu.search_field_out.is_displayed()
    time.sleep(3)

    # 3. Input some query into Search field
    main_menu.search_inn(user_input)
    assert main_menu.search_field_inn.is_enabled()
    assert main_menu.search_field_inn.is_displayed()
    time.sleep(3)

    # 3.Click Cross Button
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
    time.sleep(3)

    # TO_DO_1 - change assertion in step # 3 for more appropriate ones