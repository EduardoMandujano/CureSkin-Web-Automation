from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Grievance Policy Link')
def click_on_our_grievance(context):
    context.app.footer.click_on_our_grievance()


@then('Verify that the user is navigated to the Cureskin Grievance Policy Page')
def verify_our_grievance(context):
    context.app.footer.verify_our_grievance()
