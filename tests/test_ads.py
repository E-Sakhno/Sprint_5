from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import Select, WebDriverWait

from locators import AdLocators, HeaderLocators


class TestAdCreation:
    def test_unauthorized_user_sees_authorization_dialog(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(conditions.element_to_be_clickable(HeaderLocators.POST_AD_BUTTON)).click()
        actual_title = wait.until(conditions.visibility_of_element_located(AdLocators.AUTH_REQUIRED_TITLE)).text
        assert actual_title == "Чтобы разместить объявление, авторизуйтесь"

    def test_authorized_user_can_create_ad(self, driver, logged_in_user):
        ad_title = "Автотестовое объявление"
        wait = WebDriverWait(driver, 15)
        wait.until(conditions.element_to_be_clickable(HeaderLocators.POST_AD_BUTTON)).click()
        wait.until(conditions.visibility_of_element_located(AdLocators.TITLE_INPUT)).send_keys(ad_title)
        driver.find_element(*AdLocators.DESCRIPTION_INPUT).send_keys("Описание товара для автотеста")
        driver.find_element(*AdLocators.PRICE_INPUT).send_keys("1000")
        driver.find_element(*AdLocators.CATEGORY_SELECT_ARROW).click()
        driver.find_element(*AdLocators.CATEGORY_OPTION).click()
        driver.find_element(*AdLocators.CITY_SELECT_ARROW).click()
        driver.find_element(*AdLocators.CITY_OPTION).click()
        driver.find_element(*AdLocators.CONDITION_RADIO_NEW).click()
        driver.find_element(*AdLocators.PUBLISH_BUTTON).click()
        wait.until(conditions.visibility_of_element_located(HeaderLocators.USER_NAME)) 
        wait.until(conditions.visibility_of_element_located(HeaderLocators.PROFILE_LINK)).click()
        # почему-то если кликнуть только один раз - падает по таймауту. Если продублировать строчку - тест проходит
        # пыталась увеличивать время в wait, подскроллить до шапки, ожидать кликабельность - всё равно падало
        wait.until(conditions.visibility_of_element_located(HeaderLocators.PROFILE_LINK)).click()
        wait.until(conditions.visibility_of_element_located(AdLocators.MY_ADS_SECTION))
        my_ads_section = driver.find_element(*AdLocators.MY_ADS_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", my_ads_section)
        actual_ad_title = wait.until(conditions.visibility_of_element_located(AdLocators.MY_NEWEST_AD)).text
        assert actual_ad_title == ad_title
