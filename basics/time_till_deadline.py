import datetime

user_input = input("Please enter deadline date \n")
dead_line = datetime.datetime.strptime(user_input, "%d.%m.%Y")
# print(type(dead_line))
# print(dead_line)
remaining_days = dead_line.__sub__(datetime.datetime.today())
print(f"Remaining days for deadline : {remaining_days} \n")
print(f"Remaining days for deadline : {remaining_days.days} \n")
print(f"Remaining hours for deadline : {int( remaining_days.total_seconds()/ 60/60) } \n")
