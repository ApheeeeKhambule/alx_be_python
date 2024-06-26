# match_case_calculator.py

def main():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform calculation based on the chosen operation using match case
    result = match operation:
        case '+':
            num1 + num2
        case '-':
            num1 - num2
        case '*':
            num1 * num2
        case '/':
            if num2 != 0:
                num1 / num2
            else:
                "Division by zero is not allowed."
        case _:
            "Invalid operation"
    
    # Display the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result is {result}")

if __name__ == "__main__":
    main()
