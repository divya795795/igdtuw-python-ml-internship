from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))
print(f"Your age is: {calculate_age(birth_year)}")
