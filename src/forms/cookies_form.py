from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class CookiesForm(Form):
    def __init__(self):
        super().__init__(
            Locator.by_xpath('//*[@class="cookies"]'), 'Cookies Form'
        )

        self.accept_cookies_button = self._element_factory.get_button(
            Locator.by_xpath('//button[contains(text(), "Not really")]'), 
            'Accept cookies button'
        )

    def accept_cookies(self):
        self.accept_cookies_button.click()