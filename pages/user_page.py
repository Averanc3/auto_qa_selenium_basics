import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserPage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    AGREEMENT_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@name='firstname']")
    LASTNAME_INPUT = (By.XPATH, "//input[@name='lastname']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")
    CONTINUE_LINK = (By.XPATH, "//a[contains(text(), 'Continue')]")
    NEWSLETTER_CHECKBOX = (By.ID, "input-newsletter")
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'login page')]")
    LOGIN_INPUT = (By.XPATH, "//input[@id='input-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    CREATION_SUCCESS_MESSAGE = (By.XPATH, "//div[@id='common-success']//h1")
    CHECKOUT_BUTTON = (By.XPATH, '//span[contains(text(), "Checkout")]')

    def login(self, username, password):
        self.logger.info("Logging in, %s" % username)
        self.browser.find_element(*self.LOGIN_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def registration(self, firstname, lastname, password):
        self.logger.info("The new account registration for %s %s" % (firstname, lastname))
        self.browser.find_element(*self.FIRSTNAME_INPUT).send_keys(firstname)
        self.browser.find_element(*self.LASTNAME_INPUT).send_keys(lastname)
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(f"{firstname.replace(' ', '')}_{lastname.replace(' ', '')}@yandex.ru")
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.AGREEMENT_CHECKBOX).click()
        self.browser.find_element(*self.CONTINUE_BUTTON).click()

    def check_registration_success(self):
        self.logger.info("Checking the registration success")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CREATION_SUCCESS_MESSAGE))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON))

    @allure.step('Checking visibility of the necessary elements')
    def check_elements_on_user_page(self):
        self.logger.info("Checking elements on the user page")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LOGIN_PAGE_LINK))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FIRSTNAME_INPUT))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.NEWSLETTER_CHECKBOX))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.AGREEMENT_CHECKBOX))
