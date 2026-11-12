from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label


class LoginForm(Form):    
    def __init__(self):
        super().__init__(
            Locator.by_xpath('//*[@class="login-form"]'), 'Login Form'
        )

        self.domain_item_for_combobox = '//*[@class="dropdown__list-item" and text()="{}"]'
        self.domain_combobox_item_locator = Locator.by_xpath('//*[@class="dropdown__list-item"]')

        self.password_textbox = self._element_factory.get_text_box(
            Locator.by_xpath('//input[contains(@placeholder, "Password")]'), 
            'Password textbox'
        )
        self.email_textbox = self._element_factory.get_text_box(
            Locator.by_xpath('//input[contains(@placeholder, "email")]'), 
            'Email textbox'
        )
        self.domain_textbox = self._element_factory.get_text_box(
            Locator.by_xpath('//input[contains(@placeholder, "Domain")]'), 
            'Domain textbox'
        )
        self.domain_combobox_list = self._element_factory.get_combo_box(
            Locator.by_xpath('//*[@class="dropdown__list"]'), 
            'Domain combobox list'
        )
        self.domain_combobox = self._element_factory.get_combo_box(
            Locator.by_xpath('//*[contains(@class, "dropdown__opener")]'), 
            'Domain combobox'
        )
        self.terms_and_conditions_checkbox = self._element_factory.get_check_box(
            Locator.by_xpath('//label[contains(@class, "checkbox")]'), 
            'Terms & Conditions checkbox'
        )
        self.next_button = self._element_factory.get_button(
            Locator.by_xpath('//a[contains(text(), "Next")]'), 
            'Go to the next page button'
        )

    def input_password(self, password):
        self.password_textbox.clear_and_type(password)

    def input_email(self, email):
        self.email_textbox.clear_and_type(email)

    def input_domain(self, domain):
        self.domain_textbox.clear_and_type(domain)

    def get_all_domains_from_combobox(self):
        if not self.domain_combobox_list.state.is_displayed():
            self.domain_combobox.click()

        items = self.domain_combobox_list.find_child_elements(
            Label,
            Locator.by_xpath('//*[@class="dropdown__list-item"]')
        )
        return [item.text for item in items]
    
    def choose_domain_in_combobox(self, domain):
        if not self.domain_combobox_list.state.is_displayed():
            self.domain_combobox.click()

        domain_item_button = self._element_factory.get_button(
            Locator.by_xpath(self.domain_item_for_combobox.format(domain)), 
            f'Item "{domain}" from domain combobox'
        )
        domain_item_button.click()

    def accept_terms_and_conditions_checkbox(self):
        self.terms_and_conditions_checkbox.check()

    def go_to_the_next_page(self):
        self.next_button.click_and_wait()