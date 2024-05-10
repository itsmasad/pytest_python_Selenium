import sys
from selenium import webdriver

browser = sys.argv[1]  # Get browser type from command line argument

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()
# Add more browsers as needed

# Your test code here

driver.quit()
