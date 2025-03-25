import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic_info","browser")
    if browser =="chrome":
        driver = webdriver.Chrome()
    elif browser =="edge":
        driver = webdriver.Edge()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    else:
        print("please enter valid browser either - chrome, firefox,edge....")

    driver.implicitly_wait(10)
    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic_info","url")
    driver.get(url)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
