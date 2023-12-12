import json
import random
import pytest
from playwright.sync_api import Page, expect


from pages.DashboardPage import DashboardPage
from dotenv import load_dotenv

from pages.EmailFiltersPage import EmailFiltersPage
from utils.token import Token

SPANEL_NAME = 'spanel-demo-store-1699447964500-qa-automation-tools.com'



def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def read_from_json_file(file_path):
    with open(file_path, 'r') as file:
        # Load JSON data from file
        data = json.load(file)
        return data

filter_name = 'test filter name'

filter_data = {
    'filter_name': filter_name,
    'condition': 'If all',
    'filter_attribute': 'Any Recipient',
    'comparison_action': 'does not match',
    'condition_criteria': '@siteground.com',
    'action': 'Pipe to a Program',
    'action_value': generate_random_string(8)
}

accounts_list = ['info@qa-automation-tools.com', 'jdoe@qa-automation-tools.com', 'jsmith@qa-automation-tools.com']

@pytest.fixture
def dot_env():
    load_dotenv()


@pytest.fixture()
def dashboard_page(dot_env, page: Page):
    return DashboardPage(page)


@pytest.fixture()
def email_filters_page(dot_env, page: Page):
    return EmailFiltersPage(page)


@pytest.fixture()
def token(dot_env):
    token = Token.encode(lang='en', secret='secret', algorithm='HS256')
    return token


def test_create_mail_filter(context, page, dashboard_page, email_filters_page, dot_env, token):

    navigate_to_email_filters(dashboard_page, email_filters_page, token)
    email_filters_page.create_new_filter(**filter_data)

    expect(email_filters_page.box_notification).to_have_text(f'Filter {filter_name} is created.')


def test_delete_mail_filter(browser, token, page: Page, dashboard_page: DashboardPage, email_filters_page: EmailFiltersPage):
    #Prepare records for the delete operation
    navigate_to_email_filters(dashboard_page, email_filters_page, token)
    number_of_expected_fitlers = 3
    filter_names = [
        'Test filter 1',
        'Test filter 2',
        'Test filter 2'
    ]
    for i in range(0, number_of_expected_fitlers):
        filter_data['filter_name'] = filter_names[i]
        email_filters_page.create_new_filter(**filter_data)
        email_filters_page.box_notification_back_button.click()

    expect(email_filters_page.filter_table_row).to_have_count(len(filter_names))
    email_filters_page.delete_table_row_by_index(1)
    filter_names.pop(1)
    expect(email_filters_page.filter_table_row).to_have_text(filter_names)


def navigate_to_email_filters(dashboard_page, email_filters_page, token):
    dashboard_page.navigate(token)
    dashboard_page.left_nav_bar.navigate_to_email_filters()
    email_filters_page.email_account_select.click()
    expect(email_filters_page.email_account_item).to_have_text(accounts_list)
    email_filters_page.select_menu_option(menu_locator=email_filters_page.email_account_select,
                                          option_text=accounts_list[0])