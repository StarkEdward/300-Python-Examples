# How to find average of N numbers in Python.

num = int(input("How many numbers? : "))
total_sum = 0

for n in range(num):
    numbers = float(input(f"Enter {n+1} number : "))
    total_sum += numbers

avg = round(total_sum / num, 2)

print(f"Average is: {avg}")