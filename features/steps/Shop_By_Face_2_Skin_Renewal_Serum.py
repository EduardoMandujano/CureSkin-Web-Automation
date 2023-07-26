from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Skin Renewal Serum')
def click_skin_ren_serum(context):
    context.app.product_details_page.click_skin_ren_serum()


@then('Verify that the user is navigated to the Skin Renewal Serum Page from Shop by Face')
def verify_skin_ren_serum(context):
    context.app.product_details_page.verify_skin_ren_serum()