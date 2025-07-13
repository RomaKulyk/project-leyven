from testing.pages.category_page import CategoryPage
from testing.lib.constants import FOODS_PAGE_TITLE


class FoodsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the FoodsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = FOODS_PAGE_TITLE