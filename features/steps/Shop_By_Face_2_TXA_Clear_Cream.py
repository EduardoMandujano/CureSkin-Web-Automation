from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on TXA Clear Cream')
def click_txa_cream(context):
    context.app.product_details_page.click_txa_cream()


@then('Verify that the user is navigated to the TXA Clear Cream Page from Shop by Face')
def verify_txa_cream(context):
    context.app.product_details_page.verify_txa_cream()