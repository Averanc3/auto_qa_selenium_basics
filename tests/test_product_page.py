from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.product_page import ProductPage


def test_elements_on_product_page(base_url, browser):
    browser.get(base_url+'en-gb/product/macbook')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.SHOPPING_CART_LINK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.PRICE_TEXT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.QUANTITY_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.DESCRIPTION_TAB))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.SPECIFICATION_TAB))