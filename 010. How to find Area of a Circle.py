# 010. How to find Area of a Circle
from math import pi

r = float(input("Enter the radius of circle: "))

area_of_circle = round(pi * r**2, 2)

print(f"The area of the Circle is: {area_of_circle}")