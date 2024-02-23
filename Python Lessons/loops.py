# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Creating list
people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for Person in people:
    print(f'Current Person: {Person}', ': Simple loop')

# Break
for Person in people:
    if Person == 'Sara':
        break
    print(f'Current Person: {Person}', ': Break in loop')

# Continue will skip the 'Sara'
for Person in people:
    if Person == 'Sara':
        continue
    print(f'Current Person: {Person}', ': Continue loop')

# Range
for i in range(len(people)):
    print(people[i])

# Custom ranges
for i in range(3, 11):
    print(f'Number: {i}')


# While loops execute a set of statements as long as a condition is true.
    
count = 0
while count <= 10:
    print(f'Count : {count}')
    count += 1
    