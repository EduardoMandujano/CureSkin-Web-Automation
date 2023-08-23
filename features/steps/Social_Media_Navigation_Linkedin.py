from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Footer Linkedin Icon')
def click_linkedin_icon(context):
    context.app.footer.click_linkedin_icon()


@then('Verify the user is Navigated to the CureSkin Linkedin Page')
def verify_linkedin_icon_nav(context):
    context.app.footer.verify_linkedin_icon_nav()