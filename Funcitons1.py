# Functions

# Like in maths, a function takes an argument and returns a result

# general form of a python function:
# def function_name(arguments):
#   {lines telling the function what to do}
#   return result

# Let's consider a function that returns x**2
def squared(x):
    result = x**2
    return result
print(squared(2))  # can recall our function

# multivariable function
def squared (x, y):
    result = x**2 + y**2
    return result
print(squared(3,4))

# new function
def born(country):
    return print("I am from " + country)
born("Nigeria")
