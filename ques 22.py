def find_min_max(numbers):
    return min(numbers), max(numbers)

# Ask the user for a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
min_val, max_val = find_min_max(numbers)
print(f"The minimum value is: {min_val}")
print(f"The maximum value is: {max_val}")
