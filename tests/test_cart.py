import allure

from steam.pages.cart import CartPage
from tests.base_test import BseTest


@allure.epic('Корзина')
class TestCart(BseTest):
    @allure.title('Добавление игры в корзину')
    def test_add_game_to_cart(self):
        random_game = self.fake.random_element(elements=self.GAMES_LIST)

        self.add_game_to_cart(random_game)
        CartPage.move_to_cart()
        CartPage.check_game_in_cart(random_game)


    @allure.title('Удаление игры из корзины')
    def test_remove_game_from_cart(self):
        random_game = self.fake.random_element(elements=self.GAMES_LIST)

        self.add_game_to_cart(random_game)
        CartPage.move_to_cart()
        CartPage.remove_game_from_cart(random_game)
        CartPage.check_empty_cart()


    @allure.title('Полная очистка корзины')
    def test_clear_cart(self):
        games_cnt = self.fake.random_int(min=1, max=5)

        for _ in range(games_cnt):
            self.add_game_to_cart(self.fake.random_element(elements=self.GAMES_LIST))
            CartPage.continue_buying()
        self.add_game_to_cart(self.fake.random_element(elements=self.GAMES_LIST))
        CartPage.move_to_cart()
        CartPage.clear_cart()
        CartPage.check_empty_cart()
