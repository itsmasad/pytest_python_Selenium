import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Frames.html"
driver.get(website)
driver.maximize_window()


# Using Index
# driver.switch_to.frame(0)

# Using Name or ID (this is a overloading concept, you can use the ID or Name either)
# driver.switch_to.frame("singleframe") #ID
# driver.switch_to.frame("SingleFrame") #Name

# Using Web Element"

single_frame = driver.find_element(By.XPATH, "//div[@id='Single']/iframe")
driver.switch_to.frame(single_frame) 

driver.find_element(By.TAG_NAME, "input").send_keys("This is Text")

# Comming back to normal window or comming out of iframes
driver.switch_to.default_content()
breakpoint()
time.sleep(5)
driver.quit()