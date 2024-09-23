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

c = 0
d = 1

count = 0 
while count <= n:
    print(f"{c}", end = " ")
    c, d = d, c + d
    count += 1
print()