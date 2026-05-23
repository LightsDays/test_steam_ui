import allure

from steam.pages.main import MainPage
from steam.pages.login import LoginPage
from tests.base_test import BseTest


@allure.epic('Страница авторизации')
class TestLoginPage(BseTest):
    @allure.title('Открытие страница авторизации')
    def test_open_login_page(self):
        MainPage.open_main_page()

        LoginPage.click_on_login()

        LoginPage.this_is_login_page()
