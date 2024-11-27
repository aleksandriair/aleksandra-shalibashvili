def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield tuple(data[i:i + chunk_size])


def main():
    # Case 1:
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    chunk_size = 3

    # Case  2:
    # data = (1, 2, 3, 4, 5, 6, 7, 8)
    # chunk_size = 3

    # Case 3:
    # data = ("a", "b", "c", "d", "e", "f", "g", "h", "i")
    # chunk_size = 5

    print(f"The original data is: {data}")
    print(f"Chunk size: {chunk_size}")
    print(f"The final output:")
    for chunk in chunk_data(data, chunk_size):
        print(chunk)


if __name__ == "__main__":
    main()

