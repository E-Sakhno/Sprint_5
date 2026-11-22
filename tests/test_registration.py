from datetime import datetime #для уникальных email'ов при каждом прогоне

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import AuthLocators, HeaderLocators, RegistrationLocators
from data import TestingData


WAIT_TIMEOUT = 10
USER_PASSWORD = "Password123!"
RED_COLOR = "rgb(255, 105, 114)"


class TestUserRegistration:
    def test_user_can_register(self, driver):
        email = f"autotest-{datetime.timestamp(datetime.now())}@example.com"
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*RegistrationLocators.PASSWORD_CONFIRMATION_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        actual_user_name = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        assert actual_user_name == "User."

    def test_registration_with_invalid_email_shows_error(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys("invalid_email")
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        email_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_CONTAINER)).value_of_css_property("border-color")
        password_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR_CONTAINER)).value_of_css_property("border-color")
        password_confirmation_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_CONFIRMATION_ERROR_CONTAINER)).value_of_css_property("border-color")
        #нейронка подсказала сравнить ожидаемый и фактический результат кортежами, а не отдельными assert'ами
        actual_validation_result = (
            wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE)).text,
            (
                email_border_color,
                password_border_color,
                password_confirmation_border_color,
            ),
        )
        expected_validation_result = (
            "Ошибка",
            (
                RED_COLOR,
                RED_COLOR,
                RED_COLOR,
            ),
        )
        assert actual_validation_result == expected_validation_result

    def test_registration_with_existing_email_shows_error(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(TestingData.user_email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(TestingData.user_password)
        driver.find_element(*RegistrationLocators.PASSWORD_CONFIRMATION_INPUT).send_keys(TestingData.user_password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        email_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_CONTAINER)).value_of_css_property("border-color")
        password_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR_CONTAINER)).value_of_css_property("border-color")
        password_confirmation_border_color = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_CONFIRMATION_ERROR_CONTAINER)).value_of_css_property("border-color")
        #нейронка подсказала сравнить ожидаемый и фактический результат кортежами, а не отдельными assert'ами
        actual_validation_result = (
            wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE)).text,
            (
                email_border_color,
                password_border_color,
                password_confirmation_border_color,
            ),
        )
        expected_validation_result = (
            "Ошибка",
            (
                RED_COLOR,
                RED_COLOR,
                RED_COLOR,
            ),
        )
        assert actual_validation_result == expected_validation_result
