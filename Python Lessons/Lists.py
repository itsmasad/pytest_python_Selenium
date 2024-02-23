# A List is a collection which is ordered and changeable. Allows duplicate numbers.

#Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Pears', 'Banana']

#Use a constructor
number2 = list((1, 2, 3, 4, 5))

print(numbers, number2)
print(fruits[0])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Banana')
print(fruits)

# Insert into position
fruits.insert(0, 'Strawberries')
print(fruits)

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse the list
fruits.reverse()
print(fruits)

# Sort list (Alphabetically sorting)
fruits.sort()
print(fruits)

# Sorting reverse
fruits.sort(reverse=True)
print(fruits)


print(type(number2))