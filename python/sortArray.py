# Write a program to asks the user to enter a list off integers 
# and then sorts the list in ascending and then descending order

# Defining a function for implementing bubble ascending sort
def sort_ascending(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j] #Swap elements
    return arr

# Defining a function for implementing bubble descending sort
def sort_descending(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Ask the user to enter the input
input_str = input("Please enter a list of integers seperated by spaces: ")

# Conver the input string to a list of integers
arr = [int(x) for x in input_str.split()]

# Sort the array in ascending order
result = sort_ascending(arr)
print("The ascending sort's result is:\n")
print(result)

# Sort the array in descending order
result = sort_descending(arr)
print("The ascending sort's result is:\n")
print(result)
