print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("A. Smile and nod")
    print("B. Scream and run")

    vampire = input("> ")

    if vampire == "A":
        print("Congratulations, you found a new friend!")
    elif vampire == "B":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("That is not a valid option!")

# New door option using the `elif` statement
elif door == "2":
    print("You found a room full of coffins.")
    print("What do you do?")
    print("A. Get through them to another door without touching anything.")
    print("B. Explore the room, open a coffin.")

    coffin = input("> ")

    if coffin == "A":
        print("Congratulations, you're still alive!")
    elif coffin == "B":
        print("One of the vampires arrived and didn't like to see you messing"
              " her bed. You're not going to see the light again, sorry.")
    else:
        print("That is not a valid option!")
else:
    print("That is not a valid option!")
