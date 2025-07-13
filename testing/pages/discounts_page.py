from testing.pages.category_page import CategoryPage
from testing.lib.constants import DISCOUNTS_PAGE_TITLE


class DiscountsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the DiscountsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = DISCOUNTS_PAGE_TITLE