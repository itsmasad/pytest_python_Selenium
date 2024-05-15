
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Search(setUp):
    driver = setUp
    driver.get("https://www.google.com/")
    searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")
    searchBox.send_keys("amazone")
    time.sleep(4)
    # results = driver.find_element(By.XPATH,"(//*[@class='lnnVSe'])[1]")
    list_1 = []
    for i in range(1,8):
        xpath = "(//*[@class='lnnVSe'])[{i}]".format(i=i)  # Corrected string formatting
        list_1.append(driver.find_element(By.XPATH, xpath).text)

    print(list_1)