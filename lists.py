
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Using a for loop
for name in names:
    print(name)

# Using a while loop
index = 0
while index < len(names):
    print(names[index])
    index += 1

# Using the built-in function enumerate
for index, name in enumerate(names):
    print(f"{index+1}. {name}")
