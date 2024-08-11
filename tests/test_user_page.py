from pages.main_page import MainPage
from pages.user_page import UserPage


def test_elements_on_product_page(base_url, browser):
    browser.get(base_url + 'en-gb?route=account/register')
    user_page = UserPage(browser)
    user_page.check_elements_on_user_page()

