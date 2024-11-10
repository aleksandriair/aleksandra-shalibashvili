def find_factorial(number):
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    return factorial

print(find_factorial(5))