import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Register.html"
driver.get(website)
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Muhammad")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Asad")
driver.find_element(By.XPATH, "//*[@value='Male']").click()

checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Clicking all elements
for ele in checkbox:
    val = ele.get_attribute("value")
    ele.click()

    # if val == "Cricket":
    #     ele.click()

# Language Selection
dropdown = driver.find_element(By.ID, "msdd")
languages = driver.find_elements(By.CSS_SELECTOR, "li.ng-scope a")

dropdown.click()
for one in languages:
    one.click()
time.sleep(0.5)

time.sleep(5)
# Selecting value from drop down
dropdown = driver.find_element(By.ID, 'Skills')
select = Select(dropdown)

select.select_by_index(3)

# Going to a different URL
driver.get("https://www.google.com/")

#Printing Current URL
print(driver.current_url)

# Going back
driver.back()

# Refresh page
driver.refresh()

# Going Forward
driver.forward()
time.sleep(5)
driver.quit()