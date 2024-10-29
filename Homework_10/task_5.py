def reverse(text):
    for i in range(1, len(text) + 1):
        print(text[-i], end = "")
        i += 1
    print()

reverse("python")
reverse("hello world")
reverse("Aleksandra")