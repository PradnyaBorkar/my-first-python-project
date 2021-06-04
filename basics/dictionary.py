# dictionary : key value pair
user_input = input("Please enter number of days followed by units to convert for ex 20:hours \n")
inputs = user_input.split(":")
my_dictionary = {"days": inputs[0], "units": inputs[1]}
print(f"{my_dictionary['days']} {my_dictionary['units']}")

my_new_dictionary = {"one": 1, "two": 2, "three": 3}
print(my_new_dictionary)
