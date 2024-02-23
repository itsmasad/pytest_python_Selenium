# If/ Else conditions are used to decide to do something based on something being true or false


# Comparision Operators (==, !=, >, <, >=, <=) - Used to compare values

x = 7
y = 10

# Simple if

if x > y:
    print(f'{x} is greator then {y}', ': Simple if condition')

# If / Else
    
if x > y:
    print(f'{x} is greator then {y}', ': if else condition')
else:
    print(f'{x} is less then {y}', ': if else condition')

# elif or else / if
if x > y:
    print(f'{x} is greator then {y}', ': elif or else / if condition')
elif x == y:
    print(f'{x} is equal to {y}', ': elif or else / if condition')
else:
    print(f'{x} is less then {y}', ': elif or else / if condition')

# Nasted if
    if x > 2:
        if x <= 10:
          print(f'{x} is greater than 2 and less than or equal to {y}',': Nasted if condition')  


# Logical Operators (and, or, not) - Used to combile conditional statements

# And logical operator
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to {y}',': logical operator (And) condition')  

# Or logical operator
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to {y}',': logical operator (Or) condition')  

# Not logical operator
if not(x == y):
    print(f'{x} is not equal to {y}',': logical operator (Not) condition')  

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1,2,3,4,5,6,7,8,9,10]

z = 7
a = 13
# in
if z in numbers:
    print(z in numbers, ': in condition')

# not in
if a not in numbers:
    print(a not in numbers, ': not in condition')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
    b = 10
    c = 10

    # is
    if b is c:
        print(b is c, ': is condition')

    if x is not y:
        print(b is not c, ': is not condition')