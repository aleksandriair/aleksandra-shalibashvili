import random

n = input("Please enter a whole number between 0 and 30: ")

a = float(n)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

n = b

if n <= 0 or n >= 30:
    print("The number must be between 0 and 30")
    exit(1)

print("We are going to print",n,"numbers:")

numbers = []
for i in range(n):
    numbers.append(random.randint(0,1000))

print(numbers)

print("The largest of them is",max(numbers))