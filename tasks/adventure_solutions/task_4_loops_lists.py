import random #import library random

# create list with names
friends = ['Emily', 'Aurora', 'Jack', 'Daniel', 'Meghan']

def wrong_input(valid):
    print(f"Sorry but the only valid options are: {valid}.")

print()
name = input("What is your name? ")
print(f"Welcome to the dungeon, {name}!")

print("Do you go through door 1 or door 2?")
door = input("> ")

if door == "1":
    # print name randomly chosen from list
    print(f"Look who's here! Your friend {friends[random.randint(0,4)]}!")

    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("A. Smile and nod")
    print("B. Scream and run")

    vampire = input("> ")

    if vampire == "A":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "B":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")
    else:
        wrong_input("A, B")

elif door == "2":
    # print name randomly chosen from list
    rand_int = random.randint(0,4)  # store the random number in a variable
    print(f"Look who's here! Your friend {friends[rand_int]}!") # use variable to print item from the dictionary

    print("You found a room full of coffins.")
    print("What do you do?")
    print("A. Get through them to another door without touching anything.")
    print("B. Explore the room, open a coffin.")

    coffin = input("> ")

    if coffin == "A":
        print(f"Congratulations {name}, you're still alive!")
    elif coffin == "B":
        print("One of the vampires arrived and didn't like to see you messing"
              f" her bed. You're not going to see the light again, sorry {name}.")
    else:
        wrong_input("A, B")

else:
    wrong_input("1, 2")

print()
bye = input("Say 'Good bye' in a language other than English: ")
print(f"{bye}, {name}!")
