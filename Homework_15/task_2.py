def count_unique_symbols(text):
    text = text.lower()
    my_dict = {}

    for char in text:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1
    return my_dict

def main():
    text = input("Please enter your text: ")
    my_dict = count_unique_symbols(text)
    print(f"The number of unique characters in your text is: {my_dict}")

if __name__ == "__main__":
    main()