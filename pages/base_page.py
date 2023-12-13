import os

from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._base_url = os.getenv('BASE_URL')

    def select_menu_option(self, menu_locator: Locator, option, use_inner_text=False):
        menu_locator.click()
        if use_inner_text:
            menu_locator.get_by_role('option').filter(has_text=option).click()
        else:
            menu_locator.locator(option).click()
