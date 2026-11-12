from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class HelpForm(Form):
    def __init__(self):
        super().__init__(
            Locator.by_xpath('//*[@class="help-form"]'), 'Help Form'
        )

        self.close_help_form_button = self._element_factory.get_button(
            Locator.by_xpath('//button[contains(@class, "send-to-bottom")]'), 
            'Close help form button'
        )
        self.close_title_text = self._element_factory.get_text_box(
            Locator.by_xpath('//*[@class="help-form__title"]'),
            'Help form title'
        )

    def close_help_form(self):
        self.close_help_form_button.click_and_wait()
    
    def custom_wait_for_not_displayed(self, timeout):
        return self.close_title_text.state.wait_for_not_displayed(timeout)