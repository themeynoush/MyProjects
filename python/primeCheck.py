# Write a program to check whether a given number is prime or not

# Ask the user to enter a positive integer
num = int(input("Please enter a positive number: "))
is_prime = False

#temp = 0
for i in range(2, num//2):
    if num % i == 0:
        is_prime = True
        break

# Check wheter the number is prime or not
if is_prime:
    print(num, " is not a prime number")
else:
    print(num, " is a prime number")
