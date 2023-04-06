# define a function that prints the alphabet in English in lower case
def englishAlphabet():
    for i in range(97, 123):
        print(chr(i), end=" ")
    print()

# call the function
englishAlphabet()