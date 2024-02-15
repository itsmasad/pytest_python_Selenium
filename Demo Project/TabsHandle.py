import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Windows.html"
driver.get(website)
driver.maximize_window()

parent = driver.current_window_handle
print(parent)

driver.find_element(By.XPATH, "//button[contains(text(),' click ')]").click()

time.sleep(2)
window = driver.window_handles
print(window)

for win in window:
    if win != parent:
        driver.switch_to.window(win)

driver.find_element(By.XPATH, "//*[contains(text(),'Downloads')]").click()
time.sleep(6)

driver.close()

