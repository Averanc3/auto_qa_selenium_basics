from selenium.webdriver.common.by import By


class CataloguePage:
    GRID_VIEW_BUTTON = (By.ID, "button-grid")
    SORT_BY_LABEL = (By.XPATH, "//label[contains(text(),'Sort By')]")
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, "(//div//button[@type='submit'])[2]")
    LIST_VIEW_BUTTON = (By.ID, "button-list")
    ITEMS_AMOUNT_DROPDOWN = (By.ID, "input-limit")