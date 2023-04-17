# write a practice program that will translate a message in English into Morse code and then decode it back to English.

# Morse code is a code where each letter of the English alphabet, each digit, and various punctuation characters are represented by a series of dots and dashes.

# Define a dictionary of Morse code mappings
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', 
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', 
    ' ': '/'
}

def text_to_morse(text):
    """
    Convert text to Morse code.

    Parameters:
    text (str): The text to convert.

    Returns:
    A string representing the Morse code for the input text.
    """
    morse = []
    for char in text.upper():
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
    return ' '.join(morse)

def morse_to_text(morse):
    """
    Convert Morse code to text.

    Parameters:
    morse (str): The Morse code to convert.

    Returns:
    A string representing the text for the input Morse code.
    """
    text = []
    for code in morse.split(' '):
        for char, code_str in MORSE_CODE.items():
            if code_str == code:
                text.append(char)
    return ''.join(text)

# Example usage:
text = 'Hello, World!'
morse = text_to_morse(text)
#print(morse)
text_back = morse_to_text(morse)
#print(text_back)

# ask the user to enter a message in English
text = input('Enter a message in English: ')

# convert the message to Morse code
morse = text_to_morse(text)

# display the Morse code
print(morse)

