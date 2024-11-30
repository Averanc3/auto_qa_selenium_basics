import allure
from allure_commons.types import Severity

from pages.product_page import ProductPage


@allure.title("Checking the elements presence on product page")
@allure.severity(severity_level=Severity.MINOR)
def test_elements_on_product_page(base_url, browser):
    browser.get(base_url + "en-gb/product/macbook")
    product_page = ProductPage(browser)
    product_page.check_elements_on_product_page()
