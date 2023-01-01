# Define the main function
def main():
  # Read the input from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  op = input("Enter an operator (+, -, *, /): ")

  # Perform the operation
  if op == '+':
    result = num1 + num2
  elif op == '-':
    result = num1 - num2
  elif op == '*':
    result = num1 * num2
  elif op == '/':
    result = num1 / num2
  else:
    result = "Invalid operator"

  # Print the result
  print(result)

# Call the main function
main()
