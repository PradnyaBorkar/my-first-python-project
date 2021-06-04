calculation_units = 24 * 60
name_of_units = "seconds"


def from_days_to_seconds(number_of_days):
    return f"{number_of_days} days are {calculation_units * number_of_days} {name_of_units}"


def validate_and_execute():
    try:
        number_of_days = int(num_of_day)
        if number_of_days > 0:
            return from_days_to_seconds(number_of_days)
        elif number_of_days == 0:
            return "Please enter value greater than 0"
        elif number_of_days < 0:
            return "Please enter value positive value"

    except ValueError:
        return f"Error while processing input {num_of_day}, Please enter numeric value!!"


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, please provide number of days in comma separated values, for ex: 10,40,23 \n")
    for num_of_day in user_input.split(","):
        print(validate_and_execute())
