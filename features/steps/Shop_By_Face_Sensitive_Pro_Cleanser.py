from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Sensitive Pro Cleanser')
def click_sensitive_cleanser(context):
    context.app.product_details_page.click_sensitive_cleanser()


@then('Verify that the user is navigated to the Sensitive Pro Cleanser Page')
def verify_sensitive_cleanser(context):
    context.app.product_details_page.verify_sensitive_cleanser()