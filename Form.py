import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

Website = "https://demoqa.com/text-box"

driver.get(Website)

def wait_for_element(by, selector):
     return WebDriverWait(driver, 10).until(
             EC.presence_of_all_elements_located((by, selector))
    )
# time.sleep(10)
wait_for_element(By.CSS_SELECTOR, "input#userName")
input_username = driver.find_element(By.CSS_SELECTOR, "input#userName")
input_email = driver.find_element(By.CSS_SELECTOR, "input#userEmail")
input_address = driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress") 
input_pAddress = driver.find_element(By.CSS_SELECTOR, "textarea#permanentAddress") 
input_submit = driver.find_element(By.CSS_SELECTOR, "button#submit")

input_username.send_keys("Asad")
input_email.send_keys("Asad@email.com")
input_address.send_keys("This is my address")
input_pAddress.send_keys("This is my perminent address")
input_submit.click()


time.sleep(5)
driver.quit()
