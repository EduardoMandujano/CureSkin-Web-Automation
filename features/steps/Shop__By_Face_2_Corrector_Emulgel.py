from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on the Next Page Link')
def click_next_page(context):
    context.app.search_results_page.click_on_face_page2()


@when('Click on Corrector Emulgel')
def click_corrector_emulgel(context):
    context.app.product_details_page.click_corrector_emulgel()


@then('Verify that the user is navigated to the Corrector Emulgel Page from Shop by Face')
def verify_corrector_emulgel(context):
    context.app.product_details_page.verify_corrector_emulgel()
