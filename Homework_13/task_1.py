from random import randint

def random_number_generator():
    random_numbers = []
    for i in range (100):
        random_numbers.append(randint(10, 1000000000))
    return random_numbers

def find_shortest(random_numbers):
    shortest_number = min(random_numbers, key = lambda x: len(str(x)))
    return shortest_number

def find_longest(random_numbers):
    longest_number = max(random_numbers, key = lambda x: len(str(x)))
    return longest_number

def sort_ascending(random_numbers):
    numbers_sorted_ascending = sorted(random_numbers, key = lambda x: len(str(x)))
    return numbers_sorted_ascending

def sort_descending(random_numbers):
    numbers_sorted_descending = sorted(random_numbers, key = lambda x: len(str(x)), reverse = True)
    return numbers_sorted_descending

def main():
    random_numbers = random_number_generator()
    shortest_number = find_shortest(random_numbers)
    longest_number = find_longest(random_numbers)
    numbers_sorted_ascending = sort_ascending(random_numbers)
    numbers_sorted_descending = sort_descending(random_numbers)

    print(f"Original list is: {random_numbers}")
    print(f"The shortest number is: {shortest_number}")
    print(f"The longest number is: {longest_number}")
    print(f"The list sorted in ascending order by length: {numbers_sorted_ascending}")
    print(f"The list sorted in descending order by length: {numbers_sorted_descending}")

if __name__ == "__main__":
    main()