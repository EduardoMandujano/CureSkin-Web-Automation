from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Footer(Page):
    ABOUT_US_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/about-cureskin/"]')
    OUR_DOCTORS_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/doctor/"]')
    GRIEVANCE_POLICY_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/grievance-policy/"]')
    WHY_CURESKIN_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/why-cureskin/"]')
    BLOG_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/blog"]')
    FAQS_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="https://cureskin.com/faqs/"]')
    REFUND_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="/policies/refund-policy"]')
    PRIVACY_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="/policies/privacy-policy"]')
    SHIPPING_LINK = (By.CSS_SELECTOR, 'a.link.list-menu__item.list-menu__item--link[href="/policies/shipping-policy"]')
    # FB_LINK = (By.XPATH, "//a[contains(@class, 'list-social__link') and contains(@href, 'facebook.com')]")
    # FB_LINK = (By.CSS_SELECTOR, "a.icon.footer__list-social.list-unstyled.list-social[href='https://www.facebook.com/CureSkinProducts']")
    FB_LINK = (By.XPATH, "//*[@id='shopify-section-popup']/promo-popup/div[2]/ul/li[1]/a")
    TWITTER_LINK = (By.XPATH, '//*[@id="shopify-section-footer"]/footer/div[1]/div/div[2]/div/div[2]/footer-accordion/details/div/ul/li[2]/a')
    INSTA_LINK = (By.XPATH, '//*[@id="shopify-section-footer"]/footer/div[1]/div/div[2]/div/div[2]/footer-accordion/details/div/ul/li[3]/a')
    LINKEDIN_LINK = (By.XPATH, '//*[@id="shopify-section-footer"]/footer/div[1]/div/div[2]/div/div[2]/footer-accordion/details/div/ul/li[4]/a')
    YOUTUBE_ICON = (By.XPATH, '//*[@id="shopify-section-footer"]/footer/div[1]/div/div[2]/div/div[2]/footer-accordion/details/div/ul/li[5]/a')

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

    def click_privacy(self):
        self.driver.find_element(*self.PRIVACY_LINK).click()

    def verify_privacy(self, expected_privacy_url="https://shop.cureskin.com/policies/privacy-policy"):
        actual_privacy_url = self.driver.current_url
        assert actual_privacy_url == expected_privacy_url, \
            f"Expected {expected_privacy_url} instead got {actual_privacy_url}"

    def click_shipping(self):
        self.driver.find_element(*self.SHIPPING_LINK).click()

    def verify_shipping(self, expected_shipping_url="https://shop.cureskin.com/policies/shipping-policy"):
        actual_shipping_policy = self.driver.current_url
        assert actual_shipping_policy == expected_shipping_url, \
            f"Expected {expected_shipping_url} instead got {actual_shipping_policy}"

    def click_fb_icon(self):
        #self.driver.find_element(*self.FB_LINK).click()
        fb_icon = self.find_element(*self.FB_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(fb_icon)
        actions.double_click(fb_icon)
        actions.perform()

    def verify_fb_icon_nav(self, expected_fb_url="https://www.facebook.com/CureSkinProducts"):
        sleep(5)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_fb_url = self.driver.current_url
        assert actual_fb_url == expected_fb_url, \
            F"Expected {expected_fb_url}, instead got {actual_fb_url}"

    def click_twitter_icon(self):
        twitter_icon = self.find_element(*self.TWITTER_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(twitter_icon)
        actions.double_click(twitter_icon)
        actions.perform()

    def verify_twitter_icon_nav(self, expected_twitter_url="https://twitter.com/i/flow/login?redirect_after_login=%2Fcureskinapp"):
        sleep(5)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_twitter_url = self.driver.current_url
        assert actual_twitter_url == expected_twitter_url, \
            F"Expected {expected_twitter_url}, instead got {actual_twitter_url}"

    def click_insta_icon(self):
        insta_icon = self.find_element(*self.INSTA_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(insta_icon)
        actions.double_click(insta_icon)
        actions.perform()

    def verify_insta_icon_nav(self, expected_insta_url="https://www.instagram.com/cureskinapp/"):
        sleep(5)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_insta_url = self.driver.current_url
        assert actual_insta_url == expected_insta_url, \
            F"Expected {expected_insta_url}, instead got {actual_insta_url}"

    def click_linkedin_icon(self):
        linkedin_icon = self.find_element(*self.LINKEDIN_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(linkedin_icon)
        actions.double_click(linkedin_icon)
        actions.perform()

    def verify_linkedin_icon_nav(self, expected_linkedin_url="https://www.linkedin.com/company/cureskin/"):
        sleep(5)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_linkedin_url = self.driver.current_url
        assert actual_linkedin_url == expected_linkedin_url, \
            F"Expected {expected_linkedin_url}, instead got {actual_linkedin_url}"

    def click_youtube_icon(self):
        youtube_icon = self.find_element(*self.YOUTUBE_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(youtube_icon)
        actions.double_click(youtube_icon)
        actions.perform()

    def verify_youtube_icon_nav(self, expected_youtube_url="https://www.youtube.com/c/CureSkin"):
        sleep(5)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_youtube_url = self.driver.current_url
        assert actual_youtube_url == expected_youtube_url, \
            F"Expected {expected_youtube_url}, instead got {actual_youtube_url}"

