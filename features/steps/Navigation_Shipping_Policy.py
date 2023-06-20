from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Shipping Policy Link')
def click_shipping(context):
    context.app.footer.click_shipping()


@then('Verify that the user is navigated to the CureSkin Shipping Policy Page')
def verify_shipping(context):
    context.app.footer.verify_shipping()