# Personal Daily Reminder
# Uses Match Case and conditional statements to provide task reminders

# Get user input for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}. Focus on completing this as soon as possible.")
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}. Schedule time to work on this soon.")
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")