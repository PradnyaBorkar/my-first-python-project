calculation_units = 24 * 60
name_of_units = "seconds"


def from_days_to_seconds(number_of_days):
    return f"{number_of_days} days are {calculation_units * number_of_days} {name_of_units}"


user_input = input("please enter number of days to convert \n")
seconds = from_days_to_seconds(int(user_input))
print(f"{seconds}")
