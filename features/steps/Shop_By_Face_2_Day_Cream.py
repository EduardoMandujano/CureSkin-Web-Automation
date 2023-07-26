from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Lightening Day Cream')
def click_day_cream(context):
    context.app.product_details_page.click_day_cream()


@then('Verify that the user is navigated to the Lightening Day Cream Page from Shop by Face')
def verify_day_cream(context):
    context.app.product_details_page.verify_day_cream()