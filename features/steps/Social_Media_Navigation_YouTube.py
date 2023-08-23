from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Footer YouTube Icon')
def click_youtube_icon(context):
    context.app.footer.click_youtube_icon()


@then('Verify the user is Navigated to the CureSkin YouTube Page')
def verify_youtube_icon_nav(context):
    context.app.footer.verify_youtube_icon_nav()
