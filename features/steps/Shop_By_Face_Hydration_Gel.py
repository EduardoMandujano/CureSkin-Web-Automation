from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Shop By Face Link')
def click_shop_by_face(context):
    context.app.product_details_page.shop_by_face()


@when('Click on Hydration Gel')
def click_hydration_gel(context):
    context.app.product_details_page.click_hyd_gel()


@then('Verify that the user is navigated to the Hydration Gel Page')
def verify_hydration_gel(context):
    context.app.product_details_page.verify_hydration_gel()
