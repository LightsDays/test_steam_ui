from selene import Browser
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser: Browser) -> None:
    """
        Добавляет скриншот

        Attributes:
            :browser: экземпляр браузера
    """
    if not browser:
        return

    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(browser: Browser) -> None:
    """
        Добавляет ссылку на страницу

        Attributes:
            :browser: экземпляр браузера
    """
    if not browser:
        return

    html = browser.driver.page_source
    allure.attach(body=html, name='HTML', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser: Browser) -> None:
    """
        Добавляет видео

        Attributes:
            :browser: экземпляр браузера
    """
    if not browser:
        return

    video_url = "https://selenoid.autotests.cloud/video/" + str(browser.driver.session_id) + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + str(browser.driver.session_id), AttachmentType.HTML, '.html')
