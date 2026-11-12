from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices

from src.forms.start_form import StartForm
from src.forms.help_form import HelpForm


class TestCloseHelp:
    def test_close_help(self):
        Logger.info("Тест-кейс №2. Сокрытие формы помощи")

        start_form = StartForm()
        help_form = HelpForm()

        Logger.info("Проверка открытия стартовой страницы")
        assert start_form.state.is_displayed(), 'Домашняя страница не была открыта'

        Logger.info("Нажатие кнопки Start Game")
        start_form.start_game()
        Logger.info("Ожидание появления формы помощи")
        assert help_form.state.wait_for_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма помощи не была открыта'

        Logger.info("Нажатие кнопки сокрытия помощи")
        help_form.close_help_form()
        Logger.info("Проверка закрытия формы помощи")
        assert help_form.custom_wait_for_not_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().script
        ), 'Форма помощи не была закрыта после нажатия кнопки "Send to bottom"'

        Logger.info("Тест сокрытия формы помощи успешно завершен")