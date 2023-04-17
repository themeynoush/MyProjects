# Create a program that generates random passwords of a given length and complexity

import random
import string

def generate_password(length=8, complexity='strong'):
    """
    Generate a random password with the given length and complexity.

    Parameters:
    length (int): The length of the password (default 8).
    complexity (str): The complexity of the password: 'weak', 'medium', or 'strong' (default 'strong').

    Returns:
    A string representing the generated password.
    """

    if complexity == 'weak':
        chars = string.ascii_lowercase
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits
    else: # strong complexity
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=10, complexity='strong')
print(password)
