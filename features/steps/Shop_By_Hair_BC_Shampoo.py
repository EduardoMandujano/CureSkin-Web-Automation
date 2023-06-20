from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Shop By Hair')
def click_on_hair(context):
    context.app.product_details_page.click_on_hair()


@when('Click on Biotin & Collagen Shampoo')
def click_shampoo(context):
    context.app.product_details_page.click_shampoo()


@then('Verify that the user is navigated to the Biotin & Collagen Shampoo Page')
def verify_shampoo(context):
    context.app.product_details_page.verify_shampoo()
