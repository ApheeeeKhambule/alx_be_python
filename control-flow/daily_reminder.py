# daily_reminder.py

def main():
    # Prompt user for task details
    task = input("Enter the task description: ")
    priority = input("Enter the priority level (high, medium, low): ")
    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    
    # Process the task based on priority and time sensitivity
    print("Reminder:")
    match priority:
        case 'high':
            print(f"{task} - Priority: {priority.capitalize()}")
            if time_bound == 'yes':
                print("This task requires immediate attention today!")
        case 'medium':
            print(f"{task} - Priority: {priority.capitalize()}")
            if time_bound == 'yes':
                print("This task requires attention soon.")
        case 'low':
            print(f"{task} - Priority: {priority.capitalize()}")
            if time_bound == 'yes':
                print("This task is time-bound but has lower priority.")
        case _:
            print("Invalid priority level entered.")
    
if __name__ == "__main__":
    main()
