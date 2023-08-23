from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Shop All Header Link')
def click_shopall_header_link(context):
    context.app.header.click_shopall_header_link()


@then('Verify that the user is navigated to the Shop All Main Page')
def verify_shopall_header_link(context):
    context.app.header.verify_shopall_header_link()
