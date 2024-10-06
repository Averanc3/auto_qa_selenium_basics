import allure
import pytest
import datetime
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch", choices=["ch", "ff", "eg", "sf"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.1.77:8081/")
    parser.addoption("--bv")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="192.168.1.77")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"


@pytest.fixture(scope="function")
def base_url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    logger = logging.getLogger(request.node.name)
    executor_url = f"http://{executor}:4444/wd/hub"
    logging.basicConfig(
        filename=f"logs/{request.node.name}.log",
        format="%(levelname)s %(message)s",
        encoding="utf-8",
        level=log_level,
    )

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.datetime.now())
    )

    driver = None

    if browser == "ch":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        # driver = webdriver.Chrome(service=Service(), options=options)

    elif browser == "ff":
        options = FFOptions()
        # if headless:
        #     options.add_argument("--headless")
        # driver = webdriver.Firefox(options=options)

    elif browser == "eg":
        options = ChromeOptions()
        # if headless:
        #     options.add_argument("headless=new")
        # driver = webdriver.Edge(options=options)

    elif browser == "sf":
        options = SafariOptions()


    else:
        raise Exception

    capabilities = {
        "browserVersion": version,
        "selenoid:options":{
            "enableVNC": False,
            "enableVideo": False,
            "enableLog": True,
            "name": request.node.name
        }
    }

    for k, v in capabilities.items():
        options.set_capability(k, v)


    logger.info(
        f"Starting on remote url {executor_url}"
    )
    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    driver.set_window_size(1920, 1080)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML,
        )

    logger.info("===> Test session ended at %s" % datetime.datetime.now())
    print("finalize")

    driver.quit()
