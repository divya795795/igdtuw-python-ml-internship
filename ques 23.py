def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask the user for the temperature and the conversion direction
temperature = float(input("Enter the temperature: "))
conversion = input("Convert to (C)elsius or (F)ahrenheit? ").strip().lower()

if conversion == 'c':
    print(f"The temperature in Celsius is: {fahrenheit_to_celsius(temperature):.2f}°C")
elif conversion == 'f':
    print(f"The temperature in Fahrenheit is: {celsius_to_fahrenheit(temperature):.2f}°F")
else:
    print("Invalid conversion direction.")
