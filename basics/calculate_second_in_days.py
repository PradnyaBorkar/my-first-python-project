calculation_units = 24 * 60
name_of_units = "seconds"


def from_days_to_seconds(number_of_days):
    return f"{number_of_days} days are {calculation_units * number_of_days} {name_of_units}"


def validate_and_execute():
    if user_input.isdigit():
        number_of_days = int(user_input)
        if number_of_days > 0:
            return from_days_to_seconds(int(user_input))
        elif number_of_days == 0:
            return "Please enter value greater than 0"
        else:
            return "Please enter a positive value"
    else:
        return "Please enter numeric value"


user_input = input("please enter number of days to convert \n")
print(validate_and_execute())
