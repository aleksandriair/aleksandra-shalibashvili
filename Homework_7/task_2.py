word = input("Please enter a word: ")

for i in range(len(word)):
    if word[i] not in {"a","e","i","o","u"}:
        print(word[i])