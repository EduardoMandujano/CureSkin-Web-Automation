from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on CC Cream Link')
def click_cc_cream_text(context):
    context.app.header.click_cc_cream_text()


@then('Verify the text of the CC Cream in the Product Details Page')
def verify_cc_cream_text(context):
    context.app.header.verify_cc_cream_text()