import pytest
import logging

from utils.logger import get_logger
from selenium import webdriver
from utils.read_json_data import read_json_file

logger = get_logger(__name__)

# Arrange
@pytest.fixture(scope="session")
def first_entry(request):
    env = request.config.getoption("--env")
    logger.debug("Environment: %s", env)
    browser = request.config.getoption("--browser_type")
    logger.debug("Browser: %s", browser)
    return "a"

# Arrange
@pytest.fixture(scope="class")
def driver():
    if pytest.browser_type == "chrome":
        driver = webdriver.Chrome()
    elif pytest.browser_type == "firefox":
        driver = webdriver.Firefox()
    elif pytest.browser_type == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {pytest.browser_type} is not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(10)

    # clean up
    yield driver

    driver.quit()

@pytest.fixture
def log_test_name(request):
    logger.info("Test name: '%s' started", request.node.name)
    def fin():
        logger.info("Test name: '%s' finished", request.node.name)
    request.addfinalizer(fin)

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(params=["buttons"])
def read_data(request):
    return read_json_file(f"src\\tests\\data\\{request.param}.json")

def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='development', help="Environment where the tests are executed"
    )
    parser.addoption(
        '--browser_type', action='store', default='chrome', help="Browser where the tests are executed"
    )

def pytest_configure(config):
    pytest.env = config.getoption("env")
    pytest.browser_type = config.getoption("browser_type")