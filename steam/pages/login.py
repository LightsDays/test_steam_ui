import allure
from selene import browser, have


class LoginPage:
    @staticmethod
    @allure.step('Кликаем на кнопку "login".')
    def click_on_login() -> None:
        browser.all('.global_action_link').element_by(have.text('sign in')).click()

    @staticmethod
    @allure.step('Проверяем, что отображается страница авторизации')
    def this_is_login_page() -> None:
        browser.element('button[type="submit"]').should(have.exact_text('Sign in'))

