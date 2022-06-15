# How to find difference between two numbers.


def difference(num1, num2):
    if num1 <= num2:
        return num2 - num1
    else:
        return (num1-num2) * 2


print(difference(num1= 22, num2= 17))
