# 028. How to calculate the sum of elements in a list.

num = int(input("How many numbers? : "))
lst = []
for n in range(num):
    numbers = int(input("Enter a number"))
    lst.append(numbers)

print(f"sum of all element in list is {sum(lst)}")