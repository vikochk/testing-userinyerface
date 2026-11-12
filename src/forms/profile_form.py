import base64
import mimetypes
from py_selenium_auto.forms.form import Form
from py_selenium_auto.elements.label import Label
from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.browsers.browser_services import BrowserServices


class ProfileForm(Form):
    def __init__(self):
        super().__init__(
            Locator.by_xpath('//*[@class="avatar-and-interests-page"]'), 
            'Profile Form'
        )
        self.interest_label_locator = '//label[contains(@for, "interest_{}")]'

        self.upload_photo_button = self._element_factory.get_button(
            Locator.by_xpath('//a[contains(@class, "upload-button")]'), 
            'Upload photo button'
        )
        self.next_button = self._element_factory.get_button(
            Locator.by_xpath('//button[contains(text(), "Next")]'), 
            'Go to the next page button'
        )
        self.interests_list = self._element_factory.get_text_box(
            Locator.by_xpath('//*[@class="avatar-and-interests__interests-list"]'),
            'All interests box'
        )

    def get_all_labels(self):
        labels = self.interests_list.find_child_elements(
            Label,
            Locator.by_xpath('.//label[starts-with(@for, "interest_")]')
        )

        result = []
        for label in labels:
            value = label.get_attribute('for').replace('interest_', '')
            if 'select' in value and 'all' in value:
                continue
            result.append(value)

        return result
    
    def unselect_all_labels(self):
        self.click_one_label('unselectall')

    def click_one_label(self, label_name):
        current_label = self._element_factory.get_label(
            Locator.by_xpath(self.interest_label_locator.format(label_name)), 
            f'{label_name.capitalize()} label'
        )
        current_label.click()
    
    def upload_photo(self, photo_path):
        with open(photo_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        mime_type, _ = mimetypes.guess_type(photo_path)
        
        data_url = f'data:{mime_type};base64,{encoded_string}'

        direct_upload_script = '''
        var vueEl = document.querySelector('.avatar-and-interests');
        if (vueEl && vueEl.__vue__) {
            vueEl.__vue__.onAvatarComplete(arguments[0]);
            return "Success";
        }
        return "Vue component not found";
        '''

        result = BrowserServices.Instance.browser.driver.execute_script(direct_upload_script, data_url)
        if result != 'Success':
            Logger.fatal(f'Не удалось напрямую загрузить фото: {result}', RuntimeError)

    def go_to_the_next_page(self):
        self.next_button.click_and_wait()