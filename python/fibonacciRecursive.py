def fibonacci_recursive(n):
    if n<= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n -1) + fibonacci_recursive(n -2)
    

# Ask the user to enter the numner of terms
terms = int(input("Please enter the number of terms: "))

if terms<= 0 :
    print("Error! the number of terms must be positive. Please try again!")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci_recursive(i))

    