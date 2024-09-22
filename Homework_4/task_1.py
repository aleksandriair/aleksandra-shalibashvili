import random

players_number = int(input("Please enter the number of players: "))

for i in range(players_number):
    print(random.randint(1,6),random.randint(1,6))