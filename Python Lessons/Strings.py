# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# String Formatting
name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (Only available in python 3.6 and after)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

# Capitalize
s = 'hello world'
print(s.capitalize())

# Make all uppercase
s = 'hello world'
print(s.upper())

# Make all lowercase
s = 'hello world'
print(s.lower())

# Swap case
s = 'hello woRld'
print(s.swapcase())

# Get length
s = 'hello woRld'
print(len(s))

# Replace
s = ' hello world'
print(s.replace('world', 'everone'))

# Count how many 'H' in the variable or string
sub = 'h'
print(s.count(sub))

# Starts with will return true or false if the variable is starting with the provided name
s = 'hello woRld'
print(s.startswith('hello'))

# Ends with will do the opposite of starts with
s = 'hello woRld'
print(s.endswith('woRld'))

# Split into a list will convert it into a list which is an arry
s = 'hello woRld'
print(s.split())

# Find position
print(s.find('d'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isalnum())

#Find position

# is all alphanumeric