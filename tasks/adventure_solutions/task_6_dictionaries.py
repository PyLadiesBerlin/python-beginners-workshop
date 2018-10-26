import random
import time

def wrong_input(valid):
    print(f"Sorry but the only valid options are: {valid}.")

def dead(death_message):
    print(f"Sorry {name}, {death_message}.")
    print("You're falling for...")

    for number in range(1,11):
        print(number)
        time.sleep(1)

    print("meters!")
    print("You are dead!")

friends = ['Emily', 'Aurora', 'Jack', 'Daniel', 'Meghan']

# create dictionary with greetings to each door
door_greetings = {'1': "Welcome to paradise!",
                  '2': "Welcome to the dormitory!"}

print()
name = input("What is your name? ")
print(f"Welcome to the dungeon, {name}!")

print("Do you go through door 1 or door 2?")
door = input("> ")

if door == "1":
    print(f"{door_greetings[door]}") # print greeting based on dictionary
    print(f"Look who's here! Your friend {friends[random.randint(0,4)]} :D")

    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("A. Smile and nod")
    print("B. Scream and run")

    vampire = input("> ")

    if vampire == "A":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "B":
        dead("the vampire is faster")
    else:
        wrong_input("A, B")

elif door == "2":
    print(f"{door_greetings[door]}") # print greeting based on dictionary
    print(f"Look who's here! Your friend {friends[random.randint(0,4)]}! :D")

    print("You found a room full of coffins.")
    print("What do you do?")
    print("A. Get through them to another door without touching anything.")
    print("B. Explore the room, open a coffin.")

    coffin = input("> ")

    if coffin == "A":
        print(f"Congratulations {name}, you're still alive!")
    elif coffin == "B":
        dead("vampires don't like outsiders messing their beds")
    else:
        wrong_input("A, B")

else:
    wrong_input("1, 2")

print()
bye = input("Say 'Good bye' in a language other than English: ")
print(f"{bye}, {name}!")
