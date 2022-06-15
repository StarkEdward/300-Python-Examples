# 029. How to find area of triangle

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c) ** 0.5)

print(f"The area is {round(area, 2)}")
