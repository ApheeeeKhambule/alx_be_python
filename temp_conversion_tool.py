# temp_conversion_tool.py

# Global variables to store conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_OFFSET = -32

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factors."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, CELSIUS_TO_FAHRENHEIT_OFFSET
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_TO_FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factors."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_TO_CELSIUS_OFFSET
    return (fahrenheit + FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    # Example usage
    celsius_temp = 25
    fahrenheit_temp = 77

    converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temp)
    converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temp)

    print(f"{celsius_temp}°C is {converted_to_fahrenheit:.2f}°F")
    print(f"{fahrenheit_temp}°F is {converted_to_celsius:.2f}°C")

if __name__ == "__main__":
    main()

