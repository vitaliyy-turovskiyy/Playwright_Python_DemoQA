import pytest

from pages.buttons_page import Buttons
from utils.tools import take_screenshot


class TestButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1366, 'height': 768})
        self.buttons = Buttons(self.page)

        self.page.goto('https://demoqa.com/buttons')

    def test_double_click_button(self, test_setup):

        self.buttons.perform_double_click()

        self.buttons.check_double_click_result()
        take_screenshot(self.page, "double_click")

    def test_rmb_click_button(self, test_setup):

        self.buttons.perform_rmb_click()

        self.buttons.check_rmb_click_result()
        take_screenshot(self.page, "rmb_click")

    def test_dynamic_button(self, test_setup):

        self.buttons.click_the_button()

        self.buttons.check_click_result()
        take_screenshot(self.page, "dynamic_button")
