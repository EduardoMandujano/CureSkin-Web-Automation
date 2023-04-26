from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class MainPage(Page):
    MAIN_PAGE_TEXT = (By.CSS_SELECTOR, 'h2.title')

    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def return_nav_to_cureskin_main(self):
        back_to_main = self.wait_for_element_appear(*self.MAIN_PAGE_TEXT)
        assert back_to_main, f"Expected navigation to Main Page"


