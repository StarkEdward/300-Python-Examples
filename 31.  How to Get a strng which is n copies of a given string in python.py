# 31.  How to Get a string which is n copies of a given string in python

def integer_string(str, n):
    result = ""
    for i in range(n):
        result += str

    return result


str = input("Enter a string: ")
n = int(input("How many times you want to repeat: "))
print(integer_string(str, n))