
import allure
from allure_commons.types import Severity
from faker import Faker

from enums.settings import Settings
from steam.pages.cart import CartPage
from steam.pages.main import MainPage
from steam.pages.search import SearchPage


@allure.severity(Severity.CRITICAL)
@allure.tag('web')
@allure.label('owner', Settings.OWNER)
@allure.link(Settings.BASE_URL, name='Steam')
class BseTest:
    fake = Faker()
    
    @staticmethod
    def add_game_to_cart(game_name: str) -> None:
        MainPage.open_main_page()
        SearchPage.click_on_search()
        SearchPage.find_game_in_search(game_name)
        SearchPage.click_on_first_game_in_search_row()
        CartPage.add_game_to_cart()

    GAMES_LIST: list[str] = [
        "Dota 2",
        "PUBG: BATTLEGROUNDS",
        "Forza Horizon 6",
        "Rust",
        "Bongo Cat",
        "Apex Legends",
        "Subnautica 2",
        "Slay the Spire 2",
        "Marvel Rivals",
        "Geometry Dash",
        "ARC Raiders",
    ]

    LANGUAGES_LIST: list[str] = [
        "koreana",
        "thai",
        "bulgarian",
        "czech",
        "danish",
        "german",
        "russian",
        "english",
    ]