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



# lower_Case = "my name is asad and i am a software engineer"
# # To lower case
# print(lower_Case.lower())
# # To upper case
# print(lower_Case.upper())
# # To Title case
# print(lower_Case.title())
# # To camle case
# print(lower_Case.capitalize())



# Checkin the dublicate alphabets
# def check_dublication(input_value):
#     seen = set()
#     dublicate = set()

#     for char in input_value.lower():
#         if char.isalpha():
#             if char in seen:
#                 dublicate.add(char.upper())
#             else:
#                 seen.add(char)
#     return dublicate

# input_value = "Abcdad"
# print(check_dublication(input_value))

# Move 0 to end of the lis
# list_number = [0,1,2,3,0,4,0,5,6]

# for i in list_number:
#     if i == 0:
#         list_number.remove(i)
#         list_number.append(i)
    
# print(list_number)

# Reversing the alphabets
# def reverse_words(input):
#     # converting the string to list by spliting
#     word = input.split()
#     # reversing the list order
#     reverse = word[::-1]
#     # converting the list to string again
#     new_string = ' '.join(reverse)
#     # printing the new string
#     print(new_string)

# reverse_words("sky is blue")

# if there is number only one time in the list print this
# list = [1,2,2,2,3,3,3,4,5,5,6,6,7]
# new_list = []
# for num in list:
#     if list.count(num)==1:
#         new_list.append(num)

# print(new_list)

# checking how many times the alphbet is there
# mystr = 'a,a,a,b,b,c,c,c'
# stringtolist = mystr.split(",")
# new_list = []
# visited = []
# for i in stringtolist:
#     if i not in visited:
#         visited.append(i)
#         new_list.append(f'{stringtolist.count(i)}:{i}')

# print(new_list)

# integer = 29
# # converting integer to integer list
# integer_list = list(str(integer))
# # map(int, integer_list) converts each element of the list into an integer.
# result = map(int, integer_list)
# # getting the sum of the number
# print(sum(result))

def getting_sum(input):
    two_digit = list(str(input))
    digit_1 = []
    digit_2 = []
    for i in two_digit:
        print(i)
getting_sum(29)