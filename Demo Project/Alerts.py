import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Alerts.html"
driver.get(website)


driver.find_element(By.ID, "OKTab").click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//*[@href='#CancelTab']").click()
driver.find_element(By.ID, 'CancelTab').click()
time.sleep(2)
driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH, "//*[@href='#Textbox']").click()
driver.find_element(By.XPATH, "//*[@onclick='promptbox()']").click()
driver.switch_to.alert.send_keys("Asad")
driver.switch_to.alert.accept()
time.sleep(3)


driver.quit()
