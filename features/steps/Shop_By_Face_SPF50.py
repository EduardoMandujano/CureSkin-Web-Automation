from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on SPF50')
def click_spf50(context):
    context.app.product_details_page.click_spf50()


@then('Verify SPF50')
def verify_spf50(context):
    context.app.product_details_page.verify_spf50()
