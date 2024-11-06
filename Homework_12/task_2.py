import random

def generate_random_numbers():
    random_numbers = []
    for _ in range(50):
        random_numbers.append(random.randint(1, 30))
    
    return random_numbers

def rewrite_numbers(random_numbers: list):
    new_numbers = []
    for number in random_numbers:
        for i in range(number):
            new_numbers.append(number)

    return new_numbers

def main():
    random_numbers = generate_random_numbers()
    new_numbers = rewrite_numbers(random_numbers)
    length = len(new_numbers)
    print(f"Original list - {random_numbers}")
    print(f"New list - {new_numbers}")
    print(f"Length of the new list - {length}")

if __name__ == "__main__":
    main()