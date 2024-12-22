import pytest
from testing.pages.main_page import *
from testing.pages.hm_form import *
from testing.lib.constants import *
import time

def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    # 2.Find and click HELP_ME button
    main_page.help_me()
    assert main_page.help_me_button.is_enabled()
    assert main_page.help_me_button.is_displayed()
    time.sleep(1)

    # 3.Ensure that Help Me Form is displayed
    main_page.hm_form()
    assert main_page.help_me_form.is_enabled()
    assert main_page.help_me_form.is_displayed()
    time.sleep(1)
    
    hm_form = HelpMeForm(driver)
    # 4.Fill in the Help Me Form
    hm_form.enter_username("R2D2")
    hm_form.enter_phone("095-777-77-77")
    hm_form.enter_your_question(
        "Why I have to log in if there is not any functionality for that?")
    time.sleep(5)
