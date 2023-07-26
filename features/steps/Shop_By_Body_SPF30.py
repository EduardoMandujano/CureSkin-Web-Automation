from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on SPF30 from Shop by Body')
def click_spf30_from_body(context):
    context.app.product_details_page.click_spf30_body()


@then('Verify that the user is navigated to the SPF30 Page from Shop by Body')
def verify_spf_30_from_body(context):
    context.app.product_details_page.verify_spf30_body()