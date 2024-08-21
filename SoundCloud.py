import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
Web = "https://www.google.com/"
Search = "Muhammadasad soundcloud"

driver.get(Web)
driver.maximize_window()

# Defining the wait method so it can be used multiple times

def wait_for_element( timeout,By, selector):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By , selector))
    )


wait_for_element(5, By.CLASS_NAME, "gLFyf" )

driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Search + Keys.ENTER)


wait_for_element( 5, By.PARTIAL_LINK_TEXT, "MuhammadAsad")

driver.find_element(By.PARTIAL_LINK_TEXT, "MuhammadAsad").click()

wait_for_element( 5, By.CSS_SELECTOR, "button[id=onetrust-accept-btn-handler]")

driver.find_element(By.CSS_SELECTOR, "button[id=onetrust-accept-btn-handler]").click()

time.sleep(2)
Play_Button = driver.find_elements(By.CSS_SELECTOR, "a.sc-button-play")

if Play_Button:
    Play_Button[0].click()
else:
    print("No button found")

print(Play_Button)
time.sleep(9)
driver.quit()
