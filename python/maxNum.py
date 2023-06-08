# Write a program that asks the user to enter a list of numbers and prints the maximum value
# Author: Meynoush

# Ask the user to enter a list of numbers
num_list = input("Enter a list of numbers, separated by spaces: ")

# split the input string into a list of numbers
numbers = num_list.split()

# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers]

# Find the maximum number using max() function
maximum = max(numbers)

# Print the maximum number
print("The maximum number is: ", maximum)


