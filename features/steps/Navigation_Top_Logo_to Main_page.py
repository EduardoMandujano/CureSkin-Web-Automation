from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


# HEADER_LOGO = (By.CSS_SELECTOR, "a.header__heading-link")

@given('Open CureSkin Search Results Page')
def open_cureskin_search_results_page(context):
    context.app.search_results_page.open_cureskin_search()


@when('Click on CureSkin logo in the Header')
def click_on_header_cureskin_logo(context):
    context.app.search_results_page.click_on_cureskin_logo()


@then('Verify that user is taken to the main page')
def verify_nav_to_main_page(context):
    context.app.main_page.return_nav_to_cureskin_main()
