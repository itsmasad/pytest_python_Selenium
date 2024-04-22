# Steel exception occurs when an element on the web page is no
# longer attached to the DOM (Document Object Model) or has become stale.
# Steel exception occurs when something was previously found but later it was not found
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.title
driver.implicitly_wait
parent = driver.current_window_handle
newtab = driver.find_elements(By.XPATH,"//*[@target='_blank']")
newtab[0].click()
child = driver.window_handles
for i in child:
    if i != parent:
        driver.switch_to.window(i)
        time.sleep(3)

driver.switch_to.window(parent)
# it will not be able to relocate this this is why it will send the steel exeption
newtab[0].click()



time.sleep(3)
driver.close()

