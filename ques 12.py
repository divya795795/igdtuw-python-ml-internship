def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Ask the user for a number
number = int(input("Enter a number: "))
print(f"The sum of the digits of {number} is: {sum_of_digits(number)}")
