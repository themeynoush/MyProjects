# Define the Mad Libs story template
story = "Once upon a time, there was a {adjective} {noun} who loved to {verb} in the {adjective} {noun2}."

# Prompt the user for various parts of speech
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
noun2 = input("Enter another noun: ")

# Use string formatting to fill in the blanks in the story template
filled_in_story = story.format(adjective=adjective, noun=noun, verb=verb, noun2=noun2)

# Print the completed story
print(filled_in_story)
