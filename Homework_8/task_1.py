text = input("Please enter a text: ")

clean_text = ""
for i in range(len(text)):
    if text[i].lower() in "qwertyuiopasdfghjklzxcvbnm":
        clean_text += text[i].lower()

counter = 0
for i in range(len(clean_text)):
    if clean_text[i] == clean_text[-(i+1)]:
        counter +=1

if counter == len(clean_text):
    print("Is a palindrome")
else:
    print("Is not a palindrome")