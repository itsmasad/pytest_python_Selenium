# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select, Keys, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('')

# driver.maximize_window()
# element = driver.find_element(By.CLASS_NAME,'element')
# element.click()
# element.clear()
# driver.title
# driver.current_url
# # screenshot
# driver.save_screenshot()
# # Iframes
# driver.switch_to.frame(element)
# driver.switch_to.frame(0)
# driver.switch_to.default_content()
# # Alerts
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# driver.switch_to.alert.send_keys('Test')
# text = driver.switch_to.alert.text
# element.send_keys("This is Text")
# # Mouse & Keyboard
# action = ActionChains(driver)
# action.move_to_element(element).perform()
# action.click(element).perform()
# action.context_click(element).perform()
# action.click(element).key_down(Keys.TAB).send_keys('This is the content').key_up(Keys.TAB).perform()
# # JavaScript
# driver.execute_script('')

# # Dropdown select
# select = Select(element)
# select.select_by_index(0)
# select.select_by_value('value')
# select.select_by_visible_text('Text')
# select.deselect_by_index(0)
# select.deselect_all()

# # forword back and refresh
# driver.back()
# driver.forward()
# driver.refresh()

# # Window & Tab Handling
# parent = driver.current_window_handle
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.switch_to.window(parent)

# # Waits
# driver.implicitly_wait(4)

# # Explicit Wait
# WebDriverWait(driver,5).until(
#     EC.visibility_of_all_elements_located((By.ID,'Locator'))
# )

# # Fluent Wait
# WebDriverWait(driver,5,2).until(
#     EC.presence_of_element_located((By.TAG_NAME,'Locator'))
# )

import pytest

@pytest.fixture(scope="function")
def setUp():
    print("This is setup")


def test_data():
    data = [
        ("Asad@gmail.com","Asad_Password"),
        ("Naveed@gmail.com","Naveed_Password"),
        ("Uzair@gmail.com","Uzair_password")
    ]
    return data

@pytest.mark.parametrize("username,password",test_data())
def test_Login(username,password):
    print(username,password)