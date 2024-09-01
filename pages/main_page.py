import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    FEATURE_PRODUCT_ADD_BUTTON = (By.XPATH, "(//div//button[@type='submit'])[1]")
    FEATURE_PRODUCT_LINK = (By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")
    SHOPPING_CART_LINK = (By.XPATH, "//span[contains(text(),'Shopping Cart')]")
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "input[name='search']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency a")
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//div[@class='nav float-end']//div[@class='dropdown']//a")
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")
    REGISTER_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Register')]")
    CURRENT_CURRENCY = (By.XPATH, "//a/strong")
    FEATURE_PRODUCT_NAME = (By.XPATH, '//div[@class="description"]//a')
    FEATURE_PRODUCT_PRICE = (By.XPATH, '//div[@class="description"]//span[@class="price-new"]')

    def click_featured_product(self, index=0):
        feature_product = self.browser.find_elements(*self.FEATURE_PRODUCT_LINK)[index]
        product_name = feature_product.text
        self.logger.info("Click on the featured product")
        feature_product.click()
        return product_name

    def go_to_registration_page(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.MY_ACCOUNT_DROPDOWN)).click()
        self.logger.info("Click on the registration page link")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.REGISTER_PAGE_LINK)).click()

    def switch_currency(self):
        currency_list = ['$', '€', '£']
        current_currency = self.browser.find_element(*self.CURRENT_CURRENCY).text
        currency_list.remove(current_currency)
        self.browser.find_element(*self.CURRENCY_DROPDOWN).click()
        self.logger.info("Click on the random currency option that is not current one")
        self.browser.find_element(By.XPATH, f'//a[contains(text(), "{random.choice(currency_list)}")]').click()
        new_current_currency = self.browser.find_element(*self.CURRENT_CURRENCY).text
        assert new_current_currency != current_currency

    def get_feature_products_name_price(self):
        self.logger.info("Getting the products price")
        product_name = self.browser.find_element(*self.FEATURE_PRODUCT_NAME).text
        product_price = self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text
        return product_name, product_price

    def check_elements_on_main_page(self):
        self.logger.info("Checking elements on the main page")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SHOPPING_CART_LINK))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CURRENCY_DROPDOWN))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SEARCH_TEXT_FIELD))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FEATURE_PRODUCT_LINK))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FEATURE_PRODUCT_ADD_BUTTON))
