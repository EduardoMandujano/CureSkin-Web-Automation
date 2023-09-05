from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click on What's New Item Add to Cart Button")
def add_new_item_to_cart(context):
    context.app.header.add_new_item_to_cart()


@when('Click on the Sidebar View Cart Button')
def click_sidebar_view_cart(context):
    context.app.header.click_sidebar_view_cart()


@then('Verify that the user was navigated to the Your Cart Page')
def verify_your_cart_navigation(context):
    context.app.header.verify_your_cart_navigation()


@then('Verify that the cart contains the Item Added')
def verify_item_added(context):
    context.app.header.verify_item_added()

