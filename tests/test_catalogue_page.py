from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.catalogue_page import CataloguePage


def test_elements_on_catalogue_page(browser, base_url):
    browser.get(base_url+'en-gb/catalog/desktops')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CataloguePage.SORT_BY_LABEL))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CataloguePage.GRID_VIEW_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CataloguePage.LIST_VIEW_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CataloguePage.ITEMS_AMOUNT_DROPDOWN))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CataloguePage.ADD_TO_WISH_LIST_BUTTON))