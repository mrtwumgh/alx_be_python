task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = ""

match priority:
    case "high":
        if time_bound == "yes":
            reminder = "ht"
        elif time_bound == "no":
            reminder = "hnt"
    case "medium":
        if time_bound == "yes":
            reminder = "mt"
        elif time_bound == "no":
            reminder = "mnt"
    case "low":
        if time_bound == "yes":
            reminder = "lt"
        elif time_bound == "no":
            reminder = "lnt"
print()
while True:
    if reminder == "ht" or "mt" or "lt":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        break
    elif reminder == "hnt" or "mnt" or "lnt":
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        break
