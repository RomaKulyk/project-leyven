from testing.pages.category_page import CategoryPage


class BedsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the BedsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver