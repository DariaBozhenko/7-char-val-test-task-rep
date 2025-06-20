from seleniumpagefactory.Pagefactory import PageFactory

# Tuple used by the env fixture to dynamically discover and load this page class
MODULE_CLASSES = ('CharsValidationPage', )

class CharsValidationPage(PageFactory):
    """
    Page Object Model for the 7-character validation web page.
    Encapsulates element locators and user interactions on the page.
    """
    def __init__(self, driver):
        """
        Initializes the CharsValidationPage object with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance controlling the browser.
        """
        self.driver = driver

    # Locator definitions for elements on the page
    locators = {
        "page_header": ('XPATH', '//h1[contains(text(), "Simple 7 Char Validator")]'),
        "input_field": ('NAME', 'characters'),
        "validation_message": ('NAME', 'validation_message'),
        "check_input_btn": ('NAME', 'validate'),

    }


    def open_page(self):
        """
        Navigates to the 7-character validation web page and verifies it has loaded.
        """
        self.driver.get("https://testpages.eviltester.com/styled/apps/7charval/simple7charvalidation.html")
        assert self.page_header.is_displayed(), "Page header is not displayed. Page might have failed to load."

    def type_value_in_the_input_field(self, input_value):
        """
        Clears and types the provided input string into the character input field.

        Args:
            input_value (str): The string to input into the field.
        """
        self.input_field.clear()
        self.input_field.send_keys(input_value)

    def click_validate_btn(self):
        """
        Clicks the validate button to trigger validation of the input.
        """
        self.check_input_btn.click()

    def get_validation_message(self):
        """
        Retrieves the validation result message from the page.

        Returns:
            str: The validation message displayed by the page.
        """
        return self.driver.execute_script(
            "return arguments[0].value;",
            self.validation_message
        )