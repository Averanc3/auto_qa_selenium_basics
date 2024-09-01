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

    @allure.step('Checking visibility of the necessary elements')
    def check_elements_on_product_page(self):
        self.logger.info("Checking elements on the product page")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SHOPPING_CART_LINK))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRICE_TEXT))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.QUANTITY_INPUT))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.DESCRIPTION_TAB))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SPECIFICATION_TAB))
