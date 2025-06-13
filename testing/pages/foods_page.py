from testing.pages.category_page import CategoryPage


class FoodsPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the FoodsPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver