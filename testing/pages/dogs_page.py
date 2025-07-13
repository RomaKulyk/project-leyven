from testing.pages.category_page import CategoryPage
from testing.lib.constants import DOGS_PAGE_TITLE


class DogsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the DogsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = DOGS_PAGE_TITLE
        