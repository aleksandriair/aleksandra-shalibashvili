j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f"{i} * {j} = {i * j:<2d}", end="    ")
        i += 1
    print()
    j += 1