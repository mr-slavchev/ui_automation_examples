from pages.base_page import BasePage


class EmailFiltersPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.emai_filters_url = 'email-filters'
        # Locators
        self.email_account_select = page.locator('div[data-e2e="email-filters-users"]')
        self.email_account_item = page.locator('div[data-e2e^="dropdown-option-"]')
        self.filter_name_input = page.locator('input[data-e2e="text-input-filter_name"]')
        self.condition_dropdown = page.locator('div[data-e2e="match-condition"]')
        self.filter_attribute_dropdown = page.locator('div[data-e2e="subject"]')
        self.comparison_action_dropdown = page.locator('div[data-e2e="comparision-wrapper"]') # << typo in the HTML
        self.condition_criteria_input = page.locator('input[data-e2e="text-input-conditions[0].value"]')
        self.action_dropdown = page.locator('div[data-e2e="actions"]')
        self.action_value_input = page.locator('input[data-e2e="text-input-actions[0].value"]')
        self.create_button = page.locator('button[data-e2e="create-box-submit"]')
        self.box_notification = page.locator('div[data-e2e="box-notification"] > h3')
        self.box_notification_back_button = page.locator('button[data-e2e="box-notification-back-button"]')
        self.filter_table_row = page.locator('tr[data-e2e="table-row"]')
        self.dialogue_confirm_button = page.locator('button[data-e2e="dialog-submit"]')

        # Locator maps used for menus
        self.condition_map = { 'If all': 'div[data-e2e="dropdown-option-match_all_cond"]'}
        self.filter_attribute_map = {'Any Recipient': 'div[data-e2e="dropdown-option-To_Cc"]'}
        self.comparison_action_map = {'does not match': 'div[data-e2e="dropdown-option-not_regex_match"]'}
        self.action_map = {'Pipe to a Program': 'div[data-e2e="dropdown-option-pipe_to_program"]'}

    def navigate(self, token):
        self.page.goto(f'{self._base_url}/{self.emai_filters_url}?demoToken={token}')

    def create_new_filter(
            self,
            filter_name: str,
            condition: str,
            filter_attribute: str,
            comparison_action: str,
            condition_criteria: str,
            action: str,
            action_value: str
    ):
        self.filter_name_input.type(filter_name)
        self.select_menu_option(menu_locator=self.condition_dropdown, option=self.condition_map[condition])
        self.select_menu_option(menu_locator=self.filter_attribute_dropdown, option=self.filter_attribute_map[filter_attribute])
        self.select_menu_option(menu_locator=self.comparison_action_dropdown, option=self.comparison_action_map[comparison_action])
        self.condition_criteria_input.type(condition_criteria)
        self.select_menu_option(menu_locator=self.action_dropdown, option=self.action_map[action])
        self.action_value_input.type(action_value)
        self.create_button.click()

    def delete_table_row_by_index(self, index: int):
        row = self.filter_table_row.nth(index)
        row.locator('span[data-e2e="table-action-delete"]').click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.dialogue_confirm_button.click()



