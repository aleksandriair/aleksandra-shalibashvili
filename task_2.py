from random import uniform

number = int(input("Please enter a natural number larger than 1: "))

i = 0

for _ in range(number):
    a = uniform(0, 1)
    b = uniform (0, 1)
    if (a ** 2 + b ** 2) <= 1:
        i += 1

print(4 * (i / number))

# This is again an approximation of Pi