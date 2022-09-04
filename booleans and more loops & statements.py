# Booleans - stores true and false

# print(True)
# print("True")

# print(type(True)) # This is a bool
# print(type,"True") # This is a string

# Testing if statement is true
# print(5 == 5)
# print(5 == 6)

# Incoporating if statements with a boolean
x = 11
y = 5
if x % y == 0 :
    print(True)
else:
    print(False)

# while loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1

# incorporatnig the else statement within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4")

# if statement
number = 0
if number > 1:
    print("+ve number > 1")
elif number == 0:
    print("0")
else:
    print("-ve number")

# new
number = 1
while  number < 10:
    print(number)
    number = number +1
    if number == 10:
        print("game over")

print(int(input("pick a number")))