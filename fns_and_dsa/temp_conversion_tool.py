# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32
CELSIUS_OFFSET = -32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    """
    Main function to handle user input and perform temperature conversion.
    """
    try:
        # Prompt user for temperature and unit
        temp_input = input("Enter the temperature (e.g., 25C or 77F): ").strip()
        
        # Determine the unit and extract the temperature value
        if temp_input[-1].upper() == 'C':
            temp_value = float(temp_input[:-1])
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}C is equivalent to {converted_temp:.2f}F")
        elif temp_input[-1].upper() == 'F':
            temp_value = float(temp_input[:-1])
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}F is equivalent to {converted_temp:.2f}C")
        else:
            raise ValueError("Invalid temperature unit. Please use 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

if __name__ == "__main__":
    main()

