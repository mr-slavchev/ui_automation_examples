from playwright.sync_api import Page


class LeftNavBar:
    def __init__(self, page: Page):
        self.page = page
        self.email_list_item = page.locator('li[data-e2e="navigation-group-mail"]')
        self.email_filter_link = page.locator('a[data-e2e="navigation-list-item-email-filters"]')

    def navigate_to_email_filters(self):
        self.email_list_item.click()
        self.email_filter_link.click()