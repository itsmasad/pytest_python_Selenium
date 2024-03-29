# Checking if the number is divisible by 10
# for i in range(1, 100):
#     if i % 10 == 0:
#         print(i)

# String Reverse
# old_string = "Hello"
# new_string = old_string[::-1]
# print(new_string)


# import random
# # Random Numbers
# random_number = random.randint(0,100)
# print(random_number)

# random_fload = random.random()
# print(random_fload)

# random_range = random.uniform(0.2,0.9)
# print(random_range)

# Checking Anagram Function
# def is_anagram(str1, str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()

#     return sorted(str1) == sorted(str2)

# word1 = "silent"
# word2 = "listen"

# if is_anagram(word1,word2):
#     print("It is an anagram")
# else:
#     print("not an anagram")



# import pytest

# @pytest.fixture(scope="function")
# def setUp():
#     print("This is setup")


# def test_data():
#     data = [
#         ("Asad@gmail.com","Asad_Password"),
#         ("Naveed@gmail.com","Naveed_Password"),
#         ("Uzair@gmail.com","Uzair_password")
#     ]
#     return data

# @pytest.mark.parametrize("username,password",test_data())
# def test_Login(username,password):
#     print(username,password)

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# driver = webdriver.Chrome()
# element = driver.find_element(By.CLASS_NAME,"Class")
# element2 = driver.find_element(By.XPATH,"Xpath")
# action = ActionChains(driver)
# action.context_click(element).perform()
# action.move_to_element(element).perform()
# action.click(element).send_keys("Whatever you want to type").perform()
# action.drag_and_drop(element,element2).perform
# driver.switch_to.window()



lower_Case = "my name is asad and i am a software engineer"
# To lower case
print(lower_Case.lower())
# To upper case
print(lower_Case.upper())
# To Title case
print(lower_Case.title())
# To camle case
print(lower_Case.capitalize())
