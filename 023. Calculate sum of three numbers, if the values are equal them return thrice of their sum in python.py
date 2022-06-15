# 023. Calculate sum of three numbers, if the values are equal them return thrice of their sum in python


def calculate_sum(x,y,z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
        return sum

print(calculate_sum(2, 2, 2))