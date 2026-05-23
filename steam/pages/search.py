import allure
from selene import browser, have


class SearchPage:
    @staticmethod
    @allure.step('Кликаем на поле поиска')
    def click_on_search() -> None:
            browser.element('#store_nav_search_term').click()

    @staticmethod
    def find_game_in_search(game_name: str) -> None:
        with allure.step(f'Вводим в поле поиска текст "{game_name}"'):
            browser.element('#store_nav_search_term').type(game_name).press_enter()

    @staticmethod
    @allure.step('Кликаем на первый результат поиска')
    def click_on_first_game_in_search_row() -> None:
        browser.all('.search_result_row').first.click()

    @staticmethod
    def check_search_result(game_name: str) -> None:
        with allure.step(f'Проверяем, что была найдена игра "{game_name}".'):
            browser.element('.title').should(have.exact_text(game_name))
