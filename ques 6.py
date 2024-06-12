# Define the name of the text file
file_name = "user_input.txt"

# Open the text file in read mode and read its content
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
