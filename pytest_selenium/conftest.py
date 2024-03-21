import pytest
from selenium import webdriver


@pytest.fixture(scope="class",autouse=True)
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

