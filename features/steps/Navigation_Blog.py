from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the CureSkin Blog Link')
def click_on_blog(context):
    context.app.footer.click_blog()


@then('Verify that the user is navigated to the CureSkin Blog Page')
def verify_blog(context):
    context.app.footer.verify_blog()
