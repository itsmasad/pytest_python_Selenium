import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

# Method 1
driver.get_screenshot_as_file("C:\\Users\\Asad\\Desktop\\Selenium Projects\\Demo Project\\screenshots\\screenshot.jpeg")
# Method 2
driver.save_screenshot("C:\\Users\\Asad\\Desktop\\Selenium Projects\\Demo Project\\screenshots\\screenshot2.jpeg")

time.sleep(5)
driver.quit()