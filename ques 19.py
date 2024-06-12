import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

# Ask the user for a string input
user_input = input("Enter a string: ")

# Remove punctuation
cleaned_string = remove_punctuation(user_input)

# Print the cleaned string
print(f"The string without punctuation is: {cleaned_string}")
