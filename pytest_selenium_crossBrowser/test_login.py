import time
from conftest import wait
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class TestLogin:
    def test_navigate_to_google(self, browser):
        driver.get("https://www.google.com")
        # wait(By.CLASS_NAME,"gLFyf")
        search = driver.find_element(By.CLASS_NAME,"gLFyf")
        search.send_keys("Asad")
        time.sleep(5)