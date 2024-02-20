import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
website = "https://demo.automationtesting.in/Register.html"
driver.get(website)
driver.maximize_window()
driver.implicitly_wait(3)

def wati(by, selector):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by, selector))
    )

action = ActionChains(driver)




wati(By.XPATH, "//*[@placeholder='First Name']")
Fname = driver.find_element(By.XPATH, "//*[@placeholder='First Name']")
action.click(Fname).send_keys("Muhammad").perform()

Fname = driver.find_element(By.XPATH, "//*[@placeholder='Last Name']")
action.click(Fname).key_down(Keys.SHIFT).send_keys("asad").key_up(Keys.SHIFT).perform()

Gender = driver.find_element(By.XPATH, "//*[@value='Male']")
Gender.click()

checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele in checkbox:
    val = ele.get_attribute("value")
    if val == "Cricket":
        ele.click()

list_item = driver.find_elements(By.XPATH, "//li[@class='ng-scope']")

for li in list_item:
    link = li.find_element(By.TAG_NAME, "a")
    print(link.get_attribute("value"))



dropdown = driver.find_element(By.ID, "Skills")
skill_select = Select(dropdown)
skill_select.select_by_value("C")


time.sleep(3)
driver.quit()