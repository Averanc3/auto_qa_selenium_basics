import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


def test_elements_on_main_page(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.SHOPPING_CART_LINK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.CURRENCY_DROPDOWN))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.SEARCH_TEXT_FIELD))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.FEATURE_PRODUCT_LINK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.FEATURE_PRODUCT_ADD_BUTTON))
