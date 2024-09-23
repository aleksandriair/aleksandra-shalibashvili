number = input("Please enter a whole number - ")

if not number.isdigit() or not (0 < int(number) < 10):
    print("გთხოვთ, ახლიდან სცადოთ და შეიყავნოთ დადებითი მთელი რიცხვი, რომელიც 10-ზე ნაკლებია")
    exit(1)

number = int(number)

if number == 1:
    print("არ აქვს მარტივი გამყოფი")
elif number == 2 or number == 4 or number == 8:
    print("2")
elif number == 3 or number == 9:
    print("3")
elif number == 5:
    print("5")
elif number == 6:
    print("2, 3")
elif number == 7:
    print("7")