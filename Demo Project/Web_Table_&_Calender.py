import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
website = "https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html"
driver.get(website)
driver.maximize_window()
driver.implicitly_wait

# Describing the date
select_date = "20-Feb-2024"

# # This will split the date from "-"
dates = select_date.split("-")

calender = driver.find_element(By.ID, "datepicker").click()
calender_date = driver.find_elements(By.XPATH, "//*[@data-handler='selectDay']")

for date in calender_date:
    if date.text == dates[0]:
        date.click()


time.sleep(3)


driver.quit()
