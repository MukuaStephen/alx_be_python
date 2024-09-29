task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Define the reminder message
reminder = f"'{task}' is a {priority} priority task"

# Process the priority using match-case
match priority:
    case "high":
        reminder += " that requires your immediate attention."
    case "medium":
        reminder += " that you should try to complete soon."
    case "low":
        reminder += " that can be completed when you have free time."
    case _:
        reminder += " with an unknown priority level."

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " No urgent time constraints."

# Output the reminder
print(f"Reminder: {reminder}")