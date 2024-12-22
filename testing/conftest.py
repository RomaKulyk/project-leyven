import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def chrome_browser():
    
    # Initialize the ChromeDriver instance
    driver = webdriver.Chrome()

    # Make its calls wait up to 10 seconds for elements to appear
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Yield the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()