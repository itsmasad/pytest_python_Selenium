
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get('https://www.google.com')
# driver.implicitly_wait(4)
# driver.find_element(By.XPATH,"xpath").click()
# element = driver.find_element(By.XPATH,"xpath")
# element.click()
# element.clear()
# select = Select(element)
# select.select_by_index()
# select.select_by_value()
# select.select_by_visible_text()
# driver.maximize_window()
# driver.title

# def wait(by,locator):
#     return WebDriverWait(driver,5).until(
#         EC.presence_of_element_located((by,locator))
#     )

# driver.switch_to.frame(element)
# driver.switch_to.default_content()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# driver.switch_to.alert.send_keys()

# driver.save_screenshot('path')
# action = ActionChains(driver)
# action.click(element).perform()
# action.context_click(element).perform()
# action.double_click(element).perform()
# action.drag_and_drop(element,element).perform()
# action.click(element).key_down('Enter').send_keys("This").key_up('Enter').perform()

# driver.back()
# driver.forward()
# driver.refresh()

# handls = driver.window_handles()
# parent = driver.current_window_handle()

# for handle in handls:
#     if handls != parent:
#         driver.switch_to.window(handle)

# driver.switch_to.window(parent)


# driver.get('https://www.google.com')
# driver.back()
# driver.forward()
# driver.refresh()
# element.click()
# element.clear()
# element.send_keys('This is text')

# action.click(element).perform()
# action.click(element).key_down('Enter').send_keys('this is text').key_up('Enter').perform()
# action.context_click()
# action.drag_and_drop(element,element)
# action.move_to_element(element)
# select = Select(element)
# select.select_by_index()
# select.select_by_value()
# select.select_by_visible_text()
# driver.switch_to.alert
# driver.switch_to.frame(0)
# driver.switch_to.window(0)
# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()
# alert.send_keys()
# alert_text = alert.text
# driver.title
# driver.current_url
# driver.window_handles
# driver.current_window_handle
# driver.maximize_window()
# WebDriverWait(driver,5).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME,"locator"))
# )


# time.sleep(3)
