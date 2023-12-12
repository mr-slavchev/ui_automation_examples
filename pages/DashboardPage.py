from pages.BasePage import BasePage
from pages.partial_page_objects.LeftNavBar import LeftNavBar


class DashboardPage(BasePage):
    DASHBOARD = 'dashboard'

    def __init__(self, page):
        super().__init__(page)
        self.left_nav_bar = LeftNavBar(page)

    def navigate(self, token: str):
        self.page.goto(f'{self._base_url}/{self.DASHBOARD}?demoToken={token}')
