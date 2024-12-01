import random
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    FEATURE_PRODUCT_ADD_BUTTON = (By.XPATH, "(//div//button[@type='submit'])[1]")
    FEATURE_PRODUCT_ADD_TO_WISH_LIST = (By.XPATH, "(//div//button[@type='submit'])[2]")
    FEATURE_PRODUCT_LINK = (By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")
    SHOPPING_CART_LINK = (By.XPATH, "//a[contains(@title, 'Shopping Cart')]")
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "input[name='search']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency a")
    MY_ACCOUNT_DROPDOWN = (
        By.XPATH,
        "//div[@class='nav float-end']//div[@class='dropdown']//a",
    )
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")
    REGISTER_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Register')]")
    CURRENT_CURRENCY = (By.XPATH, "//a/strong")
    FEATURE_PRODUCT_NAME = (By.XPATH, '//div[@class="description"]//a')
    FEATURE_PRODUCT_PRICE = (
        By.XPATH,
        '//div[@class="description"]//span[@class="price-new"]',
    )
    SHOPPING_CART_PRODUCT_NAME = (By.XPATH, '//tr/td[2]/a')
    SHOPPING_CART_PRODUCT_PRICE = (By.XPATH, '//tfoot/tr[4]/td[2]')
    SHOPPING_CART_DELETE_PRODUCT = (By.XPATH, '(//button[@type="submit"])[3]')
    SHOPPING_CART_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content"]/p')



    def click_featured_product(self, index=0):
        feature_product = self.browser.find_elements(*self.FEATURE_PRODUCT_LINK)[index]
        product_name = feature_product.text
        self.logger.info("Click on the featured product")
        feature_product.click()
        return product_name

    def go_to_registration_page(self):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.MY_ACCOUNT_DROPDOWN)
        ).click()
        self.logger.info("Click on the registration page link")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.REGISTER_PAGE_LINK)
        ).click()

    def switch_currency(self):
        currency_list = ["$", "€", "£"]
        current_currency = self.browser.find_element(*self.CURRENT_CURRENCY).text
        currency_list.remove(current_currency)
        self.browser.find_element(*self.CURRENCY_DROPDOWN).click()
        self.logger.info("Click on the random currency option that is not current one")
        self.browser.find_element(
            By.XPATH, f'//a[contains(text(), "{random.choice(currency_list)}")]'
        ).click()
        new_current_currency = self.browser.find_element(*self.CURRENT_CURRENCY).text
        assert new_current_currency != current_currency

    def get_feature_products_name_price(self):
        self.logger.info("Getting the products price")
        product_name = self.browser.find_element(*self.FEATURE_PRODUCT_NAME).text
        product_price = self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text
        product_price = re.findall(r'\d+', product_price)
        product_price = int(product_price[0])
        return product_name, product_price


    def go_to_cart_page(self):
        time.sleep(8)
        self.browser.find_element(*self.SHOPPING_CART_LINK).click()
        time.sleep(2)

    def get_shopping_cart_product_name(self):
        time.sleep(1)
        product_in_cart_name = self.browser.find_element(*self.SHOPPING_CART_PRODUCT_NAME).text
        product_in_cart_price = self.browser.find_element(*self.SHOPPING_CART_PRODUCT_PRICE).text
        product_in_cart_price = re.findall(r'\d+', product_in_cart_price)
        if len(product_in_cart_price) > 2:
            product_in_cart_price = int(product_in_cart_price[0]+product_in_cart_price[1])
        else:
            product_in_cart_price = int(product_in_cart_price[0])
        return product_in_cart_name, product_in_cart_price

    def delete_item_added_to_cart(self):
        self.browser.find_element(*self.SHOPPING_CART_DELETE_PRODUCT).click()
        message = self.browser.find_element(*self.SHOPPING_CART_EMPTY_MESSAGE).text
        assert message == 'Your shopping cart is empty!', 'The message is incorrect!'

    def check_elements_on_main_page(self):
        self.logger.info("Checking elements on the main page")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SHOPPING_CART_LINK)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CURRENCY_DROPDOWN)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SEARCH_TEXT_FIELD)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.FEATURE_PRODUCT_LINK)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.FEATURE_PRODUCT_ADD_BUTTON)
        )
