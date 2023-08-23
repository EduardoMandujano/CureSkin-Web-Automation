from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Footer Twitter Icon')
def click_twitter_icon(context):
    context.app.footer.click_twitter_icon()


@then('Verify the user is Navigated to the CureSkin Twitter Page')
def verify_twitter_icon_nav(context):
    context.app.footer.verify_twitter_icon_nav()