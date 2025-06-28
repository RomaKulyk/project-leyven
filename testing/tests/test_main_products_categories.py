import pytest
from testing.pages.main_page import MainPage
from testing.lib.constants import MAIN_URL
import time


page_titles =["Годування домашніх тварин і птахів | Лейвен",
              "Ветеринарні засоби та препарати | Лейвен",
              "Товари для комфорту домашніх тварин | Лейвен",
              "Товари для прогулянок і подорожей з тваринами | Лейвен",
              ]
def test_main_products_categories(browser: object):
    driver = browser
    main_page = MainPage(driver)

     # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    main_page.find_main_products_categories()
    
    for i in range(1, len(main_page.main_products_categories_list) + 1):
        # 2.1.Find the main product category
        main_page.find_main_products_category(i)  
        print("i =", i)
        assert main_page.main_product_category_n.is_enabled(), \
            f"Main page main product category link {i} is not enabled."
        assert main_page.main_product_category_n.is_displayed(), \
            f"Main page main product category link {i} is not displayed."
        
        # 2.2.Click the social media link
        time.sleep(3)
        # link_text = main_page.main_products_categories[i - 1].text
        # link_text = main_page.main_products_categories[i + 1].text
        # link_text = main_page.main_products_categories[i].text
        main_page.click_main_product_category(i)
        print("i =", i)
        print(f"Main page main product category link '{i}' is  clicked.")
        # print(f"Main page main product category link '{link_text}' is  clicked.")
        time.sleep(1)
        driver.back()
    # assert 1 == 0