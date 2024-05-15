import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class",params=["chrome", "firefox", "edge"])
def setUp(request):

    # To run this code from command line browser specific you can use this command
    # pytest -v -s Pytest_Amazon\test_AmazonSearch.py -k "chrome"

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    # driver = webdriver.Chrome()


    yield driver
    time.sleep(3)
    driver.quit()