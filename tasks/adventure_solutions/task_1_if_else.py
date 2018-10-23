print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print("Congratulations, you found a new friend!")
    elif vampire == "2":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("You are not so good with numbers, are you?")

# New door option using the `elif` statement
elif door == "2":
    print("You found a room full of coffins.")
    print("What do you do?")
    print("1. Get through them to another door without touching anything.")
    print("2. Explore the room, open a coffin.")

    coffin = input("> ")

    if coffin == "1":
        print("Congratulations, you're still alive!")
    elif coffin == "2":
        print("One of the vampires arrived and didn't like to see you messing"
              " his bed. You're not going to see the light again, sorry.")
    else:
        print("You are not so good with numbers, are you?")
else:
    print("You are not so good with numbers, are you?")
