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
print(f"{n * ' '}*{n * ' '}")
i = 1
while i < n-1:
    print(f"{(n-i) * ' '}{i * '/'}|{i * '\\'}{(n-i) * ' '}")
    i += 1
print(f"{n * ' '}|{n * ' '}")