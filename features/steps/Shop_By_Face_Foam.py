from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Gentle Cleanse Face Foam')
def click_face_foam(context):
    context.app.product_details_page.click_face_foam()

@then('Verify that the user is navigated to the Gentle Cleanse Face Foam Page')
def verify_face_foam(context):
    context.app.product_details_page.verify_face_foam()