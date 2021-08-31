import pytest
from requests import request
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Safari


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action = "store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = Chrome(executable_path='/Users/nirbhaysingh/Downloads/chromedriver')
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = Firefox(executable_path='/Users/nirbhaysingh/Downloads/geckodriver')
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "safari":
        driver = Safari()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

