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

input_value = "Abcdad"

def solution(n):
    newN = n.lower()
    seen = []
    notSeen = []
    for i in newN:
        if i in seen:
            notSeen.append(i)
        else:
            seen.append(i)
    return notSeen

print(solution(input_value))