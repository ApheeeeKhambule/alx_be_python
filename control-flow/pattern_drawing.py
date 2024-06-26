# pattern_drawing.py

def main():
    # Prompt user to enter the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Initialize variables
    row = 0
    
    # Draw the pattern using while loop and nested for loop
    while row < size:
        for column in range(size):
            print("*", end="")
        print()  # Move to the next line after each row is printed
        row += 1

if __name__ == "__main__":
    main()
