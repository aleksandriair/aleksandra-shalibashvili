import random

n = input("Please enter a whole number between 0 and 1000: ")

a = float(n)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

n = b

if n <= 0 or n >= 1000:
    print("The number must be between 0 and 1000")
    exit(1)

for i in range(1, n):
    if n % i == 0:
        print(i,end=" ")

print()