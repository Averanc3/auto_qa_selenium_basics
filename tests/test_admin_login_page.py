from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.admin_page import AdminPage
from pages.alert_page import AlertSuccess


def test_elements_on_admin_login_page(browser, base_url):
    browser.get(base_url + 'administration')
    admin_page = AdminPage(browser)
    admin_page.check_elements_on_admin_page()


def test_admin_add_product(browser, base_url):
    browser.get(base_url + 'administration')
    admin_page = AdminPage(browser)
    admin_page.admin_login('user', 'bitnami')
    admin_page.check_if_logged_in()
    admin_page.open_products()
    admin_page.add_new_simple_product('okulus pro')
    alert_success = AlertSuccess(browser)
    alert_success.product_manipulation_success()


def test_admin_delete_product(browser, base_url):
    browser.get(base_url + 'administration')
    admin_page = AdminPage(browser)
    admin_page.admin_login('user', 'bitnami')
    admin_page.check_if_logged_in()
    admin_page.open_products()
    product_model = admin_page.add_new_simple_product('okulus pro')
    alert_success = AlertSuccess(browser)
    alert_success.product_manipulation_success()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.BACK_TO_PRODUCTS_BUTTON)).click()
    admin_page.search_by_product_model(product_model)
    admin_page.check_if_one_product_found()
    admin_page.delete_all_products()
    admin_page.search_by_product_model(product_model)
    admin_page.check_if_no_products_found()
