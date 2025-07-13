from testing.pages.category_page import CategoryPage
from testing.lib.constants import BRANDS_PAGE_TITLE


class BrandsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the BrandsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = BRANDS_PAGE_TITLE