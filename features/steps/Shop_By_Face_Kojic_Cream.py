from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Kojic Plus Cream')
def click_kojic(context):
    context.app.product_details_page.click_kojic()


@then('Verify that the user is navigated to the Kojic Plus Cream Page')
def verify_kojic(context):
    context.app.product_details_page.verify_kojic()