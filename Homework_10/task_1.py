def count_vowels(text):
    vowel_counter = 0
    for char in text:
        if char.lower() in "aeiou":
            vowel_counter += 1
    return vowel_counter

print(count_vowels("Python"))
print(count_vowels("Hello world"))
print(count_vowels("Hi, my name is Aleksandra"))