from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Hair Conditioner')
def click_on_conditioner(context):
    context.app.product_details_page.click_hair_conditioner()


@then('Verify that the user is navigated to the Hair Conditioner Page')
def verify_conditioner(context):
    context.app.product_details_page.verify_hair_conditioner()