# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

print(person, type(person))


# User constructor
person2 = dict(first_name='Muhammad',last_name='Asad',age=30)

print(person2, type(person2))

# Get the value
print(person2['first_name'], 'Getting the value')

# Another way to get value using get method
print(person.get('age'), 'getting value with another method')

# Add key value
person['profession'] = 'Worker'
print(person, 'Adding key and value to the dictionary')

# Get dict Keys
print(person.keys(), 'Geting the keys')

# Get dict Values
print(person.values(), 'Getting the values')

# Copy the dict
person = person2.copy()
print(person, 'Copying the dictionary')

# Remove item
del(person['last_name'])
print(person, 'Removing last_name with remove method')

# Another method to remove an item
person.pop('age')
print(person, 'Removing age with pop method')

# Clear the data
person.clear()
print(person, 'Clearing Data')

# Getting length
print(len(person), 'getting the length of the Dictionary')

# List of dict
people = [
    {'name': 'Martha', 'age': 31},
    {'name': 'Addie', 'age': 25}
]
print(people, 'list/Array of dictionary')

# Getting the value from the array of dictionarry
print(people[0]['name'],people[1]['name'], 'getting the values from the array of dictionary')

