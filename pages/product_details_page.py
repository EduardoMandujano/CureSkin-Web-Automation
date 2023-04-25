from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class ProductDetailsPage(Page):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.product-form__submit")

    def open_cureskin_cleansing_gel_prod_details(self):
        self.open_url('https://shop.cureskin.com/products/gentle-cleanse-face-foam?_pos=1&_psq=cleanse&_ss=e&_v=1.0')

    def add_to_cart(self):
        sleep(4)
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()