from testing.pages.category_page import CategoryPage
from testing.lib.constants import DRY_FOOD_PAGE_TITLE


class DryFoodsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the DryFoodsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = DRY_FOOD_PAGE_TITLE