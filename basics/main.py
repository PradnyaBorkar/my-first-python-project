from calculate_second_in_days import from_days_to_seconds, message

user_input = ""
while user_input != "exit":
    user_input = input(message)
    inputs = user_input.split(":")
    my_dictionary = {"days": inputs[0], "units": inputs[1]}
    print(from_days_to_seconds(my_dictionary))
