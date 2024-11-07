from random import randint

def random_number_generator():
    random_numbers = []
    for i in range (100):
        random_numbers.append(randint(10, 1000000000))
    return random_numbers

def find_smallest(random_numbers):
    smallest_number = min(random_numbers)
    return smallest_number

def find_largest(random_numbers):
    largest_number = max(random_numbers)
    return largest_number

def sort_ascending(random_numbers):
    numbers_sorted_ascending = sorted(random_numbers)
    return numbers_sorted_ascending

def sort_descending(random_numbers):
    numbers_sorted_descending = sorted(random_numbers, reverse = True)
    return numbers_sorted_descending

def main():
    random_numbers = random_number_generator()
    smallest_number = find_smallest(random_numbers)
    largest_number = find_largest(random_numbers)
    numbers_sorted_ascending = sort_ascending(random_numbers)
    numbers_sorted_descending = sort_descending(random_numbers)

    print(f"Original list is: {random_numbers}")
    print(f"The smallest number is: {smallest_number}")
    print(f"The largest number is: {largest_number}")
    print(f"The list sorted in ascending order: {numbers_sorted_ascending}")
    print(f"The list sorted in descending order: {numbers_sorted_descending}")

if __name__ == "__main__":
    main()