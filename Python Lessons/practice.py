# List
numbers = [1,2,3,4,5]
print(numbers[2])
print(len(numbers))
print(type(numbers))
numbers.append('Mangos')
numbers.remove(numbers[1])
print(numbers)


# Variables
x = 1
y = "two"
z = 2.9
a = True
print(x,y,z,a)

print(f"These are the variables {x,y,z,a}")

# tuple & sets
fruits = ('mango','banana','orange') # Tuple
fruits1 = {'mango','banana','orange'} # Set
print(type(fruits),type(fruits1))

# Loops
for i in range(6):
    print('* '*i)

count = 5
for i in range(count):
    limit = count - i
    print('* ' * limit)

digit = 5
for i in range(digit):
    updated_digit = digit - i
    print(updated_digit * ' ', i * '*')

i = 0
while i <= 10:
    print(i)
    i += 1

# Dictionary
dictionary = {
    'Name' : 'Asad',
    'Age' : '30',
    'Designation' : 'SQA'
}

keys = ['Name','Age','Designation']
for key in keys:
    if key == 'Age':
        continue
    print(dictionary[key])

# Function
def stars():
    print('This is a function')

stars() # Calling function