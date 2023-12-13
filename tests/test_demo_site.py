import json
import os
import random
import pytest
from playwright.sync_api import Page, expect



from dotenv import load_dotenv

from pages.dashboard_page import DashboardPage
from pages.email_filters_page import EmailFiltersPage
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

# filter_name = 'test filter name'

filter_data = {
    'filter_name': 'test filter name',
    'condition': 'If all',
    'filter_attribute': 'Any Recipient',
    'comparison_action': 'does not match',
    'condition_criteria': '@siteground.com',
    'action': 'Pipe to a Program',
    'action_value': generate_random_string(8)
}

accounts_list = ['info@qa-automation-tools.com', 'jdoe@qa-automation-tools.com', 'jsmith@qa-automation-tools.com']

@pytest.fixture()
def dot_env():
    load_dotenv()


@pytest.fixture()
def dashboard_page(dot_env, page: Page):
    return DashboardPage(page)


@pytest.fixture()
def email_filters_page(dot_env, page: Page):
    return EmailFiltersPage(page)


@pytest.fixture()
def token(dot_env, language_code):
    secret = os.getenv('SECRET')
    token = Token.encode(lang=language_code, secret=secret, algorithm='HS256')
    return token


@pytest.mark.parametrize("language_code, success_message",
                         [
                             ("en", "Filter {} is created."),
                             ("es_ES", "Filtro {} ha sido creado."),
                             ("de_De", "Der Filter {} wird erstellt."),
                             ("it_IT", "Il filtro {} è stato creato."),
                             ("fr_FR", "Le filtre  {}  est créé.")
                         ])
def test_create_mail_filter(dot_env, context, page, dashboard_page, email_filters_page, token, language_code, success_message):

    navigate_to_email_filters(dashboard_page, email_filters_page, token)
    email_filters_page.create_new_filter(**filter_data)

    expect(email_filters_page.box_notification).to_have_text(success_message.format(filter_data['filter_name']))

@pytest.mark.parametrize("language_code", ["en", "es_ES", "de_De", "it_IT",  "fr_FR"])
def test_delete_mail_filter(browser, token, page: Page, dashboard_page: DashboardPage, email_filters_page: EmailFiltersPage, language_code):
    # Prepare records for the delete operation
    navigate_to_email_filters(dashboard_page, email_filters_page, token)
    number_of_expected_filters = 3
    additional_filters = [
        'Test filter 1',
        'Test filter 2',
        'Test filter 3'
    ]
    for i in range(0, number_of_expected_filters):
        filter_data['filter_name'] = additional_filters[i]
        email_filters_page.create_new_filter(**filter_data)
        email_filters_page.box_notification_back_button.click()

    expect(email_filters_page.filter_table_row).to_have_count(len(additional_filters))
    email_filters_page.delete_table_row_by_index(1)
    additional_filters.pop(1)
    expect(email_filters_page.filter_table_row).to_have_text(additional_filters)


def navigate_to_email_filters(dashboard_page, email_filters_page, token):
    dashboard_page.navigate(token)
    dashboard_page.left_nav_bar.navigate_to_email_filters()
    email_filters_page.email_account_select.click()
    expect(email_filters_page.email_account_item).to_have_text(accounts_list)
    email_filters_page.select_menu_option(menu_locator=email_filters_page.email_account_select,
                                          option=accounts_list[0], use_inner_text=True)