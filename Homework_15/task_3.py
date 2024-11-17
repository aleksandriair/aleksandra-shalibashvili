def add_friendship(friendships, person1, person2):
    if person1 not in friendships:
        friendships[person1] = []
    if person2 not in friendships:
        friendships[person2] = []
    
    if person2 not in friendships[person1]:
        friendships[person1].append(person2)
    if person1 not in friendships[person2]:
        friendships[person2].append(person1)

def print_friendships(friendships):
    for person in friendships.keys():
        friends = friendships[person]
        if friends:
            print(f"{person} – ", end="")
            for i in range(len(friends)):
                if i == len(friends) - 1:
                    print(friends[i])
                else:
                    print(friends[i] + ", ", end="")

def process_input(friendships):  # New function to handle recursive input
    user_input = input("Please add friendship information: ")
    user_input = user_input.strip()

    if user_input != "FINISH":
        person1, person2 = [name.strip() for name in user_input.split(" - ")]
        add_friendship(friendships, person1, person2)
        process_input(friendships)  # Pass the friendships dictionary
    else:
        print_friendships(friendships)

def main():
    friendships = {}
    process_input(friendships)

if __name__ == "__main__":
    main()