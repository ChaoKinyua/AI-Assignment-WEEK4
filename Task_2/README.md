# Task 2: Automated Testing with Selenium

## Overview
This project demonstrates automated testing of a login page using Selenium WebDriver with Python and pytest framework.

## Project Structure
```
Task_2/
├── login_page.html          # Sample login page for testing
├── test_login.py            # Test cases for login functionality
├── conftest.py              # Pytest configuration
├── requirements.txt         # Python dependencies
├── run_tests.py            # Test runner script
├── screenshots/            # Test execution screenshots
├── test_report.html        # HTML test report
└── README.md               # This file
```

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r Task_2/requirements.txt
```

### 2. Install ChromeDriver
The tests use Chrome WebDriver. You have two options:

**Option A: Automatic (Recommended)**
```bash
pip install webdriver-manager
```
Then update `conftest.py` to use webdriver-manager.

**Option B: Manual**
- Download ChromeDriver from https://chromedriver.chromium.org/
- Ensure it's in your system PATH

### 3. Run Tests
```bash
python Task_2/run_tests.py
```

Or run pytest directly:
```bash
pytest Task_2/test_login.py -v --html=Task_2/test_report.html --self-contained-html
```

## Test Cases

### 1. Valid Login ✓
- **Purpose**: Verify successful login with correct credentials
- **Steps**: Enter valid username and password
- **Expected**: Success message displayed
- **Screenshot**: `test_valid_login_success.png`

### 2. Invalid Username ✗
- **Purpose**: Test rejection of incorrect username
- **Steps**: Enter invalid username with valid password
- **Expected**: Error message displayed
- **Screenshot**: `test_invalid_username_error.png`

### 3. Invalid Password ✗
- **Purpose**: Test rejection of incorrect password
- **Steps**: Enter valid username with invalid password
- **Expected**: Error message displayed
- **Screenshot**: `test_invalid_password_error.png`

### 4. Empty Fields Validation
- **Purpose**: Verify HTML5 form validation
- **Steps**: Attempt submit without entering credentials
- **Expected**: Browser validation prevents submission

### 5. Form Elements Visibility
- **Purpose**: Ensure all UI elements are visible and enabled
- **Steps**: Check username, password fields and login button
- **Expected**: All elements displayed and enabled
- **Screenshot**: `test_form_elements_visible.png`

## Valid Test Credentials
- Username: `testuser`
- Password: `TestPass123!`

## Test Results
After running tests, you'll find:
- **HTML Report**: `Task_2/test_report.html` - Comprehensive test results
- **Screenshots**: `Task_2/screenshots/` - Visual proof of test execution
- **Console Output**: Detailed pass/fail status for each test

## Success Metrics
- ✅ All 5 tests should pass
- ✅ 100% success rate for positive and negative test cases
- ✅ Multiple screenshots captured as evidence
- ✅ Detailed HTML report generated

## AI-Enhanced Testing Benefits

### Automated Coverage vs Manual Testing

**Speed**: AI-driven automation executes 5 test cases in seconds vs. 5-10 minutes manually.

**Consistency**: Eliminates human error. Every test run executes identical steps with precise timing, ensuring reproducible results across multiple runs.

**Scalability**: Easily expandable to 50+ test cases with minimal effort. Parallel execution across browsers/devices accelerates testing cycles exponentially.

**Coverage**: Automated testing can execute edge cases (special characters, boundary values, timing issues) that are often skipped in manual testing due to time constraints.

**Documentation**: Automatic screenshot capture and HTML reports provide audit trails impossible with manual testing, ensuring regulatory compliance and easy debugging.

**Continuous Integration**: Integrates seamlessly into CI/CD pipelines, enabling 24/7 automated regression testing without human intervention.

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **pytest**: Test framework
- **Python**: Programming language
- **HTML/CSS/JavaScript**: Sample login page
- **ChromeDriver**: Chrome browser control

## Notes
- Ensure Chrome browser is installed
- Tests run against local HTML file (no internet required)
- All screenshots are saved automatically during test execution
