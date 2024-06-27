# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task that needs to be completed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task.")
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task that should be completed today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()


