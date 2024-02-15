import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://smartradeweb.ticketpeers.com/"
driver.get(website)

def wait(by, selector):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by, selector))
    )

wait(By.CSS_SELECTOR, "a[href='/login']")
driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()


driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("colin@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Colin@12345")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "img[src='/assets/images/settings-icon.png']").click()
driver.find_element(By.CSS_SELECTOR, "img[src='/assets/images/logout-icon.png']").click()


time.sleep(5)
driver.quit()