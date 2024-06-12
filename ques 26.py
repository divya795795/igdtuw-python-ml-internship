# Ask the user for the string, prefix, and suffix
user_string = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")

# Check for prefix and suffix
starts_with_prefix = user_string.startswith(prefix)
ends_with_suffix = user_string.endswith(suffix)

print(f"Does the string start with '{prefix}'? {starts_with_prefix}")
print(f"Does the string end with '{suffix}'? {ends_with_suffix}")
