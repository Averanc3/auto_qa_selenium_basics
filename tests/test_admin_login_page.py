from allure_commons.types import Severity
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from pages.admin_page import AdminPage
from pages.alert_page import AlertSuccess

@allure.title('Checking the elements presence on admin page')
@allure.severity(severity_level=Severity.MINOR)
def test_elements_on_admin_login_page(browser, base_url):
    browser.get(base_url + 'administration')
    admin_page = AdminPage(browser)
    admin_page.check_elements_on_admin_page()

@allure.title('Cheking the admin\'s ability to add the new product')
@allure.severity(severity_level=Severity.BLOCKER)
def test_admin_add_product(browser, base_url):
    browser.get(base_url + 'administration')
    admin_page = AdminPage(browser)
    admin_page.admin_login('user', 'bitnami')
    admin_page.check_if_logged_in()
    admin_page.open_products()
    admin_page.add_new_simple_product('dyson')
    if True:
        raise Exception
    alert_success = AlertSuccess(browser)
    alert_success.product_manipulation_success()

@allure.title('Checking the admin\'s ability to delete the product')
@allure.severity(severity_level=Severity.CRITICAL)
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


def test_failure1():
    assert 0
