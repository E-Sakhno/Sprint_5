from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import AuthLocators, HeaderLocators
from data import UserData, Titles


class TestUserLogin:
    def test_user_can_log_in(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(UserData.user_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(UserData.user_password)
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        actual_user_name = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        assert actual_user_name == Titles.defaul_user_name


class TestUserLogout:
    def test_user_can_log_out(self, driver, logged_in_user):
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()
        wait.until(expected_conditions.invisibility_of_element_located(HeaderLocators.USER_AVATAR))
        wait.until(expected_conditions.invisibility_of_element_located(HeaderLocators.USER_NAME))
        actual_button_text = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).text
        assert actual_button_text == Titles.login_button_text
