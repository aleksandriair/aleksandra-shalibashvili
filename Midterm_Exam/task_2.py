user_input = input("Please enter a whole number between 10 and 5432: ")

a = float(user_input)
b = int(a)

if a != b:
    print(f"Warning! Please enter a whole number.")
    exit(1)
elif b < 10 or b > 5432:
    print(f"Warning! Please enter a whole number that is between 10 and 5432.")
    exit(1)

number = int(user_input)
result = []

for i in range(1, number):
    if i % 13 == 0:
        result.append(i)
    i += 1

result_count = len(result)

print(f"The divisors of 13 between 1 and {number} are: {result}")
print(f"There are a total of {result_count} divisors.")