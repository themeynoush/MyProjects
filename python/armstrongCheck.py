# Write a program to check whether a number is an armstrong number or not

# Ask the user to enter a positive integer number higher than 11

num = int(input("Please enter a positive integer higher than 11: "))

# Calculate the sum of the digits to the power of the number of the digits using List Comprehension
string = [int(digit) for digit in str(num)]
count = len(string)
sum = sum([digit ** count for digit in string])

# Check whether the given number is armstrong or not
if num == sum:
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")

