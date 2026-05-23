import allure
from selene import browser, have, by


class CartPage:
    @staticmethod
    @allure.step('Добавляем игру в корзину')
    def add_game_to_cart() -> None:
        browser.element('.btn_addtocart').click()

    @staticmethod
    @allure.step('Переходим в корзину')
    def move_to_cart() -> None:
        browser.all('[type="button"]').element_by(have.text('View My Cart')).click()

    @staticmethod
    @allure.step('Продолжаем покупки')
    def continue_buying() -> None:
        browser.all('[type="button"]').element_by(have.text('Continue Shopping')).click()

    @staticmethod
    @allure.step('Удаляем игру из корзины')
    def remove_game_from_cart(game_name: str) -> None:
        game_title = browser.element(by.text(game_name))
        remove_button = game_title.element(by.text("Remove"))
        remove_button.click()

    @staticmethod
    @allure.step('Очищаем корзину')
    def clear_cart() -> None:
        browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()

    @staticmethod
    @allure.step('Проверяем наличие игры {game_name} в корзине.')
    def check_game_in_cart(game_name) -> None:
        browser.element('.pVXX8Pzc4JbT40TP4RwRG').should(have.exact_text(game_name))

    @staticmethod
    @allure.step('Проверяем, что корзина пустая.')
    def check_empty_cart() -> None:
        browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Your cart is empty."))

