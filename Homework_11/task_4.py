import timeit
from task_2 import find_gcd_ite, find_gcd_rec

def main():
    result = timeit.timeit(lambda: find_gcd_ite(1000, 400), number = 1000)
    print("For iterative method, time passed: ", result)
    result = timeit.timeit(lambda: find_gcd_rec(1000, 400), number=1000)
    print("For recursive method, time passed: ", result)

if __name__ == "__main__":
    main()

# The recursive method is approximately 100 times faster.