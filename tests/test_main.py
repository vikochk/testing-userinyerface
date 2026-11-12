import string
from pathlib import Path
from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from src.forms.start_form import StartForm
from src.forms.login_form import LoginForm
from src.forms.profile_form import ProfileForm
from src.utils.test_manager import TestDataProvider
from src.utils.random_generation import RandomGeneration


class TestMain:
    PHOTO_PATH = Path(RootPathHelper.current_root_path(__file__)) \
             / "resources" \
             / TestDataProvider.get_instance().photo_name

    PHOTO_PATH = str(PHOTO_PATH.resolve())

    def test_main(self):
        Logger.info("Тест-кейс №1. Проверка логики работы форм для регистрации и заполнения профиля")

        start_form = StartForm()
        login_form = LoginForm()
        profile_form = ProfileForm()

        Logger.info("Проверка открытия стартовой страницы")
        assert start_form.state.is_displayed(), 'Домашняя страница не была открыта'

        Logger.info("Нажатие кнопки Start Game")
        start_form.start_game()
        Logger.info("Ожидание появления формы для регистрации")
        assert login_form.state.wait_for_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма для ввода регистрации не была открыта'

        Logger.info("Генерация действующего пароля и ввод в соответствующее поле")
        login_form.input_password(RandomGeneration.generate_string(10, [string.ascii_uppercase, string.digits], 'a'))
        Logger.info("Генерация действующего адреса электронной почты и ввод в соответствующее поле")
        login_form.input_email(RandomGeneration.generate_string(length=5, mandatory_symbols='a'))
        Logger.info("Генерация действующего домена и ввод в соответствующее поле")
        login_form.input_domain(RandomGeneration.generate_string(length=5, mandatory_symbols='a'))
        Logger.info("Выбор случайного домена из списка доступных")
        login_form.choose_domain_in_combobox(
            RandomGeneration.choose_from_list(login_form.get_all_domains_from_combobox())
        )
        Logger.info("Принятие условий пользования")
        login_form.accept_terms_and_conditions_checkbox()

        Logger.info("Нажатие кнопки перехода на следующую страницу")
        login_form.go_to_the_next_page()
        Logger.info("Проверка закрытия формы для регистрации")
        assert profile_form.state.wait_for_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма регистрации не была закрыта после нажатия кнопки "Next"'
        
        Logger.info(f"Нажатие кнопки для загрузки фото и выбор фото по пути '{self.PHOTO_PATH}'")
        profile_form.upload_photo(self.PHOTO_PATH)
        Logger.info(f"Нажатие чекбокса для выключения остальных чекбоксов в списке интересов")
        profile_form.unselect_all_labels()
        
        all_checkbox_from_website = profile_form.get_all_labels()
        already_used_labels = []

        for _ in range(TestDataProvider.get_instance().amount_of_required_interests):
            current_label = RandomGeneration.choose_from_list(
                all_checkbox_from_website, already_used_labels
            )
            Logger.info(f"Нажатие чекбокса {current_label} в списке интересов")
            profile_form.click_one_label(current_label)
            already_used_labels.append(current_label)
        
        Logger.info("Нажатие кнопки перехода на следующую страницу")
        profile_form.go_to_the_next_page()
        Logger.info("Проверка закрытия формы для заполнения профиля")
        assert profile_form.state.wait_for_not_displayed(
            BrowserServices.Instance.service_provider.timeout_configuration().page_load
        ), 'Форма для заполнения профиля не была закрыта после нажатия кнопки "Next"'

        Logger.info("Тест на проверку логики работы форм для регистрации и заполнения профиля успешно завершен")