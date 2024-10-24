# # String Reverse
# old_string = "Hello"
# new_string = old_string[::-1]
# print(new_string)

# import random
# print(random.uniform(0.1,99))

# Checking anagram
# def solution(str1,str2):
#     new1 = sorted(str1.lower())
#     new2 = sorted(str2.lower())
#     if new1==new2:
#         print('Anagram')
#     else:
#         print('Not anagram')

# solution('Silent','Listen')

# lower_Case = "my name is asad and i am a software engineer"
# print(lower_Case.upper())
# print(lower_Case.title())
# print(lower_Case.capitalize())

# input_value = "Abcdad"

# def solution(n):
#     newN = n.lower()
#     seen = []
#     notSeen = []
#     for i in newN:
#         if i in seen:
#             notSeen.append(i)
#         else:
#             seen.append(i)
#     return notSeen

# print(solution(input_value))

# list_number = [0,1,2,3,0,4,0,5,6]
# def solution(n):
#     for i in n:
#         if i == 0:
#             n.remove(i)
#             n.append(i)
#     return n
# print(solution(list_number))

# def reverse_words(input):
#     toList = input.split()
#     reverse = toList[::-1]
#     toString = ' '.join(reverse)
#     print(toString)   

# reverse_words("sky is blue")

# list = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7]

# def numbOnce(input):
#     newList = []
#     for i in input:
#         if input.count(i) == 1:
#             newList.append(i)
#     print(newList)

# numbOnce(list)

# checking how many times the alphbet is there
