import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
def wait(by, selector):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by,selector))
    )



@pytest.fixture(scope="class",autouse=True)
def browser():
    driver = webdriver.Chrome()
 
    yield driver
    driver.close()
    


