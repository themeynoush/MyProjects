# Write a program that asks the user to enter two numbers and mulitply them together
# Author: Meynoush

# Define the mulitplication number
def multiply_numbers(num1, num2):
    return num1 * num2

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = multiply_numbers(num1, num2)

# Call the function and print the results:
print("The mulitpcation result is: ", result)




