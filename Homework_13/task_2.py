from random import randint

list_one = [randint(1, 1000) for x in range(10)]
list_two = [randint(1, 1000) for x in range(10)]
list_three = [randint(1, 1000) for x in range(10)]

sum_list_elements = lambda *args: sum(args)
result = list(map(sum_list_elements, list_one, list_two, list_three))

print(f"List one: {list_one}")
print(f"List two: {list_two}")
print(f"List three: {list_three}")
print(f"Sum of lists: {result}")