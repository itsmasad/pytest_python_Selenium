import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
website = "https://magento.softwaretestingboard.com/women.html"
driver.get(website)
driver.maximize_window()

driver.implicitly_wait(5)
# ActionChains - mouse movements, mouse button actions, keypress, and context menu interactions
women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")
women_top = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
women_top_jacket = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")

# Creating Mouse Click Action Chain
action = ActionChains(driver)
# Hover on women
action.move_to_element(women).perform()
# Hover on Women > Top
action.move_to_element(women_top).perform()
# Clicking on Women > Top > Jacket using action click method
action.click(women_top_jacket).perform()

driver.implicitly_wait(3)

# Initializing the element
search = driver.find_element(By.ID, "search")

# Typing in Search, Pressing shift key, writing text, releasing shift key and then pressing enter.
action.click(search).key_down(Keys.SHIFT).send_keys("asad is my name").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()

time.sleep(3)
driver.quit()