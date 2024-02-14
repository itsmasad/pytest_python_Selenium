import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

Website = "https://demoqa.com/text-box"

driver.get(Website)

def wait_for_element(by, selector):
     return WebDriverWait(driver, 5).until(
             EC.presence_of_all_elements_located((by, selector))
    )
# time.sleep(10)
wait_for_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[2]/input[1]")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[2]/input[1]").send_keys("Hi")

time.sleep(5)
driver.quit()