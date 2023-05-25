from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when ('Click on the Refund Policy Link')
def click_refund(context):
    context.app.footer.click_refund()


@then('Verify that the user is navigated to the CureSkin Refund Policy Page')
def verify_refund(context):
    context.app.footer.verify_refund()
