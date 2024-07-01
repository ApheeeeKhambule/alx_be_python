# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        number_of_days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {number_of_days} days: {formatted_future_date}")
    except ValueError:
        print("Error: Please enter a valid integer for number of days.")

# Main function to run the script
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
