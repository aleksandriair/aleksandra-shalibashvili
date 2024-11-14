word_list = ["dog", "cat", "internet", "python", "car", "food"]

def filter_words(word_list):
    return [word.upper() for word in word_list if len(word) <= 3]

def main():
    filtered_word_list = filter_words(word_list)
    print(f"Filtered word list: {filtered_word_list}")

if __name__ == "__main__":
    main()