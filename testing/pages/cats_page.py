from testing.pages.category_page import CategoryPage
from testing.lib.constants import CATS_PAGE_TITLE


class CatsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the CatsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = CATS_PAGE_TITLE