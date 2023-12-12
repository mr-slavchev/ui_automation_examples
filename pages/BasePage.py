import os

from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._base_url = os.getenv('BASE_URL')

    def select_menu_option(self, menu_locator: Locator, option_text):
        menu_locator.click()
        menu_locator.get_by_role('option').filter(has_text=option_text).click()