from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Vitamin ABC Cream Cream')
def click_vitamin_cream(context):
    context.app.product_details_page.click_vitamin_cream()


@then('Verify that the user is navigated to the Vitamin ABC Cream Page from Shop by Face')
def verify_vitamin_cream(context):
    context.app.product_details_page.verify_vitamin_cream()