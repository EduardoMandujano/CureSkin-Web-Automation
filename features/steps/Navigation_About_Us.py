from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the About Us Link')
def click_on_about_us(context):
    context.app.footer.click_on_about_us()


@then('Verify that the user is navigated to the CureSkin About Us page')
def verify_about_us_nav(context):
    context.app.footer.verify_about_us_nav()
