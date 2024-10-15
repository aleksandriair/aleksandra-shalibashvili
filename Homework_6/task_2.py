number = input("Please enter a whole number between 0 and 1000: ")

a = float(number)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

number = b

if number <= 0 or number > 1000:
    print("The number must be between 0 and 1000")
    exit(1)

while number > 1:
    print(f"{round(number)} ->", end = " ")
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1

print(1)