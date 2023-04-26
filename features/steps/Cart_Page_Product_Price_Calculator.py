from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Product Details page of CureSkin Cleansing Gel')
def open_cureskin_product_details_page(context):
    context.app.product_details_page.open_cureskin_cleansing_gel_prod_details()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_details_page.add_to_cart()


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.open_your_cart()


@when('Store the current price')
def store_current_price(context):
    context.app.cart_page.storing_the_price()


@when('Click plus icon to increase product quantity')
def click_plus_icon(context):
    context.app.cart_page.clicking_plus_icon()


@then('Verify total price has doubled')
def verify_doubled_price(context):
    context.app.cart_page.price_has_doubled("Rs. 590.00")


@then('Verify that product quantity is set to 2')
def verify_product_quantity(context):
    context.app.cart_page.quantity_has_doubled("2")

