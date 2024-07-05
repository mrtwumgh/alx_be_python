FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32) * celsius
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")

if temperature.isdigit() and unit.lower() == "f":
    temperature = int(temperature)
    celcius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celcius}°C")
elif temperature.isdigit() and unit.lower() == "c":
    temperature = int(temperature)
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")