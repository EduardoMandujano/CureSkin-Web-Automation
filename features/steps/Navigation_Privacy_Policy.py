from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Privacy Policy Link')
def click_privacy(context):
    context.app.footer.click_privacy()


@then('Verify that the user is navigated to the CureSkin Privacy Policy Page')
def verify_privacy(context):
    context.app.footer.verify_privacy()