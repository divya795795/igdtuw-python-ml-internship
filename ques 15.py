import csv

# Ask the user for the CSV file name
file_name = input("Enter the CSV file name (with .csv extension): ")

# Read and print the CSV file contents
try:
    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
