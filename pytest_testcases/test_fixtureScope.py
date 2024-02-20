# to read what fixture,session and module is please go to readme file
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def launchbrowser():
    # Make a keyword global so it can be used everywhare
    global driver
    driver = webdriver.Chrome()



# pass the fixture method name in function to pass the data
def test_printUrl(launchbrowser):
    driver.get("https://docs.pytest.org/en/6.2.x/fixture.html")
    print(driver.current_url)