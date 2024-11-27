def find_midpoint(x1, y1, x2, y2):
    midpoint = (round((x1 + x2) / 2), round((y1 + y2) / 2))
    return midpoint

def main():
    # Case 1:
    x1 = 10
    y1 = 5
    x2 = 32
    y2 = 52

    # Case 2:
    # x1 = 432
    # y1 = 214
    # x2 = 352
    # y2 = 504

    # Case 3:
    # x1 = 1
    # y1 = 1
    # x2 = 3
    # y2 = 3

    midpoint = find_midpoint(x1, y1, x2, y2)
    print(f"The midpoint of the points ({x1}, {y1}) and ({x2}, {y2}) is: {midpoint}")

if __name__ == "__main__":
    main()
