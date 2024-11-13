import random

def generate_random_numbers():
    random_numbers = []
    for _ in range(50):
        random_numbers.append(random.randint(1, 30))
    
    return random_numbers

def remove_duplicates(random_numbers: list):
    new_numbers = []
    for number in random_numbers:
        if number not in new_numbers:
            new_numbers.append(number)

    return new_numbers

def main():
    random_numbers = generate_random_numbers()
    new_numbers = remove_duplicates(random_numbers)
    length = len(new_numbers)
    print(f"Original list - {random_numbers}")
    print(f"List without duplicates - {new_numbers}")
    print(f"Length without duplicates - {length}")

if __name__ == "__main__":
    main()