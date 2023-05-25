from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Why CureSkin Link')
def click_on_why_cureskin(context):
        context.app.footer.click_on_why_cureskin()


@then('Verify that the user is navigated to the Why CureSkin Page')
def verify_why_cureskin(context):
        context.app.footer.verify_why_cureskin()
