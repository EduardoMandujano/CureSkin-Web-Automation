from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Ceramide Cream')
def click_ceramide(context):
    context.app.product_details_page.click_ceramide()


@then('Verify Ceramide Cream')
def verify_ceramide(context):
    context.app.product_details_page.verify_ceramide()
