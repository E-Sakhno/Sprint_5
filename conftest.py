import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import AuthLocators, HeaderLocators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    browser.get("https://qa-desk.education-services.ru/")
    # нейронка подсказала, что можно использовать yield вместо return, и закрывать браузер после yield
    yield browser

    browser.quit()


@pytest.fixture
def existing_user():
    # как поняла, удаляется на стенде каждый день и надо заново регистрироваться вручную
    email = "sakhno_40@yandex.ru"
    password = "qwerty"
    return {"email": email, "password": password}


@pytest.fixture
def logged_in_user(driver, existing_user):
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_IN_OR_REGISTER_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(existing_user["email"])
    driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
    driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
    wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME))
    return existing_user
