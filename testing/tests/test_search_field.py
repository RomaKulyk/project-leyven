import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.lib.constants import MAIN_URL
import time

@pytest.mark.parametrize('user_input',[('Сімпаріка'),('Sim'),
                         ('Сімп'),('10024337'),(10022531)])
# Search by ID number can't be verified right now since the number itself 
# is hidden right now on Product Card
# Due to this last two tests will be FAILING despite the expected results will
# be shown but they are impossible to verify

def test_main_menu(browser: object, user_input: str):
    driver = browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
        
    main_menu = MainMenu(driver)
    # 2.Click on search field to start search
    main_menu.search_out()
    assert main_menu.search_field_out.is_enabled()
    assert main_menu.search_field_out.is_displayed()
   
    # 3. Input some query into Search field
    main_menu.search_inn(user_input)
    main_menu.search_list()
    assert main_menu.search_field_inn.is_enabled()
    assert main_menu.search_field_inn.is_displayed()

    # 4. Verify that the shown results is equal to expected results
    # It's to verify that the list of founded items is not empty
    assert main_menu.search_found_list != []

    # It's to verify that every item in the list contaim user input in its name
    for item in range(1, len(main_menu.search_found_list) + 1):
        print(item)
        print(len(main_menu.search_found_list))
        print(main_menu.search_found_list)
        assert str(user_input) in main_menu.search_item(item)
    
    # 3.Click Cross Button
    main_menu.cross()
    assert main_menu.cross_button.is_enabled()
    assert main_menu.cross_button.is_displayed()
    main_menu.cross_button.click()
   
    # TO_DO_1 - change assertion in step # 3 for verification by ID number