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
# Original list with duplicate and unique elements
# list = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7]

# # Initialize an empty list to store elements that occur only once
# new_list = []

# # Iterate through each element in the original list
# for num in list:
#     # Check how many times the current element appears in the original list
#     if list.count(num) == 1:
#         # If the count is 1, it means the element occurs only once
#         # Append the element to the new_list
#         new_list.append(num)

# # Print the new_list containing elements that occur only once
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

# integer_list = list(str(integer))

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

# To count how many upper and lower cases are there in a string

# def solution(string):
#     upper = []
#     lower = []
#     for i in string:
#         if i.islower():
#             lower.append(i)
#         else:
#             upper.append(i)
#     return upper,lower

# result = solution("AutomationIsmaAzing")
# print(len(result[0]),len(result[1]),)

# find the first non-repeated character in a string

# string = "aavvdk"

# def solution(input):
#     for char in string:
#         if input.count(char) == 1:
#             print(char)
#             break

# solution(string)


# To get the 5 consecutive number of any number, i.e. 850

# def solution(n):
#     verify = False  # Flag to check if a sequence is found
#     for i in range(1, n+1):  # Iterate over possible starting points of sequences
#         count = 0  # Reset the sum of consecutive numbers for each starting point
#         if not verify:  # If a sequence hasn't been found yet
#             for b in range(i, i+5):  # Iterate over 5 consecutive numbers starting from i
#                 count += b  # Add the current number to the sum
#             if count == n:  # If the sum matches the target number
#                 print(n)  # Print the target number
#                 print(f'{i},{i+1},{i+2},{i+3},{i+4}')  # Print the consecutive sequence
#                 verify = True  # Set the flag to indicate a sequence has been found
#                 break  # Exit the inner loop since the sequence is found
#     if not verify:  # If no sequence is found after checking all possible starting points
#         print("No consecutive sequence found for", n)  # Print a message indicating no sequence was found

# solution(851)

# ----------------------------------------------

# agar palindrom hai
# jitny corrector hein us ka table pr ulta

# agar nahi hai
# jitny corrector hein ussy 5 se  multiply


# string = "mo0om"

# def solution(n):
#     reversed_table = []
#     low = n.lower()
#     low_1 = low[::-1]
#     if low == low_1:
#         print("palindrom hai")
#         table = len(n)
#         for i in range(1,10+1):
#             reversed_table.append(i*table)
            
#     else:
#         print("palindrome nahi hai")
#     for i in reversed(reversed_table):
#         print(i)



# solution(string)

# ---------------------------------------------

# Print every second value in the array
# arr = ["a","b","c","d"]

# for a,b in enumerate(arr):
#     if a % 2 == 0:
#         print(b)

# Another way of doing this
# print(arr[::2])



# ------------------------------------------------------------------

# # How to reverse int value without chaging its datatype
# def solution(n):
#     # Initialize 'new' to 0; this will store the result.
#     new = 0
    
#     # Example initial value: n = 94574645
#     # Loop as long as 'n' is greater than 0.
#     while n > 0:
#         # Get the last digit of 'n' by taking 'n' modulo 10.
#         digit = n % 10  # digit = 5 (94574645 % 10)
        
#         # Shift the current digits in 'new' to the left by multiplying by 10
#         # and add the new digit to the rightmost position.
#         new = new * 10 + digit  # new = 0 * 10 + 5 = 5
        
#         # Remove the last digit from 'n' by doing integer division by 10.
#         n = n // 10  # n = 94574645 // 10 = 9457464
        
#         # Current state:
#         # new = 5, n = 9457464
    
#     # Next iteration:
#     # digit = 9457464 % 10 = 4
#     # new = 5 * 10 + 4 = 54
#     # n = 9457464 // 10 = 945746
#     # Current state:
#     # new = 54, n = 945746
    
#     # Next iteration:
#     # digit = 945746 % 10 = 6
#     # new = 54 * 10 + 6 = 546
#     # n = 945746 // 10 = 94574
#     # Current state:
#     # new = 546, n = 94574
    
#     # Next iteration:
#     # digit = 94574 % 10 = 4
#     # new = 546 * 10 + 4 = 5464
#     # n = 94574 // 10 = 9457
#     # Current state:
#     # new = 5464, n = 9457
    
#     # Next iteration:
#     # digit = 9457 % 10 = 7
#     # new = 5464 * 10 + 7 = 54647
#     # n = 9457 // 10 = 945
#     # Current state:
#     # new = 54647, n = 945
    
#     # Next iteration:
#     # digit = 945 % 10 = 5
#     # new = 54647 * 10 + 5 = 546475
#     # n = 945 // 10 = 94
#     # Current state:
#     # new = 546475, n = 94
    
#     # Next iteration:
#     # digit = 94 % 10 = 4
#     # new = 546475 * 10 + 4 = 5464754
#     # n = 94 // 10 = 9
#     # Current state:
#     # new = 5464754, n = 9
    
#     # Next iteration:
#     # digit = 9 % 10 = 9
#     # new = 5464754 * 10 + 9 = 54647549
#     # n = 9 // 10 = 0
#     # Current state:
#     # new = 54647549, n = 0
    
#     # Print the resulting integer, which is 'new'.
#     print(new)  # Output: 54647549
    
#     # Print the type of 'new' to confirm it's an integer.
#     print(type(new))  # Output: <class 'int'>

# # Example usage: Call the solution function with the integer 94574645.
# solution(94574645)

# ------------------------------------------------------------------

# This is how you can do it with for loop

# var = 94574645
# var2 = len(str(var))
# new = 0

# for i in range(1,var2+1):
#     # Getting the last digit
#     digit = var % 10
#     # Adding the last digit to the new variable
#     new = new * 10 + digit
#     # Removing the last degit from original so we can get the 2nd last in the next iteration
#     var = var // 10

# print(new)

# ---------------------------------------------------------------------------------