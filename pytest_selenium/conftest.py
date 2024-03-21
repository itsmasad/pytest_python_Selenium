import time
import pytest
from selenium import webdriver

def wait():
    return time.sleep(5)

@pytest.fixture(scope="class",autouse=True)
def browser():
    driver = webdriver.Chrome()
 
    yield driver
    driver.close()


