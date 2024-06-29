# daily_reminder.py

def main():
    # Prompt the user to enter task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    
    # Process the task based on priority and time sensitivity
    reminder_message = f"'{task}' is a {priority} priority task"
    
    # Use match-case for priority
    match priority:
        case 'high':
            reminder_message += " that requires"
        case 'medium':
            reminder_message += " that could"
        case 'low':
            reminder_message += " that can"
        case _:
            reminder_message += " that might"
    
    # Check if the task is time-bound
    if time_bound == 'yes':
        reminder_message += " immediate attention today!"
    else:
        reminder_message += ". Consider completing it when you have free time."
    
    # Print the customized reminder message
    print("Reminder:", reminder_message)

if __name__ == "__main__":
    main()
