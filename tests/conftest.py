import os
import pytest

from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    Logger.info(f"Установлена рабочая директория: {work_dir}")
    yield
    Logger.info("Завершение тестовой сессии")


@pytest.fixture(scope="function", autouse=True)
def setup_function():
    Logger.info("Запуск браузера")
    browser = BrowserServices.Instance.browser
    browser.maximize()
    browser.go_to(BrowserServices.Instance.service_provider\
                  .settings_file().get("base_url"))
    browser.wait_for_page_to_load()
    yield
    if BrowserServices.Instance.is_browser_started:
        Logger.info("Закрытие браузера")
        BrowserServices.Instance.browser.quit()