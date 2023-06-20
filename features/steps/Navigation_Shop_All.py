from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Shop All Link')
def click_shop_all(context):
    context.app.header.click_shop_all()


@then('Verify that the user is navigated to the CureSkin Shop All Page')
def verify_shop_all(context):
    context.app.header.verify_shop_all()



