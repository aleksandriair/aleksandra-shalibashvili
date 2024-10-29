number = int(input("Please enter a natural number larger than 1: "))

result = 0
denominator = 1
counter = 0

while denominator <= 2 * number - 1:
    if counter % 2 == 0:
        result += 1 / denominator
    else:
        result -= 1 / denominator
    denominator +=2
    counter += 1

print(4 * result)

# Wow, we get Pi :)))