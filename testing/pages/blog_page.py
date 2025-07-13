from testing.pages.category_page import CategoryPage
from testing.lib.constants import BLOG_PAGE_TITLE


class BlogPage(CategoryPage):
    def __init__(self, webdriver) -> None:
        """
        This is a method to initialize instance of the BlogPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        self.title = BLOG_PAGE_TITLE