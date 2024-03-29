import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(3)

time.sleep(3)

print(driver.title)
print(driver.current_url)


def wait(by, selector):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by,selector))
    )

wait(By.CLASS_NAME,"gLFyf")
search = driver.find_element(By.CLASS_NAME,"gLFyf")
action = ActionChains(driver)
action.click(search).send_keys("MuhammadAsad").perform()
time.sleep(10)
driver.close()