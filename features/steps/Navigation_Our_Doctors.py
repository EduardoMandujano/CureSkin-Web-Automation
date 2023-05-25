from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Our Doctors Link')
def click_on_our_doctors(context):
    context.app.footer.click_on_our_doctors()


@then('Verify that the user is navigated to the CureSkin Our Doctors page')
def verify_our_doctors_nav(context):
    context.app.footer.verify_our_doctors()