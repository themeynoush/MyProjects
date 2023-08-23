# Ask the user how many Fibonacci numbers to generate
num_terms = int(input("How many Fibonacci numbers do you want? "))

# The first two terms of the Fibonacci series
first_term = 0
second_term = 1

# Print the first two terms
print("Fibonacci Series: ")
print(first_term)
print(second_term)

# Generate the remaining terms iteratively
for i in range(num_terms -2):
    next_term = first_term + second_term
    print(next_term)

    # Update the terms for the next iteration
    first_term = second_term
    second_term = next_term