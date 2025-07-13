from testing.pages.category_page import CategoryPage
from testing.lib.constants import SIMPARICA_PAGE_TITLE


class SimparicaPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the SimparicaPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = SIMPARICA_PAGE_TITLE