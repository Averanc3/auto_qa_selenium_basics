from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.admin_login_page import AdminLoginPage


def test_elements_on_admin_login_page(base_url, browser):
    browser.get(base_url+'administration')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_LABEL))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminLoginPage.USERNAME_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminLoginPage.USERNAME_LABEL))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_BUTTON))