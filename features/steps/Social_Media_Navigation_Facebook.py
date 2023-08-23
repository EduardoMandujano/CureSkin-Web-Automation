from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Footer Facebook Icon')
def click_fb_icon(context):
    context.app.footer.click_fb_icon()


@then('Verify the user is Navigated to the CureSkin Facebook Page')
def verify_fb_icon_nav(context):
    context.app.footer.verify_fb_icon_nav()

