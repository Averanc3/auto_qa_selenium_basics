import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ch", "ff", "eg"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--url", default='http://192.168.1.77:8080/'
    )


@pytest.fixture(scope='function')
def base_url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None

    if browser_name == "ch":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=Service(), options=options)

    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "eg":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(options=options)

    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()
