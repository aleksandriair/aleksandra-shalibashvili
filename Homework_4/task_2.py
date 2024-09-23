import random

number = input("Please enter a whole number between 0 and 30: ")

a = float(number)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

number = b

if number <= 0 or number >= 30:
    print("The number must be between 0 and 30")
    exit(1)

print("We are going to print",number,"numbers:")

numbers = []
for i in range(number):
    numbers.append(random.randint(0,1000))

print(numbers)

print("The largest of them is",max(numbers))