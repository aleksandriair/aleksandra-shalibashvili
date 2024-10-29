def find_maximum(*args):
    maximum = args[0]
    for i in args:
        if i > maximum:
            maximum = i
        i += 1
    return maximum

print(find_maximum(1, 2, 3))
print(find_maximum(-1000, 100000, 5))
print(find_maximum(0.5, 0.3333, 0.12, 0.997))