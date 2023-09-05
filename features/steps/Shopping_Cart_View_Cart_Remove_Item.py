from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Minus Icon')
def click_minus_icon(context):
    context.app.header.click_minus_icon()


@then('Verify that the cart is empty')
def verify_emptied_cart(context):
    context.app.header.verify_emptied_cart()
