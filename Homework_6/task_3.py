number = input("Please enter a whole number between 0 and 10,000: ")

a = float(number)
b = int(a)

if a != b:
    print("The number must be whole")
    exit(1)

number = b

if number <= 0 or number > 10000:
    print("The number must be between 0 and 10,000")
    exit(1)

number = str(number)

i = 0

print("Reversed number is: ", end = "")
while i < len(number):
    print(number[len(number)-i-1],end = "")
    i += 1
print()

i = 0
sum = 0

print("Sum of digits: ", end = "")
while i < len(number):
    sum += int(number[i])
    i += 1
print(sum)