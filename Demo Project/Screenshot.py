import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

driver.get_screenshot_as_file("C:\\Users\\Asad\\Desktop\\Selenium Projects\\Demo Project\\screenshots\\screenshot.jpeg")

time.sleep(5)
driver.quit()