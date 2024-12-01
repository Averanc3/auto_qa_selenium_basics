import allure
import pytest
from datetime import datetime
import logging

from request_models import ProjectTaskRequestBody
from tests.gectaro_http_client import GectaroHttpClient

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.safari.options import Options as SafariOptions



def pytest_addoption(parser):
    parser.addoption("--browser", default="ch", choices=["ch", "ff", "eg", "sf"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url_ui", default="http://192.168.1.77:8081/", help="base url for UI")
    parser.addoption("--url_api", default="https://api.gectaro.com", help="base url for API client")
    parser.addoption("--bv", default='128.0', help="browser version")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="192.168.1.77", help='selenoid')
    parser.addoption("--token", help="token for test API")
    parser.addoption("--execution_type", default='local', choices=['local', 'remote'])



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"


@pytest.fixture(scope="function")
def base_url(request):
    url_ui = request.config.getoption("--url_ui")
    return url_ui


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    logger = logging.getLogger(request.node.name)
    executor_url = f"http://{executor}:4444/wd/hub"
    execution_type = request.config.getoption('--execution_type')

    logging.basicConfig(
        filename=f"logs/{request.node.name}.log",
        format="%(levelname)s %(message)s",
        encoding="utf-8",
        level=log_level,
    )

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.now())
    )

    driver = None


    if browser == "ch":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        if execution_type == 'local':
            driver = webdriver.Chrome(service=Service(), options=options)

    elif browser == "ff":
        options = FFOptions()
        if execution_type == 'local':
            driver = webdriver.Firefox(options=options)

    elif browser == "eg":
        options = ChromeOptions()
        if execution_type == 'local':
            driver = webdriver.Edge(options=options)

    elif browser == "sf":
        options = SafariOptions()


    else:
        raise Exception

    if execution_type == 'remote':

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

    logger.info("===> Test session ended at %s" % datetime.now())
    print("finalize")

    driver.quit()


@pytest.fixture(scope="session")
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url_api")


@pytest.fixture
def client(token, url):
    client = GectaroHttpClient(base_url=url, token=token)
    yield client
    # teardown


@pytest.fixture
def resource(client):
    data = {
        "name": "first_resource",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 80024,
        "type": 1,
        "volume": 5,
    }

    resource_id = client.post_projects_resources(data=data).json()["id"]

    print(f"resource_id: {resource_id}")
    yield resource_id

    client.delete_projects_resources(resource_id)


@pytest.fixture
def resource_request(client, request, resource):
    data = ProjectTaskRequestBody(
        project_tasks_resource_id=resource,
        volume="5",
        cost="5",
        is_over_budget=True,
        needed_at=int(datetime.now().timestamp()),
    )

    request_id = client.post_projects_resource_requests(data=data).json()["id"]
    print(f"request_id: {request_id}")
    yield request_id





@pytest.fixture
def is_over_budget(request):
    return int(request.param)