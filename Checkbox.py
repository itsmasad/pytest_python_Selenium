import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://demoqa.com/text-box"
driver.get(website)

def wait(by, selector):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, selector))
    )

# Call wait() function to wait for the element
wait(By.CSS_SELECTOR, "div[class='element-list collapse show'] li[id='item-1']")

# Find and click on the element

driver.find_element(By.CSS_SELECTOR, "div[class='element-list collapse show'] li[id='item-1']").click()

driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[name()='svg'][1]").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]/button[1]/*[name()='svg'][1]").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[2]/span[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]").click()
time.sleep(5)
driver.quit()