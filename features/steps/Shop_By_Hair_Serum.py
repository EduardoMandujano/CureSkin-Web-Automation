from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Smooth & Shine Serum')
def click_on_serum(context):
    context.app.product_details_page.click_on_serum()


@then('Verify that the user is navigated to the Smooth & Shine Serum Hair Page')
def verify_serum(context):
    context.app.product_details_page.verify_hair_serum()