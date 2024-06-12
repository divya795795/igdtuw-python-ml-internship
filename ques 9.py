# Ask the user for the main string
main_string = input("Please enter the main string: ")

# Ask the user for the substring
substring = input("Please enter the substring to check: ")

# Check if the substring is present in the main string
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
