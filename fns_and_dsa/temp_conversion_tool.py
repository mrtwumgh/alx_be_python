FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")

if unit == "F":
    celcius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celcius}°C")

if unit == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")