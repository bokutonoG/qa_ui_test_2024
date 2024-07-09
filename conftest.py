import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://chainik.fun/welcome",
        help="url short"
    ),
    parser.addoption("--headless", action="store_true", help="Headless node"),
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="type driver"
    ),


@pytest.fixture(scope="session")
def driver(request, driver_opt=None):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    driver = request.config.getoption("--driver")
    # driver
    options = Options()
    if headless is True:
        options.add_argument("--headless=new")
    # driver
    if driver_opt == "chrome":
        web_driver = webdriver.Chrome(options=options)
    else:
        pass  # and other drivers
    driver.implicitly_wait(10)
    return web_driver, url
