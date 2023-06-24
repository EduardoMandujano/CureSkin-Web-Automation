from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class ProductDetailsPage(Page):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.product-form__submit")
    SHOP_BY_FACE_LINK = (By.CSS_SELECTOR, "a.card-wrapper.card.card--media[href='/collections/face']")
    HYD_GEL_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/hydration-gel"]')
    FACE_FOAM_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/gentle-cleanse-face-foam"]')
    SPF30_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/sunscreen-spf-30"]')
    CERAMIDE_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/ceramide-care-cream"]')
    SPF50_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/mineral-sunscreen"]')
    SENSITIVE_CLEANSER_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/sensitive-pro-cleanser"]')
    UNDEREYE_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/under-eye-gel"]')
    KOJIC_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/face/products/kojic-plus-cream"]')
    SHOP_BY_HAIR_LINK = (By.CSS_SELECTOR, "a.card-wrapper.card.card--media[href='/collections/hair']")
    SHAMPOO_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/hair/products/biotin-collagen-shampoo"]')
    HAIR_SOLUTION_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/hair/products/hair-pro-solution"]')
    HAIR_CONDITIONER_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/hair/products/hair-conditioner"]')
    HAIR_SERUM_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/hair/products/smooth-shine-serum"]')
    SHOP_BY_BODY_LINK = (By.CSS_SELECTOR, 'a.card-wrapper.card.card--media[href="/collections/body"]')
    RESTRUCTURE_CREAM_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/body/products/restructure-cream"]')

    def open_cureskin_cleansing_gel_prod_details(self):
        self.open_url('https://shop.cureskin.com/products/gentle-cleanse-face-foam?_pos=1&_psq=cleanse&_ss=e&_v=1.0')

    def add_to_cart(self):
        sleep(4)
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def shop_by_face(self):
        self.driver.find_element(*self.SHOP_BY_FACE_LINK).click()

    def click_hyd_gel(self):
        self.driver.find_element(*self.HYD_GEL_LINK).click()

    def verify_hydration_gel(self, expected_hyd_gel_url="https://shop.cureskin.com/collections/face/products/hydration-gel"):
        actual_hyd_gel_url = self.driver.current_url
        assert actual_hyd_gel_url == expected_hyd_gel_url, \
            f"Expected {expected_hyd_gel_url} instead got {actual_hyd_gel_url}"

    def click_face_foam(self):
        self.driver.find_element(*self.FACE_FOAM_LINK).click()

    def verify_face_foam(self, expected_foam_url="https://shop.cureskin.com/collections/face/products/gentle-cleanse-face-foam"):
        actual_foam_url = self.driver.current_url
        assert expected_foam_url == actual_foam_url, \
            f"Expected {expected_foam_url} instead got {actual_foam_url}"

    def click_spf30(self):
        self.driver.find_element(*self.SPF30_LINK).click()

    def verify_spf30(self, expected_spf30_url="https://shop.cureskin.com/collections/face/products/sunscreen-spf-30"):
        actual_spf30_url = self.driver.current_url
        assert expected_spf30_url == actual_spf30_url, \
            f"Expected {expected_spf30_url} instead got {actual_spf30_url}"

    def click_ceramide(self):
        self.driver.find_element(*self.CERAMIDE_LINK).click()

    def verify_ceramide(self, expected_ceramide_url="https://shop.cureskin.com/collections/face/products/ceramide-care-cream"):
        actual_ceramide_url = self.driver.current_url
        assert actual_ceramide_url == expected_ceramide_url, \
            f"Expected {expected_ceramide_url} instead got {actual_ceramide_url}"

    def click_spf50(self):
        self.driver.find_element(*self.SPF50_LINK).click()

    def verify_spf50(self, expected_sfp50_url="https://shop.cureskin.com/collections/face/products/mineral-sunscreen"):
        actual_spf50_url = self.driver.current_url
        assert actual_spf50_url == expected_sfp50_url, \
            F"Expected {expected_sfp50_url} instead got {actual_spf50_url}"

    def click_sensitive_cleanser(self):
        self.driver.find_element(*self.SENSITIVE_CLEANSER_LINK).click()

    def verify_sensitive_cleanser(self, expected_sensitive_cl_url="https://shop.cureskin.com/collections/face/products/sensitive-pro-cleanser"):
        actual_sensitive_cl_url = self.driver.current_url
        assert actual_sensitive_cl_url == expected_sensitive_cl_url,\
            F"Expected {expected_sensitive_cl_url} instead got {actual_sensitive_cl_url}"

    def click_undereye(self):
        self.driver.find_element(*self.UNDEREYE_LINK).click()

    def verify_undereye(self, expected_undereye_url="https://shop.cureskin.com/collections/face/products/under-eye-gel"):
        actual_undereye_url = self.driver.current_url
        assert actual_undereye_url == expected_undereye_url, \
            F"Expected {expected_undereye_url} instead got {actual_undereye_url}"

    def click_kojic(self):
        self.driver.find_element(*self.KOJIC_LINK).click()

    def verify_kojic(self, expected_kojic_url="https://shop.cureskin.com/collections/face/products/kojic-plus-cream"):
        actual_kojic_url = self.driver.current_url
        assert actual_kojic_url == expected_kojic_url, \
            F"Expected {expected_kojic_url} instead got {actual_kojic_url}"

    def click_on_hair(self):
        self.driver.find_element(*self.SHOP_BY_HAIR_LINK).click()

    def click_shampoo(self):
        self.driver.find_element(*self.SHAMPOO_LINK).click()

    def verify_shampoo(self, expected_shampoo_url="https://shop.cureskin.com/collections/hair/products/biotin-collagen-shampoo"):
        actual_shampoo_url = self.driver.current_url
        assert actual_shampoo_url == expected_shampoo_url, \
            F"Expected {expected_shampoo_url} instead got {actual_shampoo_url}"

    def click_hair_solution(self):
        self.driver.find_element(*self.HAIR_SOLUTION_LINK).click()

    def verify_hair_solution(self, expected_hair_sol_url="https://shop.cureskin.com/collections/hair/products/hair-pro-solution"):
        actual_hair_sol_url = self.driver.current_url
        assert expected_hair_sol_url == actual_hair_sol_url, \
            F"Expected {expected_hair_sol_url} instead got {actual_hair_sol_url}"

    def click_hair_conditioner(self):
        self.driver.find_element(*self.HAIR_CONDITIONER_LINK).click()

    def verify_hair_conditioner(self, expected_conditioner_url="https://shop.cureskin.com/collections/hair/products/hair-conditioner"):
        actual_conditioner_url = self.driver.current_url
        assert expected_conditioner_url == actual_conditioner_url, \
            F"Expected {expected_conditioner_url} instead got {actual_conditioner_url}"

    def click_on_serum(self):
        self.driver.find_element(*self.HAIR_SERUM_LINK).click()

    def verify_hair_serum(self, expected_hair_serum_url="https://shop.cureskin.com/collections/hair/products/smooth-shine-serum"):
        actual_hair_serum_url = self.driver.current_url
        assert actual_hair_serum_url == expected_hair_serum_url, \
            F"Expected {expected_hair_serum_url} instead got {actual_hair_serum_url}"

    def click_on_body(self):
        self.driver.find_element(*self.SHOP_BY_BODY_LINK).click()

    def click_restructure_cream(self):
        self.driver.find_element(*self.RESTRUCTURE_CREAM_LINK).click()

    def verify_restructure_cream(self, expected_rest_cream_url="https://shop.cureskin.com/collections/body/products/restructure-cream"):
        actual_rest_cream_url = self.driver.current_url
        assert actual_rest_cream_url == expected_rest_cream_url, \
            F"Expected {expected_rest_cream_url}, instead got {actual_rest_cream_url}"