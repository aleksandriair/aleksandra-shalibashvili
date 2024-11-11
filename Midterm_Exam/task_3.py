from random import randint

def rock_paper_scissors():
    options = ["R", "P", "S"]
    random_number = randint(0, 2)
    computer_choice = options[random_number]
    return computer_choice

def main():
    print(f"Welcome to the game of Rock, Paper, Scissors! R stands for Rock; P stands for paper; S stands for scissors. Good luck!")
    user_choice = input("Please enter R, P or S: ")

    computer_choice = rock_paper_scissors()

    if user_choice == computer_choice:
        print(f"This is a tie. You can play again.")
        user_input = input("Would you like to play again? [Yes / No]: ")
        if user_input == "Yes":
            main()
    elif (user_choice == "R" and computer_choice == "S") or (user_choice == "S" and computer_choice == "P") or (user_choice == "P" and computer_choice == "R"):
        print(f"{user_choice} beats {computer_choice}.")
        print(f"You've won! Congratulations!")
    elif (user_choice == "S" and computer_choice == "R") or (user_choice == "P" and computer_choice == "S") or (user_choice == "R" and computer_choice == "P"):
        print(f"{computer_choice} beats {user_choice}.")
        print(f"You've lost. Better luck next time.")

if __name__ == "__main__":
    main()