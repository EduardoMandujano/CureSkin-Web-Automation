from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the BC Shampoo Link')
def click_bc_shampoo_link(context):
    context.app.header.click_bc_shampoo_link()


@then('Verify the text of the BC Shampoo in the Product Details Page')
def verify_bc_shampoo_text(context):
    context.app.header.verify_bc_shampoo_text()


