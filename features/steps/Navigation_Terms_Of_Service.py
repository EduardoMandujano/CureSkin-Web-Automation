from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the X to close the Popup Window')
def click_on_x_icon(context):
    context.app.main_page.click_on_x_icon()


@when('Click on the Terms Of Service Link')
def click_on_terms_of_service(context):
    context.app.main_page.click_on_terms_of_service()


@then('Verify that the user is navigated to the CureSkin Terms Of Service page')
def verify_tos_page(context):
    context.app.main_page.navigation_to_tos_page()
