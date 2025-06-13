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


def test_main_page_categories(browser: object):
    driver = browser
    main_page = MainPage(driver)
    main_menu = MainMenu(driver)
    page_titles =["Собаки | Лейвен",
                  "Коти | Лейвен",
                  "Сухий корм | Лейвен",
                  "Сімпаріка | Інтернет-зоомагазин Лейвен",
                  "Бренди | Лейвен - Інтернет-зоомагазин",
                  "Лейвен Блог",
                  "Будиночки, лежанки, м'які місця | Лейвен",
                  "Акції | Інтернет-зоомагазин Лейвен",
                  "Новинки | Інтернет-зоомагазин Лейвен"]
    
    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    
    main_page.product_categories()
    # print(len(main_page.product_categories_list))
    # print(main_page.product_categories_list)
    assert len(main_page.product_categories_list) > 0, \
    "No product categories found on the main page."
    
    # 2.Ensure that each Product's category link is displayed and clickable
    for i in range(1, len(main_page.product_categories_list) + 1):
        time.sleep(1)
        main_page.product_category(i)
        print(f"{i}. Click the '{page_titles[i - 1]}' product\'s category link.")

        assert main_page.product_category_n.is_enabled(),\
        f"Product category {page_titles[i - 1]} is not enabled."
        assert main_page.product_category_n.is_displayed(),\
        f"Product category {page_titles[i - 1]} is not displayed."
        
        print(f"The '{page_titles[i - 1]}' product\'s category link is enabled"
              f" and displayed.")
        print('=' * 100)
        time.sleep(1)
        main_menu.main_logo()
        
    # 3.1.Ensure that "🐕 Собакам" Product's category link redirects 
    # to the correct URL
    dogs_page = DogsPage(driver)
    dogs_page.product_category(1)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Собаки | Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.2.Ensure that "🐈 Котам" Product's category link redirects 
    # to the correct URL
    cats_page = CatsPage(driver)
    cats_page.product_category(2)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Коти | Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.3.Ensure that "🍖 Корми" Product's category link redirects 
    # to the correct URL
    foods_page = FoodsPage(driver)
    foods_page.product_category(3)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Сухий корм | Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.4.Ensure that "💊 Сімпаріка" Product's category link redirects 
    # to the correct URL
    simparica_page = SimparicaPage(driver)
    simparica_page.product_category(4)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Сімпаріка | Інтернет-зоомагазин Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.5.Ensure that "🏭 Бренди" Product's category link redirects 
    # to the correct URL
    brands_page = BrandsPage(driver)
    brands_page.product_category(5)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Бренди | Лейвен - Інтернет-зоомагазин"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.6.Ensure that "📒 Блог" Product's category link redirects 
    # to the correct URL
    blog_page = BlogPage(driver)
    blog_page.product_category(6)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Лейвен Блог"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.7.Ensure that "🛏️ Лежаки" Product's category link redirects 
    # to the correct URL
    beds_page = BedsPage(driver)
    beds_page.product_category(7)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Будиночки, лежанки, м'які місця | Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.8.Ensure that "🔥 Акції" Product's category link redirects 
    # to the correct URL
    discounts_page = DiscountsPage(driver)
    discounts_page.product_category(8)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Акції | Інтернет-зоомагазин Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # 3.9.Ensure that "✨ Новинки" Product's category link redirects 
    # to the correct URL
    new_arrivals_page = NewArrivalsPage(driver)
    new_arrivals_page.product_category(9)
    time.sleep(1)
    page_title = driver.title
    expected_title = "Новинки | Інтернет-зоомагазин Лейвен"
    assert page_title == expected_title, \
        f"Expected '{expected_title}', but got '{page_title}'"
    main_menu.main_logo()

    # assert 1 == 0


    