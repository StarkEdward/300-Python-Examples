# How to read a number n and compute n+nn+nnn

a = int(input("Enter a number: "))
n1 = int(f"{a}")
n2 = int(f"{a}{a}")
n3 = int(f"{a}{a}{a}")
print(n1 + n2 + n3)