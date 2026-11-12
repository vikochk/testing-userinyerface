from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices

from src.forms.start_form import StartForm
from src.forms.main_interface_form import MainInterfaceForm
from src.utils.test_manager import TestDataProvider


class TestCheckTimer:
    def test_check_timer(self):
        Logger.info("Тест-кейс №4. Проверка таймера")

        start_form = StartForm()
        main_interface = MainInterfaceForm()

        Logger.info("Проверка открытия стартовой страницы")
        assert start_form.state.is_displayed(), 'Домашняя страница не была открыта'

        Logger.info("Нажатие кнопки Start Game")
        start_form.start_game()
        Logger.info("Ожидание появления интерфейса с таймером")
        assert main_interface.state.wait_for_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма для ввода пароля и почты не была открыта'

        Logger.info("Сбор значения таймера в интерфейсе")
        website_timer = main_interface.get_time_from_page()
        Logger.info("Сбор ожидаемого значения таймера из тестовых данных")
        expected_time = TestDataProvider.get_instance().expected_timer_value
        Logger.info("Проверка значения таймера")
        assert website_timer == expected_time, \
            f'Таймер начинает свою работу со значения "{website_timer:%H:%M:%S}" '\
            f'вместо ожидаемого "{expected_time:%H:%M:%S}"' 
        
        Logger.info("Тест с проверкой таймера успешно завершен")