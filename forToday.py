# Join function
listVariable = ['Sky','Is','Blue']
# this will join the list into string with anything defined before the function
joiningListToString = ' '.join(listVariable)
print(joiningListToString)

# Replacing Function
b = "1,2,3"
# This will replace anything from the string you want
clean_string = b.replace(',','')
print(clean_string)
# Can also be used for lists
b = ["hello,", "world", "this,", "is", "a", "test"]
b = [item.replace(',', '') for item in b]
print(b)  # Output: ['hello', 'world', 'this', 'is', 'a', 'test']
