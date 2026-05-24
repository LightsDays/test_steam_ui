import allure

from steam.pages.main import MainPage
from tests.base_test import BseTest

@allure.epic('Главная страница')
class TestMainPage(BseTest):
    @allure.title('Переключение на вкладку "Сообщество"')
    def test_switch_tab(self):
        MainPage.open_main_page()

        MainPage.switch_navigation_tab(tab_name='COMMUNITY')

        MainPage.check_community_tab_title()

    @allure.title('Смена языка')
    def test_change_language(self):
        MainPage.open_main_page()

        MainPage.click_on_list_of_lang()
        MainPage.choose_lang('german')

        MainPage.check_lang_on_page('german')
