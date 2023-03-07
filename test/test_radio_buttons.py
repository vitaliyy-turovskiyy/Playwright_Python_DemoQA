import pytest

from pages.radio_button_page import RadioButton
from utils.tools import take_screenshot


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1366, 'height': 768})
        self.radio = RadioButton(self.page)

        self.page.goto('https://demoqa.com/radio-button')

    def test_text_boxes(self, test_setup):

        self.radio.select_radio_button('Yes')
        self.radio.check_result('Yes')

        self.radio.select_radio_button('Impressive')
        self.radio.check_result('Impressive')
        take_screenshot(self.page, "test_text_boxes")