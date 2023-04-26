# define a function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# take input from the user
num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))

