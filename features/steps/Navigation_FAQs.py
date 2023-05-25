from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the FAQs Link')
def click_on_faqs(context):
    context.app.footer.click_faqs()


@then('Verify that the user is navigated to the CureSkin FAQs Page')
def verify_faqs(context):
    context.app.footer.verify_faqs()