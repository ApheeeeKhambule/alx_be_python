# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def check_global_variables():
    """
    Check if global variables are defined correctly.
    """
    if FAHRENHEIT_TO_CELSIUS_FACTOR == 5 / 9:
        print("FAHRENHEIT_TO_CELSIUS_FACTOR is defined correctly.")
    else:
        print("Error: FAHRENHEIT_TO_CELSIUS_FACTOR is not defined correctly.")
    
    if CELSIUS_TO_FAHRENHEIT_FACTOR == 9 / 5:
        print("CELSIUS_TO_FAHRENHEIT_FACTOR is defined correctly.")
    else:
        print("Error: CELSIUS_TO_FAHRENHEIT_FACTOR is not defined correctly.")

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    check_global_variables()
    
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
