# How to reverse a string in python


def reverse_string(str1):
    return "".join(reversed(str1))

print()
str1 = input("Enter a String: ")
print(reverse_string(str1))