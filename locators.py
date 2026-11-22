from selenium.webdriver.common.by import By


class HeaderLocators:
    SIGN_IN_OR_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')
    USER_NAME = (By.CSS_SELECTOR, ".profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    PROFILE_LINK = (By.CSS_SELECTOR, ".circleSmall")


class AuthLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")


class RegistrationLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    PASSWORD_CONFIRMATION_INPUT = (By.CSS_SELECTOR, 'input[name="submitPassword"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR_CONTAINER = (By.CSS_SELECTOR, "div[class*='input_inputError']:has(input[name='email'])")
    PASSWORD_ERROR_CONTAINER = (By.CSS_SELECTOR, "div[class*='input_inputError']:has(input[name='password'])")
    PASSWORD_CONFIRMATION_ERROR_CONTAINER = (By.CSS_SELECTOR, "div[class*='input_inputError']:has(input[name='submitPassword'])")
    ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")


class AdLocators:
    AUTH_REQUIRED_TITLE = (By.XPATH, ".//h1")
    TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_SELECT_ARROW = (By.CSS_SELECTOR, 'div[class^="dropDownMenu"]:has(input[name="category"]) button[class^="dropDownMenu_arrowDown"]')
    CATEGORY_OPTION = (By.CSS_SELECTOR, 'div[class^="dropDownMenu"]:has(input[name="category"]) button[class^="dropDownMenu_btn"]:first-child')
    CITY_SELECT_ARROW = (By.CSS_SELECTOR, 'div[class^="dropDownMenu"]:has(input[name="city"]) button[class^="dropDownMenu_arrowDown"]')
    CITY_OPTION = (By.CSS_SELECTOR, 'div[class^="dropDownMenu"]:has(input[name="city"]) button[class^="dropDownMenu_btn"]:first-child')
    CONDITION_RADIO_NEW = (By.XPATH, './/label[text()="Новый"]')
    CONDITION_RADIO_OLD = (By.XPATH, './/label[text()="Б/У"]')
    PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    MY_ADS_SECTION = (By.XPATH, ".//h1[text()='Мои объявления']")
    MY_NEWEST_AD = (By.CSS_SELECTOR, ".about h2:first-child")
