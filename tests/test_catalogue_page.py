import allure
from allure_commons.types import Severity

from pages.catalogue_page import CataloguePage
@allure.title('Checking the elements presence on catalogue page')
@allure.severity(severity_level=Severity.NORMAL)
def test_elements_on_catalogue_page(browser, base_url):
    browser.get(base_url + 'en-gb/catalog/desktops')
    catalogue_page = CataloguePage(browser)
    catalogue_page.check_elements_on_catalogue_page()
