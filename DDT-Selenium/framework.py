import pytest
from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def test_data():
    workbook = load_workbook(filename="DDT-Selenium\\exelsheet\\TestCasesFramework.xlsx")
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming the data starts from row 2
        data.append(row)
    workbook.close()
    return data

@pytest.mark.parametrize("action, data, locator, locator_type", test_data())
def test_excel_actions(browser, action, data, locator, locator_type):
    if action == "Navigate":
        browser.get(data)
    elif action == "Click":
        if locator_type == "class":
            element = browser.find_element(By.CLASS_NAME, locator)
            element.click()
        elif locator_type == "xpath":
            element = browser.find_element(By.XPATH, locator)
            element.click()
    elif action == "Type":
        if locator_type == "class":
            element = browser.find_element(By.CLASS_NAME, locator)
            element.send_keys(data)
        elif locator_type == "xpath":
            element = browser.find_element(By.XPATH, locator)
            element.send_keys(data)
