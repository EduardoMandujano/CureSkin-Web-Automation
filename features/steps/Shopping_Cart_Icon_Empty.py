from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Header Shopping Cart Icon')
def click_shopping_cart_icon(context):
    context.app.header.click_shopping_cart_icon()


@then('Verify the correct sidebar text when the Shopping Cart is empty')
def verify_empty_cart_text(context):
    context.app.header.verify_empty_cart_text()