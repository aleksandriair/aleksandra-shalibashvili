import random

n = input("Please enter a whole number between 0 and 20: ")

a = float(n)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

n = b

if n < 0 or n >= 20:
    print("The number must be between 0 and 20")
    exit(1)

if 0 == n:
    print(0)
elif 1 == n:
    print(1)
else:
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    print(b)