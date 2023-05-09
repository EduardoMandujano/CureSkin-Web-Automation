from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open CureSkin Home Page')
def open_cureskin_main_page(context):
    context.app.main_page.open_main()


@when('Click on Login Icon in the Header')
def click_on_login_icon(context):
    context.app.header.click_login_icon()


@then('Verify that the user is taken to the Login Page')
def verify_login_icon_nav(context):
    context.app.sign_in_page.verify_login_page_nav()