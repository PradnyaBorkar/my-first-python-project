horus = 24
minutes = 60
seconds = 60


def from_days_to_seconds(my_dictionary):
    units = my_dictionary['units']
    days = int(my_dictionary['days'])
    if units == "hours":
        return f" {days} days are {days * horus} {units} \n"
    elif units == "minutes":
        return f" {days} days are {days * minutes} {units} \n"
    else:
        return " Unsupported unit type \n"


def validate_and_execute(my_dictionary):
    try:
        number_of_days = int(my_dictionary["days"])
        if number_of_days > 0:
            return from_days_to_seconds(my_dictionary)
        elif number_of_days == 0:
            return "Please enter value greater than 0"
        elif number_of_days < 0:
            return "Please enter value positive value"

    except ValueError:
        return f"Error while processing input {min.num_of_day}, Please enter numeric value!!"


message = "Hey user, please provide number of days in comma separated values, for ex: 10,40,23 \n"
