from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Footer Instagram Icon')
def click_insta_icon(context):
    context.app.footer.click_insta_icon()


@then('Verify the user is Navigated to the CureSkin Instagram Page')
def verify_insta_icon_nav(context):
    context.app.footer.verify_insta_icon_nav()