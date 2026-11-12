from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class StartForm(Form):
    def __init__(self):
        super().__init__(
            Locator.by_xpath('//*[contains(@class, "start__button")]'), 
            'Start Form'
        )

        self.start_game_link = self._element_factory.get_link(
            Locator.by_xpath('//a[@href="/game.html"]'), 'Start Game Button'
        )

    def start_game(self):
        self.start_game_link.click_and_wait()