import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

suits_random_number = random.randint(1, 4)
ranks_random_number = random.randint(1, 13)

print("Your random card is a", ranks[ranks_random_number],"of",suits[suits_random_number])