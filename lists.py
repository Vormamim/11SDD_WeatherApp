
names = ["Alice", "Bob", "Charlie", "David", "Eve"] # a list of names

# Using a for loop
for name in names: # name is a variable that will take on each value in names
    print(name)

# Using a while loop
index = 0
while index < len(names):  # len(names) is the number of elements in names
    print(names[index]) # names[index] is the element at index
    index += 1 # increment index by 1

# Using the built-in function enumerate
for index, name in enumerate(names):# index is the index of the element in names, name is the element
    print(f"{index+1}. {name}") # index+1 is the number of the element in names
