import allure
from allure_commons.types import Severity

from pages.user_page import UserPage


@allure.title("Checking the elements presence on users page")
@allure.severity(severity_level=Severity.MINOR)
def test_elements_on_users_page(base_url, browser):
    browser.get(base_url + "en-gb?route=account/register")
    user_page = UserPage(browser)
    user_page.check_elements_on_user_page()
