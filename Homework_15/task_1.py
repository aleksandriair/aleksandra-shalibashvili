from random import randint

def random_number_generator(n):
    numbers = []
    for i in range(n):
        numbers.append(randint(0, 1000))
    return numbers

def count_odds_and_evens(data):
    number_of_evens = 0
    number_of_odds = 0
    for number in data:
        if number % 2 == 0:
            number_of_evens += 1
        else:
            number_of_odds += 1
    return number_of_evens, number_of_odds

def main():
    numbers = random_number_generator(100)
    number_of_evens, number_of_odds = count_odds_and_evens(numbers)
    my_dict = {"even": number_of_evens, "odd": number_of_odds}
    print(f"The list of numbers: {numbers}")
    print(f"The number of even and odd numbers: {my_dict}")

if __name__ == "__main__":
    main()