🧪 7-Character Validator Test Automation Framework
This project is a test automation framework built with Selenium, Pytest, and Python, targeting the web application:

[Simple 7 Character Validator](https://testpages.eviltester.com/styled/apps/7charval/simple7charvalidation.html)

It verifies input validation logic for a form that accepts exactly 7 characters using various character combinations.

📁 Project Structure
<pre> <code>
├── conftest.py               # Global fixtures and environment setup
├── core/
│   └── pages/
│       └── charvalidationpage.py  # Page Object for the validation page
├── tests/
│   └── test_char_validation.py    # Parametrized test cases
├── screenshots/             # Screenshots saved on test failures
├── requirements.txt         # List of required dependencies
└── README.md                # You're here!</code> </pre>

🧰 Technologies Used
 - Python 3.9.6
 - Selenium WebDriver
 - Pytest
 - webdriver-manager
 - selenium-page-factory (for POM support)

▶️ How to Run the Tests
1. ✅ Install Dependencies

<pre> <code> pip install -r requirements.txt </code></pre>

2. 🧪 Run Tests

<pre> <code>pytest tests/</code></pre>

3. 🌐 Run in a Specific Browser

<pre> <code> pytest tests/ --browser=firefox </code></pre>

Supported browsers: chrome (default), firefox.

📸 Screenshots on Failure

On test failure, a screenshot is automatically saved in the screenshots/ directory with a timestamp and test ID.

🙋‍♀️ Author 

Created by a passionate QA who enjoys clean architecture, readable tests, and scalable frameworks.

