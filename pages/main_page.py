from selenium.webdriver.common.by import By


class MainPage:
    FEATURE_PRODUCT_ADD_BUTTON = (By.XPATH, "(//div//button[@type='submit'])[1]")
    FEATURE_PRODUCT_LINK = (By.CSS_SELECTOR, "div.product-thumb div.image")
    SHOPPING_CART_LINK = (By.XPATH, "//span[contains(text(),'Shopping Cart')]")
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "input[name='search']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency a")