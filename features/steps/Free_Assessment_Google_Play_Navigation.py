from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Free Assessment Header Button')
def click_free_assessment_button(context):
    context.app.header.click_free_assessment_button()


@then('Verify that the user is navigated to the Google Play Cureskin App Page')
def verify_free_assessment_nav(context):
    context.app.header.verify_free_assessment_nav()
