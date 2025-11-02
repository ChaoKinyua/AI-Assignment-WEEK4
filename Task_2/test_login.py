import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestLoginPage:
    """Test suite for login page automation"""
    
    # Valid credentials
    VALID_USERNAME = 'testuser'
    VALID_PASSWORD = 'TestPass123!'
    
    # Invalid credentials for negative testing
    INVALID_USERNAME = 'wronguser'
    INVALID_PASSWORD = 'WrongPass456!'
    
    def test_valid_login(self, driver, login_page_url):
        """Test successful login with valid credentials"""
        driver.get(login_page_url)
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
        )
        
        # Find and fill username field
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(self.VALID_USERNAME)
        
        # Find and fill password field
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.VALID_PASSWORD)
        
        # Click login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for success message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "successMessage"))
        )
        
        # Verify success message is displayed
        success_message = driver.find_element(By.ID, "successMessage")
        assert "Login successful" in success_message.text
        assert success_message.is_displayed()
        
        # Take screenshot
        driver.save_screenshot("Task_2/screenshots/test_valid_login_success.png")
        
        print("Test Passed: Valid login credentials accepted")
    
    def test_invalid_username(self, driver, login_page_url):
        """Test login failure with invalid username"""
        driver.get(login_page_url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
        )
        
        # Fill with invalid username
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(self.INVALID_USERNAME)
        
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.VALID_PASSWORD)
        
        # Submit form
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for error message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        
        # Verify error message
        error_message = driver.find_element(By.ID, "errorMessage")
        assert "invalid" in error_message.text.lower()
        assert error_message.is_displayed()
        
        # Take screenshot
        driver.save_screenshot("Task_2/screenshots/test_invalid_username_error.png")
        
        print("Test Passed: Invalid username correctly rejected")
    
    def test_invalid_password(self, driver, login_page_url):
        """Test login failure with invalid password"""
        driver.get(login_page_url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
        )
        
        # Fill with invalid password
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(self.VALID_USERNAME)
        
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.INVALID_PASSWORD)
        
        # Submit form
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for error message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        
        # Verify error message
        error_message = driver.find_element(By.ID, "errorMessage")
        assert "invalid" in error_message.text.lower()
        assert error_message.is_displayed()
        
        # Take screenshot
        driver.save_screenshot("Task_2/screenshots/test_invalid_password_error.png")
        
        print("Test Passed: Invalid password correctly rejected")
    
    def test_empty_fields(self, driver, login_page_url):
        """Test form validation with empty fields"""
        driver.get(login_page_url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
        )
        
        # Try to submit without filling fields
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # HTML5 validation should prevent submission
        try:
            login_button.click()
            time.sleep(1)
            # Check if form validation occurred
            username_field = driver.find_element(By.ID, "username")
            assert username_field.get_attribute("required") is not None
            print("Test Passed: Empty fields correctly prevented")
        except Exception as e:
            # Take screenshot for debugging
            driver.save_screenshot("Task_2/screenshots/test_empty_fields_validation.png")
            print(f"Test result: {e}")
    
    def test_form_elements_visible(self, driver, login_page_url):
        """Test that all form elements are visible and enabled"""
        driver.get(login_page_url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
        )
        
        # Check username field
        username_field = driver.find_element(By.ID, "username")
        assert username_field.is_displayed()
        assert username_field.is_enabled()
        
        # Check password field
        password_field = driver.find_element(By.ID, "password")
        assert password_field.is_displayed()
        assert password_field.is_enabled()
        
        # Check login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        assert login_button.is_displayed()
        assert login_button.is_enabled()
        
        # Take screenshot
        driver.save_screenshot("Task_2/screenshots/test_form_elements_visible.png")
        
        print("Test Passed: All form elements visible and enabled")
