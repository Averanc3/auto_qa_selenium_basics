import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    DESCRIPTION_TAB = (By.XPATH, "//a[contains(text(), 'Description')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@name='quantity']")
    SHOPPING_CART_LINK = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    PRICE_TEXT = (By.XPATH, "//span[@class='price-new']")
    SPECIFICATION_TAB = (By.XPATH, "//a[contains(text(), 'Description')]")
    PRODUCT_NUMBER_INPUT = (By.XPATH, '//input[@id="input-quantity"]')

    @allure.step("Checking visibility of the necessary elements")
    def check_elements_on_product_page(self):
        self.logger.info("Checking elements on the product page")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SHOPPING_CART_LINK)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PRICE_TEXT)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.DESCRIPTION_TAB)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SPECIFICATION_TAB)
        )

    def click_add_to_cart(self, number):
        product_number_input = self.browser.find_element(*self.PRODUCT_NUMBER_INPUT)
        product_number_input.clear()
        product_number_input.send_keys(number)
        self.browser.find_element(*self.SHOPPING_CART_LINK).click()
        time.sleep(1)

