# Tuples in python

# I.e. of a tuple
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)
List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]
print(type(Fruit))
print(type(List_of_Fruit))

# We can modify elements within a list
List_of_Fruit[0] = "Strawberries"
print(List_of_Fruit)
# Can't do the same for a tuple
# Fruit[0] = "Strawberries"
# print(Fruit)

# Slicing tuples
print((Fruit[1:5]))

# Recalling elements in tuples
print(Fruit[0])

# Concatenation of tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuples with one element
x = (5,)  # notation for single element tuple
print(type(x))

# length of a tuple
print(len(Fruit))

# Creating a tuple
tuple_2 = tuple(("Hello", 18, True))
print(type(tuple_2))

# how to append a tuple: converting a tuple to a list and then back to a tuple
Fruit = list(Fruit)
Fruit.append("Pears")
Fruit = tuple(Fruit)
print(Fruit)

# Unpacking tuples
T2 = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, *two, three, four) = Fruit
print(one)
print(two)
print(three)

# loops + tuples
for i in range(3):
    print(T2[i])