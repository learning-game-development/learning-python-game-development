# Print out the middle item of this list using an indexgit
planets = ['Mercury', 'Venus', 'Earth']
middle_item_index = int(len(planets)/2)
print(planets[middle_item_index])

# Write a script that displays a multiplication table from 1 * 1 to 10 * 10
for y in range(1, 11):
    for x in range(1, 11):
        print(str(y*x) + " ", end='')
    print(end='\n')

# Use enumerate and the % operator to print every third word in this list
names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
for i, value in enumerate(names, 1):
    if i % 3 == 0:
        print(value)
