import random
from sys import exit  # exit builtin function is used to terminate the program

# start room
def start():

    choice = input("There is a door to your right and left."
                   "Which one do you take? ")

    if choice == "left":
        bank_room()
    elif choice == "right":
        your_room()  # you need to create the function your_room
    else:
        dead("You stumble around the room until you starve.")

# second room
def bank_room():

    choice = input("This room is full of money."
                   "How many bank note bundles do you take? ")

    if choice.isdigit():

        if int(choice) > 0 and int(choice) < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        elif int(choice) > 50:
            dead("You greedy bastard!")

    else:
        dead("Man, learn to type a number.")


def your_room():
    friends = []  # this is an empty list
    print("You hear a voice from somewhere: What are the names of your 3 best friends?")
    for i in range(3):
        friend = input("Give one name: ")
        friends.append(friend)  # this way we add more elements to an existing list
    print(f"Suddenly you see {friends[random.randint(0,2)]} who asks you:")
    hard_words = ["sesquipedalian", "winebibber", "saxicolous", "ebullient"]
    index = random.randint(0,2)
    print(f"Can you reverse this word? {hard_words[index]}")
    word = input("Try: ")
    if is_reverse(word, hard_words[index]):
        print(f"You did well! You can have a glass of wine now with {friends[random.randint(0,2)]}")
    else:
        print("You can't reverse a word... You live your life in reverse and go back to the time you learned to type.")


def is_reverse(word1, word2):
    size = len(word1)  # size of word in characters
    if size != len(word2):
        return False
    for index in range(size):
        if word1[index] != word2[size - index - 1]:
            return False
    return True


def dead(message):
    print(message, "You are dead.")
    exit(0)

start()
