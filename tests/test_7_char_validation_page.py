import pytest


class Test7CharsPage:
    """
       Test suite for validating input values on the 7-character validation page.
       Each test case provides an input value, the expected validation message,
       and a unique test ID for easier identification.
       """

    test_data = [
        ("abc123*", "Valid Value", "exactly_7_chars_all_allowed_types_no_uppercase"),
        ("abc$23*", "Invalid Value", "invalid_special_char"),
        ("abc12", "Invalid Value", "too_short"),
        ("abc1234z", "Invalid Value", "too_long"),
        ("", "Invalid Value", "empty_value"),
        ("A2bC4*d", "Valid Value", "exactly_7_chars_all_allowed_types_with_uppercase"),
        ("*******", "Valid Value", "exactly_7_chars_all_*"),
        ("abc123", "Invalid Value", "lower_boundary_value"),
        ("abc12345", "Invalid Value", "upper_boundary_value")
    ]

    @pytest.mark.parametrize(
        "input_value, expected_validity, test_id",
        test_data,
        ids=[td[2] for td in test_data]
    )

    def test_validate_input(self, env, input_value, expected_validity, test_id):
        """
                Test the character validation feature using various input strings.

                Args:
                    env: Pytest fixture providing the environment with initialized page objects.
                    input_value (str): The string to be input for validation.
                    expected_validity (str): The expected result message from the validation.
                    test_id (str): A unique identifier for the test case.
                """
        env.chars_validation_page.open_page()
        env.chars_validation_page.type_value_in_the_input_field(input_value)
        env.chars_validation_page.click_validate_btn()
        actual_message = env.chars_validation_page.check_validation_message()
        assert actual_message == expected_validity, (
        f"[{test_id}] Expected message: '{expected_validity}', got: '{actual_message}'"
    )


