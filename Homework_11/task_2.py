def find_gcd_ite(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def find_gcd_rec(a, b):
    if b == 0:
        return a
    return find_gcd_rec(b, a % b)


def main():
    print("Finding the greatest common denominator of two natural numbers")
    print("1. Iterative method")
    print("2. Recursive method")
    choice = input("Please choose a method (1-2): ")

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if choice == "1":
        result = find_gcd_ite(a, b)
        print(f"GCD of {a} and {b} is {result}.")
    elif choice == "2":
        result = find_gcd_rec(a, b)
        print(f"GCD of {a} and {b} is {result}.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()