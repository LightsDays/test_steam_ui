import allure
from selene import browser, have


class MainPage:
    @staticmethod
    def open_main_page() -> None:
         with allure.step('Открываем главную страницу "Steam"'):
            browser.open('/')

    @staticmethod
    def switch_navigation_tab(tab_name: str) -> None:
        with allure.step(f'Переключаемся на вкладку "{tab_name}"'):
            browser.all('.content .supernav').element_by(have.text(tab_name)).click()

    @staticmethod
    def click_on_list_of_lang() -> None:
        with allure.step('Кликаем на список доступных языков'):
            browser.element('#language_pulldown').click()

    @staticmethod
    def choose_lang(language: str) -> None:
        with allure.step(f'Выбираем {language} язык'):
            browser.element(f'[onclick*="{language}"]').click()

    @staticmethod
    def check_community_tab_title() -> None:
        with allure.step('Проверяем заголовок вкладки "Community Activity".'):
            browser.element('.community_home_title').should(have.exact_text('Community Activity'))

    @staticmethod
    def check_lang_on_page(language: str) -> None:
        with allure.step(f'Проверяем, что на странице установлен {language} язык'):
            browser.element('#language_pulldown').should(have.exact_text('langue'))
