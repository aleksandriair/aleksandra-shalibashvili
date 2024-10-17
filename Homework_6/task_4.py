number = input("Please enter a whole number between 0 and 10: ")

a = float(number)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

number = b

if number <= 0 or number >= 10:
    print("The number must be between 0 and 10")
    exit(1)

i = 0

while i < number:
    j = 1
    while j < i + 2:
        print(j, end = "")
        j += 1
    i += 1
    print()

while i > 1:
    j = 1
    while j < i:
        print(j, end = "")
        j += 1
    i -= 1
    print()