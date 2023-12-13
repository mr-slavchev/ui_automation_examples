from pages.base_page import BasePage
from pages.partial_page_objects.left_nav_bar import LeftNavBar


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.dashboard_url = 'dashboard'
        self.left_nav_bar = LeftNavBar(page)

    def navigate(self, token: str):
        self.page.goto(f'{self._base_url}/{self.dashboard_url}?demoToken={token}')
