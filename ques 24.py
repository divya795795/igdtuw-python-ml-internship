# Ask the user for two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ").strip()

# Perform the calculation and print the result
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = None
    print("Invalid operator.")

if result is not None:
    print(f"The result of {num1} {operator} {num2} is: {result}")
