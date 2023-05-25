from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Footer(Page):
    ABOUT_US_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/about-cureskin/"]')
    OUR_DOCTORS_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/doctor/"]')
    GRIEVANCE_POLICY_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/grievance-policy/"]')
    WHY_CURESKIN_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/why-cureskin/"]')
    BLOG_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/blog"]')
    FAQS_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/faqs/"]')
    REFUND_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="/policies/refund-policy"]')

    def click_on_about_us(self):
        self.driver.find_element(*self.ABOUT_US_LINK).click()

    def verify_about_us_nav(self, expected_url="https://cureskin.com/about-cureskin/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"

    def click_on_our_doctors(self):
        self.driver.find_element(*self.OUR_DOCTORS_LINK).click()

    def verify_our_doctors(self, expected_url="https://cureskin.com/doctor/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"

    def click_on_our_grievance(self):
        self.driver.find_element(*self.GRIEVANCE_POLICY_LINK).click()

    def verify_our_grievance(self, expected_url="https://cureskin.com/grievance-policy/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"

    def click_on_why_cureskin(self):
        self.driver.find_element(*self.WHY_CURESKIN_LINK).click()

    def verify_why_cureskin(self, expected_url="https://cureskin.com/why-cureskin/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"

    def click_blog(self):
        self.driver.find_element(*self.BLOG_LINK).click()

    def verify_blog(self, expected_url="https://cureskin.com/blog/"):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f"Expected {expected_url} instead got {actual_url}"

    def click_faqs(self):
        self.driver.find_element(*self.FAQS_LINK).click()

    def verify_faqs(self, expected_faqs_url="https://cureskin.com/faqs/"):
        actual_faqs_url = self.driver.current_url
        assert actual_faqs_url == expected_faqs_url, \
            f"Expected{expected_faqs_url} instead got {actual_faqs_url}"

    def click_refund(self):
        self.driver.find_element(*self.REFUND_LINK).click()

    def verify_refund(self, expected_refund_url="https://shop.cureskin.com/policies/refund-policy"):
        actual_refund_url = self.driver.current_url
        assert actual_refund_url == expected_refund_url, \
            f"Expected{expected_refund_url} instead got {actual_refund_url}"

