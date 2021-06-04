# list of months
"""multi line
comments"""
months = ["January", "February", "March", "April", "May"]
print(months)
months.append("August")
print(months.sort())
months.remove("March")
print(months)
# date = input("Please enter you birthdate\n")
# print(f"Your birthday is on {date} May")

# set: unique ele unordered
list_1 = ["one", "two", "three", "two"]
set_from_list = set(list_1)
print(set_from_list)

my_set = {"a", "b", "c", "a"}
for ele in my_set:
    print(f"{ele}\n")

my_set.add("d")
print(my_set)
