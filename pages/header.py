from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class Header(Page):
    ORDERS_CLICK = (By.XPATH, "//a[@id='nav-orders']")
    VISIBLE_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    PRESENT_INPUT_FIELD = (By.ID, 'ap_email')
    CART_ICON_CLICK = (By.ID, 'nav-cart-count')
    EMPTY_CART = (By.CSS_SELECTOR, "span.nav-cart-0")
    NUMBER_ZERO = (By.CSS_SELECTOR, "span.nav-cart-0")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    LOGIN_ICON = (By.CSS_SELECTOR, 'a.header__icon')
    SHOP_ALL_LINK = (By.CSS_SELECTOR, 'a.header__menu-item.header__menu-item--top.list-menu__item.focus-inset')
    SHOPALL_HEADER_LINK = (By.CSS_SELECTOR, 'a.header__menu-item.header__menu-item--top.list-menu__item.focus-inset[href="/collections/all"]')
    BC_SHAMPOO_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/all/products/biotin-collagen-shampoo"]')
    BC_SHAMPOO_TEXT = (By.CSS_SELECTOR, 'h1.h2')
    CC_CREAM_LINK = (By.CSS_SELECTOR, 'a.full-unstyled-link[href="/collections/all/products/ceramide-care-cream"]')
    CC_CREAM_TEXT = (By.CSS_SELECTOR, 'h1.h2')
    FREE_ASSESSMENT = (By.XPATH, "//*[@id='shopify-section-header']/sticky-header/nav/ul/li[5]/a")
    FREE_ASSESSMENT_TEXT = (By.CSS_SELECTOR, 'h1.Fd93Bb.F5UCq.p5VxAd')
    SHOP_CART_ICON = (By.ID, 'cart-icon-bubble')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "h3.mini-cart__empty-text")
    ADD_WHATS_NEW_ITEM = (By.CSS_SELECTOR, 'add-to-cart.w-full.button.button--small')
    SIDEBAR_VIEW_CART_BUTTON = (By.CSS_SELECTOR, 'a.button.button--secondary[href="/cart"]')
    # SIDEBAR_VIEW_CART_BUTTON = (By.XPATH, '//a[contains(@class, "button--secondary") and text()="View cart"]')
    ADDED_ITEM_TEXT = (By.CSS_SELECTOR, 'a.cart-item__name.link')
    MINUS_ICON = (By.CSS_SELECTOR, 'button.quantity__button.no-js-hidden')
    EMPTIED_CART_TEXT = (By.CSS_SELECTOR, 'h2.cart__empty-text')
    def click_orders_menu(self):
        self.click(*self.ORDERS_CLICK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON_CLICK)

    def select_department(self, alias):
        department_dropdown_menu = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dropdown_menu)
        select.select_by_value(f'search-alias={alias}')

    def search_terms_input(self, text, *SEARCH_INPUT_FIELD):
        e = self.driver.find_element(*SEARCH_INPUT_FIELD)
        e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

    def open_cureskin_search(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_login_icon(self):
        self.click(*self.LOGIN_ICON)

    def click_shop_all(self):
        self.find_element(*self.SHOP_ALL_LINK).click()

    def verify_shop_all(self, expected_shop_all_url="https://shop.cureskin.com/collections/all"):
        actual_shop_all_url = self.driver.current_url
        assert actual_shop_all_url == expected_shop_all_url, \
            f"Expected {expected_shop_all_url} instead got {actual_shop_all_url}"

    def click_shopall_header_link(self):
        self.driver.find_element(*self.SHOPALL_HEADER_LINK).click()

    def verify_shopall_header_link(self, expected_shopall_url="https://shop.cureskin.com/collections/all"):
        actual_shopall_url = self.driver.current_url
        assert expected_shopall_url == actual_shopall_url, \
            F"Expected {expected_shopall_url} instead got {actual_shopall_url}"

    def click_bc_shampoo_link(self):
        self.driver.find_element(*self.BC_SHAMPOO_LINK).click()

    def verify_bc_shampoo_text(self, expected_bc_shampoo_text="Biotin & Collagen Shampoo"):
        actual_bc_shampoo_text = self.driver.find_element(*self.BC_SHAMPOO_TEXT).text
        assert actual_bc_shampoo_text == expected_bc_shampoo_text, \
            F"Expected {expected_bc_shampoo_text}, instead got {actual_bc_shampoo_text}"

    def click_cc_cream_text(self):
        self.driver.find_element(*self.CC_CREAM_LINK).click()

    def verify_cc_cream_text(self, expected_cc_cream_text="Ceramide Care Cream"):
        actual_cc_cream_text = self.driver.find_element(*self.CC_CREAM_TEXT).text
        assert expected_cc_cream_text == actual_cc_cream_text, \
            F"Expected {expected_cc_cream_text} instead got {actual_cc_cream_text}"

    def click_free_assessment_button(self):
        self.driver.find_element(*self.FREE_ASSESSMENT).click()

    def verify_free_assessment_nav(self, expected_free_assessment_text="Cureskin: Skin & Hair Experts"):
        sleep(2)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        actual_free_assessment_text = self.driver.find_element(*self.FREE_ASSESSMENT_TEXT).text
        assert expected_free_assessment_text == actual_free_assessment_text, \
            F"Expected {expected_free_assessment_text}, instead got {actual_free_assessment_text}"

    def click_shopping_cart_icon(self):
        self.driver.find_element(*self.SHOP_CART_ICON).click()

    def verify_empty_cart_text(self, expected_sidebar_text="Your cart is currently empty"):
        actual_sidebar_text = self.find_element(*self.EMPTY_CART_TEXT).text
        assert actual_sidebar_text == expected_sidebar_text, \
            F"Expected {expected_sidebar_text}, instead got {actual_sidebar_text}"

    def add_new_item_to_cart(self):
        self.driver.find_element(*self.ADD_WHATS_NEW_ITEM).click()

    def click_sidebar_view_cart(self):
        sleep(2)
        self.driver.find_element(*self.SIDEBAR_VIEW_CART_BUTTON).click()

    def verify_your_cart_navigation(self, expected_cart_url="https://shop.cureskin.com/cart"):
        actual_cart_url = self.driver.current_url
        assert expected_cart_url == actual_cart_url, \
            F"Expected {expected_cart_url}, instead got {actual_cart_url}."

    def verify_item_added(self, expected_item_text="SPF30 Sunscreen"):
        actual_item_text = self.find_element(*self.ADDED_ITEM_TEXT).text
        assert expected_item_text == actual_item_text, \
            F"Expected {expected_item_text}, instead got {actual_item_text}. Added item not verified."

    def click_minus_icon(self):
        self.find_element(*self.MINUS_ICON).click()

    def verify_emptied_cart(self, expected_emptied_text="Your cart is currently empty"):
        sleep(2)
        actual_emptied_text = self.find_element(*self.EMPTIED_CART_TEXT).text
        assert expected_emptied_text == actual_emptied_text, \
            F"Expected {expected_emptied_text}, instead got {actual_emptied_text}."

