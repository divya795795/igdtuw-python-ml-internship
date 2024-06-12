# Ask the user for a string input
user_input = input("Please enter a string: ")

# Define the name of the text file
file_name = "user_input.txt"

# Open the text file in write mode and write the input string to it
with open(file_name, "w") as file:
    file.write(user_input)

print(f"Your input has been written to {file_name}")
