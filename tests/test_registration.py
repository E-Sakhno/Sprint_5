from datetime import datetime #для уникальных email'ов при каждом прогоне

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import AuthLocators, HeaderLocators, RegistrationLocators


WAIT_TIMEOUT = 10
USER_PASSWORD = "Password123!"


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
        actual_user_name = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        assert actual_user_name == "User."

    def test_registration_with_invalid_email_shows_error(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys("invalid_email")
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        actual_error = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE)).text
        assert actual_error == "Ошибка"

    def test_registration_with_existing_email_shows_error(self, driver, existing_user):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(existing_user["email"])
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        driver.find_element(*RegistrationLocators.PASSWORD_CONFIRMATION_INPUT).send_keys(existing_user["password"])
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        actual_error = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE)).text
        assert actual_error == "Ошибка"
