import random

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    def __init__(self, browser):
        self.browser = browser

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    USERNAME_LABEL = (By.XPATH, "//label[contains(text(), 'Username')]")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_LABEL = (By.XPATH, "//label[contains(text(), 'Password')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGOUT_TXT = (By.XPATH, "//li[@id='nav-logout']//span")
    CATALOGUT_DROPDOWN = (By.XPATH, "//li[@id='menu-catalog']/a")
    ADMIN_PRODUCTS = (By.XPATH, "//li[@id='menu-catalog']/ul/li[2]/a")
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, '//div[@class="float-end"]/a')
    PRODUCT_NAME_INPUT = (By.XPATH, "//input[@id='input-name-1']")
    META_TAG_INPUT = (By.XPATH, "//input[@id='input-meta-title-1']")
    DATA_TAB = (By.XPATH, "//a[@href='#tab-data']")
    MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")
    SEO_TAB = (By.XPATH, "//a[@href='#tab-seo']")
    SEO_INPUT = (By.XPATH, "//input[@id='input-keyword-0-1']")
    SAVE_NEW_PRODUCT_BUTTON = (By.XPATH, '//div[@class="float-end"]/button')
    FILTER_MODEL_INPUT = (By.XPATH, "//input[@placeholder='Model']")
    FILTER_BUTTON = (By.XPATH, ' //button[@id="button-filter"]')
    FILTER_RESULTS_GRID = (By.XPATH, "//tbody/tr")
    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, '//div[@class="float-end"]/a')
    PRODUCT_CHOOSE_ALL_CHECKBOX = (By.XPATH, '//td/input[@type="checkbox"]')
    DELETE_PRODUCTS_BUTTON = (By.CSS_SELECTOR, 'button.btn-danger')
    NO_RESULTS_GRID_TEXT = (By.XPATH, '//td[contains(text(), "No results!")]')

    def admin_login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def check_if_logged_in(self):
        logout_text = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LOGOUT_TXT)).text
        assert logout_text == 'Logout', (f'Пользователь не залогинен или соответствующий признак не отображается'
                                         f'должным образом - {logout_text}')

    def open_products(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CATALOGUT_DROPDOWN)).click()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ADMIN_PRODUCTS)).click()

    def add_new_simple_product(self, product_name: str):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ADD_NEW_PRODUCT_BUTTON)).click()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRODUCT_NAME_INPUT)).send_keys(
            product_name)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.META_TAG_INPUT)).send_keys(
            f"{product_name}+{random.randrange(100, 999)}")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.DATA_TAB)).click()
        model = f"{product_name}_{random.randrange(1, 19)}"
        self.browser.find_element(*self.MODEL_INPUT).send_keys(model)
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SEO_TAB)).click()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SEO_INPUT)).send_keys(
            f"Apple_Microsoft_{random.randrange(1000, 9999)}")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SAVE_NEW_PRODUCT_BUTTON)).click()
        print(model)
        return model

    def search_by_product_model(self, model: str):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FILTER_MODEL_INPUT)).send_keys(
            model)
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FILTER_BUTTON)).click()

    def check_if_one_product_found(self):
        products_found = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.FILTER_RESULTS_GRID))
        assert len(products_found) == 1

    def check_if_no_products_found(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(self.NO_RESULTS_GRID_TEXT))

    def delete_all_products(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRODUCT_CHOOSE_ALL_CHECKBOX)).click()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.DELETE_PRODUCTS_BUTTON)).click()
        Alert(self.browser).accept()

    def check_elements_on_admin_page(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PASSWORD_LABEL))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.USERNAME_LABEL))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
