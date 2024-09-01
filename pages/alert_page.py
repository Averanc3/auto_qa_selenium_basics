from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccess:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.alert = (WebDriverWait(self.browser, 3).
                      until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))))

    def product_manipulation_success(self):
        self.logger.info("Checking the modifying success message on alert")
        alert_text = self.alert.text
        assert "Success: You have modified products!" in alert_text
