action = input("Enter action (e/d): ")
text = input("Enter text: ")

keyboard1 = "qwertyuiop"
keyboard2 = "asdfghjkl"
keyboard3 = "zxcvbnm"

if action == "e":
    for i in range(len(text)):
        if text[i] in keyboard1:
            for j in range(len(keyboard1)):
                if text[i] == keyboard1[j]:
                    if j != len(keyboard1)-1:
                        print(keyboard1[j+1], end = "")
                    else:
                        print(keyboard1[0], end = "")
        elif text[i] in keyboard2:
            for j in range(len(keyboard2)):
                if text[i] == keyboard2[j]:
                    if j != len(keyboard2)-1:
                        print(keyboard2[j+1], end = "")
                    else:
                        print(keyboard2[0], end = "")
        elif text[i] in keyboard3:
            for j in range(len(keyboard3)):
                if text[i] == keyboard3[j]:
                    if j != len(keyboard3)-1:
                        print(keyboard3[j+1], end = "")
                    else:
                        print(keyboard3[0], end = "")
        else:
            print(text[i], end = "")
            


if action == "d":
    for i in range(len(text)):
        if text[i] in keyboard1:
            for j in range(len(keyboard1)):
                if text[i] == keyboard1[j]:
                    if j != 0:
                        print(keyboard1[j-1], end = "")
                    else:
                        print(keyboard1[len(keyboard1)-1], end = "")
        elif text[i] in keyboard2:
            for j in range(len(keyboard2)):
                if text[i] == keyboard2[j]:
                    if j != 0:
                        print(keyboard2[j-1], end = "")
                    else:
                        print(keyboard2[len(keyboard3)-1], end = "")
        elif text[i] in keyboard3:
            for j in range(len(keyboard3)):
                if text[i] == keyboard3[j]:
                    if j != 0:
                        print(keyboard3[j-1], end = "")
                    else:
                        print(keyboard3[len(keyboard3)-1], end = "")
        else:
            print(text[i], end = "")

print()