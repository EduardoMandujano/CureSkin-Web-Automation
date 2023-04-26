from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class CartPage(Page):

    VIEW_CART_BUTTON = (By.XPATH, "a.button.button--secondary[href='/cart']")
    CART_PRICE_STORAGE = (By.CSS_SELECTOR, "p.totals__subtotal-value")
    PLUS_ICON_BUTTON = (By.CSS_SELECTOR, "button.quantity__button[name='plus']")
    # CART_PRICE_STORAGE = (By.XPATH, "//span[@class='price-item price-item--sale']/price-money/bdi")
    QUANTITY_UPDATED_VALUE = (By.CSS_SELECTOR, "input[value='2']")


    def click_view_cart(self):
        self.driver.find_element(*self.VIEW_CART_BUTTON).click()

    def open_your_cart(self):
        sleep(2)
        self.open_url('https://shop.cureskin.com/cart')

    def storing_the_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, "p.totals__subtotal-value").text
        self.driver.find_element(*self.CART_PRICE_STORAGE)
        print(price)

    def clicking_plus_icon(self):
        self.driver.find_element(*self.PLUS_ICON_BUTTON).click()

    def price_has_doubled(self, expected_price, *locator):
        global product_price
        sleep(2)
        doubled_price = self.driver.find_element(By.CSS_SELECTOR, "p.totals__subtotal-value").text
        self.driver.find_element(*self.CART_PRICE_STORAGE)
        product_price = expected_price
        assert product_price == doubled_price, \
            f'Checking by locator {"p.totals__subtotal-value"}. Expected {expected_price}, but got {doubled_price}'
        print(doubled_price)
        print(expected_price)
        print(product_price)

    def quantity_has_doubled(self, expected_value, *locator):
        value_to_be_verified = self.driver.find_element(*self.QUANTITY_UPDATED_VALUE)
        actual_value = value_to_be_verified.get_attribute("value")
        self.driver.find_element(*self.QUANTITY_UPDATED_VALUE)
        assert expected_value == actual_value, \
            f'Expected {expected_value}, got {actual_value}'
        print(expected_value)
        print(actual_value)




