import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
website = "https://magento.softwaretestingboard.com/"
driver.get(website)
driver.maximize_window()

# ActionChains - mouse movements, mouse button actions, keypress, and context menu interactions
women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")
women_top = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
women_top_jacket = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")


action = ActionChains(driver)
action.move_to_element(women).perform()
action.move_to_element(women_top).perform()
action.click(women_top_jacket)

time.sleep(3)
driver.quit()