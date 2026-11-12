from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices

from src.forms.start_form import StartForm
from src.forms.cookies_form import CookiesForm


class TestAcceptCookies:
    def test_accept_cookies(self):
        Logger.info("Тест-кейс №3. Принятие cookies")
        
        start_form = StartForm()
        cookies_form = CookiesForm()

        Logger.info("Проверка открытия стартовой страницы")
        assert start_form.state.is_displayed(), 'Домашняя страница не была открыта'

        Logger.info("Нажатие кнопки Start Game")
        start_form.start_game()
        Logger.info("Ожидание появления формы cookies")
        assert cookies_form.state.wait_for_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма с cookies не была открыта'

        Logger.info("Нажатие кнопки принятия cookies")
        cookies_form.accept_cookies()
        Logger.info("Проверка закрытия формы cookies")
        assert cookies_form.state.wait_for_not_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма с cookies не была закрыта после нажатия кнопки "Yes"'

        Logger.info("Тест принятия cookies успешно завершен")