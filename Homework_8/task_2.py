text_1 = input("Please enter the first text: ")
text_2 = input("Please enter the second text: ")

anagram = True
for i in range(len(text_1)):
    if text_1[i].lower() not in text_2.lower():
        anagram = False

for j in range(len(text_2)):
    if text_2[j].lower() not in text_1.lower():
        anagram = False

print("Output: ", end = "")

if anagram == True:
    print("YES")
else:
    print("NO")


# მეორენაირი გზა:
# print("Output: ", end = "")
# if sorted(text_1.lower()) == sorted(text_2.lower()):
#     print("YES")
# else:
#     print("NO")