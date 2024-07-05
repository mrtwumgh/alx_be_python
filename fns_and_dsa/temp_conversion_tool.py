FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    fahrenheit = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature.isdigit() and unit.lower() == "f":
    celcius = convert_to_celsius(int(temperature))
    print(f"{temperature}°F is {celcius}°C")
elif temperature.isdigit() and unit.lower() == "c":
    fahrenheit = convert_to_fahrenheit(int(temperature))
    print(f"{temperature}°C is {fahrenheit}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")