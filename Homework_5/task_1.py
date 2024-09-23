n = input("Please enter a whole number between 0 and 50: ")

a = float(n)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

n = b

if n <= 0 or n >= 50:
    print("The number must be between 0 and 50")
    exit(1)

i = 1
while i <= n:
    print(f"{i} —", end="")
    count = 0
    m = 1
    while m <= i and count < 3:
        if i % m == 0:
            print(f" {m}", end = "")
            count += 1
        m += 1
    print()
    i += 1