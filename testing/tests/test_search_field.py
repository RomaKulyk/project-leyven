import pytest
from testing.pages.main_page import *
from testing.pages.main_menu import *
from testing.lib.constants import *
import time

@pytest.mark.parametrize('user_input',[('Simparica'),('Sim'),
                         ('Сім'),('10024337'),(10022531)])
def test_main_menu(chrome_browser: object, user_input: str):
    driver = chrome_browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)
    
    main_menu = MainMenu(driver)
    # 2.Input some query into Search field
    main_menu.search(user_input)
    assert main_menu.search_field.is_enabled()
    assert main_menu.search_field.is_displayed()
    time.sleep(3)

    # 3.Click Cross Button
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
    time.sleep(3)