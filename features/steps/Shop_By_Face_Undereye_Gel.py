from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Under Eye Gel')
def click_undereye(context):
    context.app.product_details_page.click_undereye()


@then('Verify that the user is navigated to the Under Eye Gel Page')
def verify_undereye(context):
    context.app.product_details_page.verify_undereye()