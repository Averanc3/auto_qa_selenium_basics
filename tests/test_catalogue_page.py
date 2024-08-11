from pages.catalogue_page import CataloguePage


def test_elements_on_catalogue_page(browser, base_url):
    browser.get(base_url + 'en-gb/catalog/desktops')
    catalogue_page = CataloguePage(browser)
    catalogue_page.check_elements_on_catalogue_page()
