# multiplication_table.py

def main():
    # Prompt user to enter a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Print statement for the multiplication table
    print(f"Multiplication Table for {number}:")
    
    # Generate and print the multiplication table using a for loop
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()

