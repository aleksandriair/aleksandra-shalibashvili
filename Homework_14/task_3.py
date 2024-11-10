def fibonacci_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b  = b, a + b
        count += 1

def main():
    n = int(input("Please enter a natural number: "))

    print(f"The first {n} numbers in the Fibonacci sequence are: ")
    for number in fibonacci_generator(n):
        print(number, end = " ")

if __name__ == "__main__":
    main()
