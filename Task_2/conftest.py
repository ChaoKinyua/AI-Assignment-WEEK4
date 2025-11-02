import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="session")
def driver():
    """Setup and return WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Initialize Chrome driver with automatic driver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page_url():
    """Return the login page URL"""
    file_path = os.path.join(os.path.dirname(__file__), "login_page.html")
    return f"file:///{file_path.replace(os.sep, '/')}"
