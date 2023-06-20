from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on SPF30')
def click_spf30(context):
    context.app.product_details_page.click_spf30()


@then("Verify that the user is navigated to the SPF30 Page")
def verify_spf30(context):
    context.app.product_details_page.verify_spf30()
