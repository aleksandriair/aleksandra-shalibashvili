def is_prime(number):
    prime = True
    i = 2
    while i < number:
        if number % i == 0:
            prime = False
            break
        i += 1
    return prime

print(is_prime(1))
print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(25))
print(is_prime(37))