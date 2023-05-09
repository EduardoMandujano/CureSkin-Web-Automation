from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    MAIN_PAGE_TEXT = (By.CSS_SELECTOR, 'h2.title')
    X_ICON = (By.CSS_SELECTOR, 'button.popup-close')
    TOS_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="/policies/terms-of-service"]')
    TOS_PAGE_TEXT = (By.CSS_SELECTOR, 'h1:contains("Terms of service")')

    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def return_nav_to_cureskin_main(self):
        back_to_main = self.wait_for_element_appear(*self.MAIN_PAGE_TEXT)
        assert back_to_main, f"Expected navigation to Main Page"

    def click_on_x_icon(self):
        self.driver.find_element(*self.X_ICON).click()

    def click_on_terms_of_service(self):
        self.driver.find_element(*self.TOS_LINK).click()

    def navigation_to_tos_page(self, expected_url="https://shop.cureskin.com/policies/terms-of-service"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"







