from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CataloguePage:

    def __init__(self, browser):
        self.browser = browser

    GRID_VIEW_BUTTON = (By.ID, "button-grid")
    SORT_BY_LABEL = (By.XPATH, "//label[contains(text(),'Sort By')]")
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, "(//div//button[@type='submit'])[2]")
    LIST_VIEW_BUTTON = (By.ID, "button-list")
    ITEMS_AMOUNT_DROPDOWN = (By.ID, "input-limit")

    def check_elements_on_catalogue_page(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SORT_BY_LABEL))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.GRID_VIEW_BUTTON))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LIST_VIEW_BUTTON))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ITEMS_AMOUNT_DROPDOWN))
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ADD_TO_WISH_LIST_BUTTON))
