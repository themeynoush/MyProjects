import math 

def square_root(x):
    sqrt = math.sqrt(x)
    print(f"Squre root of {x} is {sqrt}")


input_str = input("Please enter 5 integers, seperated by commas: ")

# Split the input string into alist of strings using a comma as the seperator
input_list = input_str.split(',')

# convert the list of strings to a llist of integers
my_list = [int(num) for num in input_list]

# Calculate the square root of each number in the list
for num in my_list:
    square_root(num)
