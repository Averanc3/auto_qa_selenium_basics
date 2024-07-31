from selenium.webdriver.common.by import By


class UserRegistrationPage:
    AGREEMENT_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@name='firstname']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")
    NEWSLETTER_CHECKBOX = (By.ID, "input-newsletter")
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'login page')]")