# How to create a list and tuple with comma separated numbers

values = input("Enter some number separated with comma: ")
list = values.split(",")
new_list = [int(i) for i in list]

tuple = tuple(new_list)

print(new_list)
print(tuple)