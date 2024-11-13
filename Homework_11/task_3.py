from task_2 import find_gcd_rec

def find_lcm(a, b):
    lcm = (a * b)//find_gcd_rec(a, b)
    return lcm

a = int(input("Please enter a: "))
b = int(input("Please enter b: "))

result = find_lcm(a, b)

print(f"The LCM of {a} and {b} is {result}.")
    