# Write a program that asks the user to inter an int and reverse the int

# Ask the user to enter a positive integer number
num = int(input("Please enter a positive integer number:"))

# Reverse the given number
reverse = 0
while num!=0:
    reverse = reverse*10 + num%10
    num = (num//10)

if num == reverse:
    print(num, " is a palindrome number. ")
else:
    print(num, " is not a palindrome number. ")

