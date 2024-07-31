from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.user_registration_page import UserRegistrationPage


def test_elements_on_product_page(base_url, browser):
    browser.get(base_url+'en-gb?route=account/register')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(UserRegistrationPage.LOGIN_PAGE_LINK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(UserRegistrationPage.CONTINUE_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(UserRegistrationPage.FIRSTNAME_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(UserRegistrationPage.NEWSLETTER_CHECKBOX))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(UserRegistrationPage.AGREEMENT_CHECKBOX))