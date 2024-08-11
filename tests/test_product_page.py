from pages.product_page import ProductPage


def test_elements_on_product_page(base_url, browser):
    browser.get(base_url + 'en-gb/product/macbook')
    product_page = ProductPage(browser)
    product_page.check_elements_on_product_page()
