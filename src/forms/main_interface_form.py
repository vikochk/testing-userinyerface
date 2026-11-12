from datetime import datetime
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class MainInterfaceForm(Form):    
    def __init__(self):
        self.timer_locator = Locator.by_xpath('//*[contains(@class, "timer")]')
        super().__init__(self.timer_locator, 'Main Interface Form')
    
        self.timer_label = self._element_factory.get_label(self.timer_locator, 'Timer Label')

    def get_time_from_page(self):
        time_str = self.timer_label.get_text()
        time = datetime.strptime(time_str, '%H:%M:%S').time()
        return time