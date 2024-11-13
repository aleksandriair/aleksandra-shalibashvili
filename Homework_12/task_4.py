def combine_lists(list_one, list_two):
    list_combined = []

    i = 0
    j = 0

    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            list_combined.append(list_one[i])
            i += 1
        else:
            list_combined.append(list_two[j])
            j += 1

    while i < len(list_one):
        list_combined.append(list_one[i])
        i += 1

    while j < len(list_two):
        list_combined.append(list_two[j])
        j += 1

    return list_combined

def main():
    
    # Test case 1:
    list_one = [1, 3, 10]
    list_two = [0, 4, 7, 9]
    
    # Test case 2:
    # list_one = [1, 5, 120, 3000]
    # list_two = [-5, 0, 3.14, 156, 1500, 2304]

    # Test case 3:
    # list_one = [0, 0.25, 0.333, 0.9, 1]
    # list_two = [0.5]

    list_combined = combine_lists(list_one, list_two)

    print(f"List one: {list_one}")
    print(f"List two: {list_two}")
    print(f"Combined list: {list_combined}")



if __name__ == "__main__":
    main()