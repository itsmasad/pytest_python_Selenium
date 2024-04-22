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
# 
# integer_list = list(str(integer))
# 
# result = map(int, integer_list)
# # getting the sum of the number
# print(sum(result))

# # get the sum of two ingiter
# def solution(n):
#     # converting integer to integer list
#     integer_list = list(str(n))
#     # map(int, integer_list) converts each element of the list into an integer.
#     result = map(int, integer_list)
#     total = sum(result)
#     return total

# result = solution(29)
# assert result == 11, "result is not as expected"

# def piramid(n):
#     for i in range(1,n +1):
#         space = (n-i)*' '
#         asterisk = '*'*(i*2-1)
#         print(space, asterisk)

# piramid(5)

# it will get the value from the left for array a, and from the right for value b
# then concatinating them and comparing if the value is less or greater then variable k
# a = [1,2,3]
# b = [1,2,3]
# k = 31
# def solution(a,b,k):
#     count = 0
#     for value_1,value_2 in zip(a, reversed(b)):
#         concatinated_Value = str(value_1) + str(value_2)
#         if int(concatinated_Value) < 31:
#             print(f'{concatinated_Value} is less than {k}')
#             count += 1
#             # print(i)
#         else:
#             print(f'{concatinated_Value} is not less than {k}')
#     print(count)

# solution(a,b,k)

# # Checking palindrome 
# def check_palindrome(input):
#     # Remove non-alphanumeric characters and convert to lowercase
#     clean_input = ''.join(c.lower() for c in input if c.isalnum())
#     # Check if the cleaned input is equal to its reverse
#     palindrome = clean_input[::-1]
#     if palindrome == clean_input:
#         return "This is palindrome"
#     else:
#         return "This is not a palindrome"
        
# result = check_palindrome("Noon")
# print(result)

# # Fibonacci Series
# fabonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# def check_fab(input):
#     # loop for checking the fabonacci list
#     for i in range(0,len(input)-2):
#         # adding first two digits
#         added = input[i] + input[i+1]
#         # Comparing first two digits to the 3rd one
#         next_num = input[i+2]
#         if added == next_num:
#             return True
#         else:
#             return False
            

# result = check_fab(fabonacci)
# print(result)
# assert True

# # Factorial Calculation
# # Check the factorial of 7
# Examples :
# Factorial of 6:
# 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720
# ----------------------------------
# Factorial of 7:
# 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040
# --------------------------------------
# def solution(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
        
    
# result = solution(7)
# print(result)

# concatinating list and string together

# a = [1,2,3]
# b = "1,2,3"
# def solution(a,b):
#     clean_string = b.replace(',','')
#     clean_string_to_list = list(map(int,clean_string))
#     new_list = a + clean_string_to_list
#     return new_list


# result = solution(a,b)
# print(result)

# if the value of the array is equal to its index print this
# arr = [3,3,5,7,2,5,3]

# def solution(n):
#     for a,b in enumerate(n):
#         if a == b:
#             print(b)

# solution(arr)

# Another way of doing this
# arr = [3,3,5,7,2,5,3]

# def solution(n):
#         for i in range(0,len(n)):
#             if i == n[i]:
#                 print(n[i])

# solution(arr)