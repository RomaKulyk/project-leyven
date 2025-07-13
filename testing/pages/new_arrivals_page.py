from testing.pages.category_page import CategoryPage
from testing.lib.constants import NEW_ARRIVALS_PAGE_TITLE


class NewArrivalsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the NewArrivalsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = NEW_ARRIVALS_PAGE_TITLE