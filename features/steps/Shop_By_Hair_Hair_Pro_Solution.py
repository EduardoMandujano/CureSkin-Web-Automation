from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Hair Pro Solution')
def click_hair_solution(context):
    context.app.product_details_page.click_hair_solution()


@then('Verify that the user is navigated to the Hair Pro Solution Page')
def verify_hair_solution(context):
    context.app.product_details_page.verify_hair_solution()
