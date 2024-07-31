from selenium.webdriver.common.by import By


class AdminLoginPage:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    USERNAME_LABEL = (By.XPATH, "//label[contains(text(), 'Username')]")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_LABEL = (By.XPATH, "//label[contains(text(), 'Password')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")