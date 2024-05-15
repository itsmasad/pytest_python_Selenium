
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Search(setUp):
    driver = setUp
    driver.get("https://www.amazon.com/")
    searchBox = driver.find_element(By.ID, "twotabsearchtextbox")
    searchBox.send_keys("magnesium oil"+ Keys.ENTER)
