from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    VISIBLE_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    PRESENT_INPUT_FIELD = (By.ID, 'ap_email')
    LOGIN_TEXT = (By.ID, 'login')

    def verify_sign_in_page(self, expected_text):
        expected_text = 'Sign in'
        actual_text = self.driver.find_element(*self.VISIBLE_SIGNIN).text
        assert expected_text == actual_text, f'Expected {expected_text} but got actual {actual_text}'

    def verify_input_field_present(self):
        email = self.driver.find_element(*self.PRESENT_INPUT_FIELD)
        assert email, f"Expecting Email Field but could not find the field"

    def verify_login_page_nav(self):
        login = self.driver.find_element(*self.LOGIN_TEXT)
        assert login, f'Expecting Login text, but could NOT find'
