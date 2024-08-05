# Examples of various built-in string functions

# isalpha(): Checks if all characters in a string are alphabetic (letters)
string_alpha = "abc"
print(string_alpha.isalpha())  # Output: True

# isdigit(): Checks if all characters in a string are digits
string_digit = "123"
print(string_digit.isdigit())  # Output: True

# isspace(): Checks if all characters in a string are whitespace characters (spaces, tabs, newline)
string_space = " \t\n"
print(string_space.isspace())  # Output: True

# islower(): Checks if all characters in a string are lowercase
string_lower = "abc"
print(string_lower.islower())  # Output: True

# isupper(): Checks if all characters in a string are uppercase
string_upper = "ABC"
print(string_upper.isupper())  # Output: True

# startswith(prefix): Checks if a string starts with the specified prefix
string_start = "Hello, world!"
print(string_start.startswith("Hello"))  # Output: True


# endswith(suffix): Checks if a string ends with the specified suffix
string_end = "Hello, world!"
print(string_end.endswith("world!"))  # Output: True

# split(): Splits a string into a list of substrings based on a delimiter
string_split = "Hello, world!"
print(string_split.split(", "))  # Output: ['Hello', 'world!']

# join(iterable): Concatenates elements of an iterable (like a list) into a single string, using the string as a delimiter
my_list = ["Hello", "world!"]
print(", ".join(my_list))  # Output: Hello, world!

