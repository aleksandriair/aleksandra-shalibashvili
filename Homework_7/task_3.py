word = input("Please enter a word: ")

counter = 0
while counter < 5:
    if len(word) % 2 == 1:
        print(word[0], word[int(len(word)/2-0.5)], word[len(word)-1])
    else:
        print(word[0],word[int(len(word)/2-1)], word[int(len(word)/2)], word[len(word)-1])
    counter += 1