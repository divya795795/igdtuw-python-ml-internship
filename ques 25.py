# Ask the user for the source and destination file names
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

# Copy the contents from source to destination
try:
    with open(source_file, "r") as src:
        content = src.read()
    with open(destination_file, "w") as dest:
        dest.write(content)
    print(f"Contents copied from {source_file} to {destination_file}.")
except FileNotFoundError:
    print(f"One of the files, {source_file} or {destination_file}, does not exist.")
