from selenium.webdriver.common.by import By


class ProductPage:
    DESCRIPTION_TAB = (By.XPATH, "//a[contains(text(), 'Description')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@name='quantity']")
    SHOPPING_CART_LINK = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    PRICE_TEXT = (By.XPATH, "//span[@class='price-new']")
    SPECIFICATION_TAB = (By.XPATH, "//a[contains(text(), 'Description')]")