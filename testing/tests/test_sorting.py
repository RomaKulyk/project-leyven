from testing.pages.main_page import MainPage
import time
import random
from testing.lib.constants import MAIN_URL,\
                                  SORT1,\
                                  SORT2,\
                                  SORT3
                            

def test_main_page(browser: object):
    driver = browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(0.5)

     # 2.Find and click GO_TO_CATEGORY_2 button
    main_page.find_go_to_category(3)
    assert main_page.go_to_category_button.is_enabled(),\
        "GO_TO_CATEGORY_2 button is not enabled."
    assert main_page.go_to_category_button.is_displayed(),\
        "GO_TO_CATEGORY_2 button is not displayed."
    main_page.click_go_to_category(3)

    # 3.Find and click SORTING dropdown list
    # list of available options in dropdown
    sort_options = [SORT1, SORT2, SORT3]
    for options in sort_options:
        main_page.sort_item(options)
        main_page.dropdown_list.is_enabled()
        main_page.dropdown_list.is_displayed()
        # verify if certain options is enabled and displayed
        assert main_page.sort_menu_item.is_displayed()
        assert main_page.sort_menu_item.is_enabled()
        time.sleep(0.5)

    # 4.Find and click ascending option in Sorting dropdown
    main_page.sort_item(SORT1)
    time.sleep(0.5)

    # 5.Verify that product cards are in ascending order
    main_page.product_cards()
    step = random.randint(1, 5)

    product_card_prices = []
    for e in range(1, len(main_page.product_cards_n), step):
        time.sleep(0.5)
        main_page.product_card(e)
        time.sleep(3)

        product_card_prices.append(main_page.product_card_price())
        assert main_page.product_card_price() >= 0
        time.sleep(0.5)
        driver.back()
    print(product_card_prices)

    step = random.randint(1, 5)
    print(len(product_card_prices))
    for i in range(0, (len(product_card_prices) - 1), step):
        assert product_card_prices[i] <= product_card_prices[i + 1]

    # 6.Find and click descending option in Sorting dropdown
    main_page.sort_item(SORT2)
    time.sleep(0.5)

    # 7.Verify that product cards are in descending order
    main_page.product_cards()
    step = random.randint(1, 5)

    product_card_prices = []
    for e in range(1, len(main_page.product_cards_n), step):
        time.sleep(0.5)
        main_page.product_card(e)
        time.sleep(3)

        product_card_prices.append(main_page.product_card_price())
        assert main_page.product_card_price() >= 0
        time.sleep(0.5)
        driver.back()
    print(product_card_prices)

    step = random.randint(1, 5)
    print(len(product_card_prices))
    for i in range(0, (len(product_card_prices) - 1), step):
        assert product_card_prices[i] >= product_card_prices[i + 1]

