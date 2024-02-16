import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Index.html"
driver.get(website)
driver.maximize_window()

# Wait Slee (this is basic python wait)
time.sleep(5)

# Wait Imlicit Wait - Implicitly waiting, WebDriver polls the DOM (Entire Website is a DOM) webpage
# we are telling the Dom to wait for all the web elements in the page 
# Where are not available immediately and need some time to load.
# Mostly use when we load the page or moving/refreshing the new page
driver.implicitly_wait(3)

# Wait Explicit Wait - hey allow your code to halt program execution, or freeze the thread, until the condition you pass it resolves.
# The condition is called with a certain frequency until the timeout of the wait is elapsed.
# Mostly use to wait for a particular element to apear

def Wait(by, selector):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by, selector))
    )

Wait(By.ID, "email")
driver.find_element(By.ID, "email").send_keys("email@gmail.com")

time.sleep(5)
driver.quit()