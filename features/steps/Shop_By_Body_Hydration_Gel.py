from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click on Hydration Gel from Shop by Body')
def click_hyd_gel_from_body(context):
    context.app.product_details_page.click_hyd_gel_from_body()


@then('Verify that the user is navigated to the Hydration Gel Page from Shop by Body')
def verify_hyd_gel_from_body(context):
    context.app.product_details_page.verify_hyd_gel_from_body()