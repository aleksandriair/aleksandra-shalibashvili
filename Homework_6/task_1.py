from random import randint

magic_number = randint(0,100)

try_count = 0
while try_count < 10:
    user_number = int(input("Please enter your guess: "))
    try_count += 1

    if user_number == magic_number:
        print("You are the winner!")
        break
    elif user_number < magic_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

if try_count == 10 and user_number != magic_number:
    print("Computer is the winner!")