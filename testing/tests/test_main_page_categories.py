import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.pages.dogs_page import DogsPage
from testing.pages.cats_page import CatsPage
from testing.pages.foods_page import FoodsPage
from testing.pages.simparica_page import SimparicaPage
from testing.pages.brands_page import BrandsPage
from testing.pages.blog_page import BlogPage
from testing.pages.beds_page import BedsPage
from testing.pages.discounts_page import DiscountsPage
from testing.pages.new_arrivals_page import NewArrivalsPage
from testing.lib.constants import MAIN_URL
import time

page_titles =["Собаки | Лейвен",
              "Коти | Лейвен",
              "Сухий корм | Лейвен",
              "Сімпаріка | Інтернет-зоомагазин Лейвен",
              "Бренди | Лейвен - Інтернет-зоомагазин",
              "Лейвен Блог",
              "Будиночки, лежанки, м'які місця | Лейвен",
              "Акції | Інтернет-зоомагазин Лейвен",
              "Новинки | Інтернет-зоомагазин Лейвен"]
    
page_classes = [DogsPage,
                CatsPage,
                FoodsPage,
                SimparicaPage,
                BrandsPage,
                BlogPage,
                BedsPage,
                DiscountsPage,
                NewArrivalsPage]

def test_main_page_categories(browser: object):
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)
    

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    
    main_page.product_categories()
    # print(len(main_page.product_categories_list))
    # print(main_page.product_categories_list)
    assert len(main_page.product_categories_list) > 0, \
    "No product categories found on the main page."
    
    # 2.Ensure that each Product's category link is displayed, clickable,
    # and redirects to the correct URL
    for i in range(1, len(main_page.product_categories_list) + 1):
        main_page.product_category(i)
     
        print(f"{i}. Click the '{page_titles[i - 1]}' product\'s category link.")
        assert main_page.product_category_n.is_enabled(),\
        f"Product category {page_titles[i - 1]} is not enabled."
        assert main_page.product_category_n.is_displayed(),\
        f"Product category {page_titles[i - 1]} is not displayed."        
        print(f"The '{page_titles[i - 1]}' product\'s category link is enabled"
              f" and displayed.")
        
        time.sleep(1)
        current_page_title = driver.title
        print(f"Current page title is '{current_page_title}'")
        expected_title = page_titles[i-1]
        print(f"Expected title is '{expected_title}', and got '{current_page_title}'")
        assert current_page_title == expected_title, \
            f"Expected title is '{expected_title}', but got '{current_page_title}'"
        print('=' * 100)
        main_menu.main_logo()

    assert 1 == 0


# TO-DO_1 - Implement some login functionality to be able to log test execution
# order to the file.