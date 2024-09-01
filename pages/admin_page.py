import random

import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

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
    DELETE_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button.btn-danger")
    NO_RESULTS_GRID_TEXT = (By.XPATH, '//td[contains(text(), "No results!")]')

    @allure.step("Input name, password and click submit")
    def admin_login(self, username, password):
        self.logger.info("Logging in as admin, %s" % username)
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    @allure.step("Getting the element proving the user is logged in")
    def check_if_logged_in(self):
        self.logger.info("Check if the user is actually logged in")
        logout_text = (
            WebDriverWait(self.browser, 2)
            .until(EC.visibility_of_element_located(self.LOGOUT_TXT))
            .text
        )
        assert logout_text == "Logout", (
            f"Пользователь не залогинен или соответствующий признак не отображается"
            f"должным образом - {logout_text}"
        )

    @allure.step("Opening the catalogue with products")
    def open_products(self):
        self.logger.info("Clicking on the catalog dropdown and products list")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CATALOGUT_DROPDOWN)
        ).click()
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.ADMIN_PRODUCTS)
        ).click()

    @allure.step("Adding the new product")
    def add_new_simple_product(self, product_name: str):
        self.logger.info(
            "Adding the product %s with minimum info on the list" % product_name
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.ADD_NEW_PRODUCT_BUTTON)
        ).click()
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PRODUCT_NAME_INPUT)
        ).send_keys(product_name)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.META_TAG_INPUT)
        ).send_keys(f"{product_name}+{random.randrange(100, 999)}")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.DATA_TAB)
        ).click()
        model = f"{product_name}_{random.randrange(1, 19)}"
        self.browser.find_element(*self.MODEL_INPUT).send_keys(model)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SEO_TAB)
        ).click()
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SEO_INPUT)
        ).send_keys(f"Apple_Microsoft_{random.randrange(1000, 9999)}")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE_NEW_PRODUCT_BUTTON)
        ).click()
        self.logger.info("Getting the full product name generated - %s" % model)
        return model

    @allure.step("Searching by the model of registred product")
    def search_by_product_model(self, model: str):
        self.logger.info("Searching for the product added by the model - %s" % model)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.FILTER_MODEL_INPUT)
        ).send_keys(model)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.FILTER_BUTTON)
        ).click()

    @allure.step("Making sure the searched product is found")
    def check_if_one_product_found(self):
        self.logger.info("Making sure the searching results length = 1")
        products_found = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.FILTER_RESULTS_GRID)
        )
        assert len(products_found) == 1

    @allure.step("Making sure the non-existing product search gave no results")
    def check_if_no_products_found(self):
        self.logger.info("Making sure the searching gave no results")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.NO_RESULTS_GRID_TEXT)
        )

    @allure.step("Deleting all the products from the list")
    def delete_all_products(self):
        self.logger.info("Deleting all the products from the grid")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PRODUCT_CHOOSE_ALL_CHECKBOX)
        ).click()
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.DELETE_PRODUCTS_BUTTON)
        ).click()
        Alert(self.browser).accept()

    @allure.step("Checking visibility of the necessary elements")
    def check_elements_on_admin_page(self):
        self.logger.info("Checking elements on the admin page")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PASSWORD_LABEL)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.USERNAME_LABEL)
        )
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        )
