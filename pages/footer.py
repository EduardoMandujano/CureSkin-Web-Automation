from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Footer(Page):
    ABOUT_US_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/about-cureskin/"]')

    def click_on_about_us(self):
        self.driver.find_element(*self.ABOUT_US_LINK).click()

    def verify_about_us_nav(self, expected_url="https://cureskin.com/about-cureskin/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"


