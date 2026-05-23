import allure

from enums.settings import Settings
from steam.pages.main import MainPage
from steam.pages.search import SearchPage
from tests.base_test import BseTest


@allure.epic('Поиск')
@allure.link(Settings.BASE_URL, name='Steam')
class TestSearch(BseTest):
    @allure.title('Нахождение игры по поиску')
    def test_search_field(self):
        random_game = self.fake.random_element(elements=self.GAMES_LIST)

        MainPage.open_main_page()

        SearchPage.click_on_search()
        SearchPage.find_game_in_search(random_game)

        SearchPage.check_search_result(random_game)
