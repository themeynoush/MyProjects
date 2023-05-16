# write a program that prints out the text entered by the user
# the program should print out the text in a list

text = []
#ask the user to enter a text
text.append(input('Enter a text: '))
#ask the user to enter another text
text.append(input('Enter another text: '))

for charachter in text:
    print(charachter)
