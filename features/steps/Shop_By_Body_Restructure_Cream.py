from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Shop by Body')
def click_on_body(context):
    context.app.product_details_page.click_on_body()


@when('Click on Restructure Cream')
def click_restructure_cream(context):
    context.app.product_details_page.click_restructure_cream()


@then('Verify that the user is navigated to the Restructure Cream Page')
def verify_restructure_cream(context):
    context.app.product_details_page.verify_restructure_cream()

