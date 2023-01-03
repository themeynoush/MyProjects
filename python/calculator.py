# Write a simple calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# Ask the user for the first operand
a = input("Enter the first operand: ")

# Ask the user for the operation they want to perform
operation = input("Enter the operation (+, -, *, /): ")

# Ask the user for the second operand
b = input("Enter the second operand: ")

# Convert the operands to floats
a = float(a)
b = float(b)

# Perform the requested operation
if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)
else:
    print("Invalid operator")

# Print the result
print(result)
