#greet you through your name and time of the day
name=input("Enter your name: ")
time_of_day=float(input("Enter the time of the day in hours (0-23): "))
if 0 <= time_of_day < 12:
    time_of_day = "morning"
elif 12 <= time_of_day < 16:
    time_of_day = "afternoon"
elif 16 <= time_of_day < 20:
    time_of_day = "evening"
else:
    time_of_day = "night"
print(f"Good {time_of_day}, {name}!")