def factorial(n):
    """Calculate the factorial of a given number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Prompt the user to enter a number
    number = int(input("Enter a number to calculate its factorial: "))
    
    # Calculate the factorial using the factorial function
    result = factorial(number)
    
    # Print the result
    print(f"The factorial of {number} is {result}")
