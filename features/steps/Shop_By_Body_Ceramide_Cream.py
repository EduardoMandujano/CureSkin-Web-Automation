from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Ceramide Care Cream from Shop by Body')
def click_ceramide_from_body(context):
    context.app.product_details_page.click_ceramide_from_body()


@then('Verify that the user is navigated to the Ceramide Care Cream Page from Shop by Body')
def verify_ceramide_from_body(context):
    context.app.product_details_page.verify_ceramide_from_body()

