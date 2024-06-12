from collections import Counter

# Ask the user for a string input
user_input = input("Enter a string: ")

# Count the frequency of each character
char_frequency = Counter(user_input)

# Print the frequency of each character
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")
