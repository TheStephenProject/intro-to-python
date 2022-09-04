# To create a list use square brackets and manually add data
my_list1 = [1, 2, 3, 4, 5, 6]   # This is a variable and expresses a list, the components 1->6 can represent anything
# to automate list use the list and range functions cooperatively as seen below
# my_list2 = list(range(1, 6))
# my_list3 = list(range(0, 101, 10))
# print(my_list1)
# print(my_list2)
# print(my_list3)
# print(type(my_list1))

# Operations on lists:
# first element in a list is numbered 0
# this returns the 3rd element in my_list1
# print(my_list1[2])
# Gives you the last element,
# print(my_list1[-1])

# let's create a slice from 2nd element to the fourth
# A slice is a piece of a list
# print(my_list1[1:4])
# print(my_list1[-5:-2])

# Length of a list - important for data analysis
# print(len(my_list1))

# Maximum and Minimum of a list
# print(max(my_list1))
# print(min(my_list1))

# Add an element onto our list
my_list1.append(120)  # appends (adds) our chosen element into out list
print(my_list1)

# Reverse a list
my_list1.reverse()
print(my_list1)

# Create another list and sequencing (add) two list together
# my_list2 = [10, 20, 30 ,40, 50, 60]
my_list3 = list(range(10, 70, 10))
print(my_list3)
print(my_list1 + my_list3)
