def sum_of_list(numbers):
    return sum(numbers)

# Ask the user for a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"The sum of the list is: {sum_of_list(numbers)}")
