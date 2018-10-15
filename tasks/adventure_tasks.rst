===============
Adventure Tasks
===============


.. contents::


1. If/Else
==========

A) Type the following code, save it in a file and try to understand what it does.
B) Run the file and check if what you imagined really happens.
C) Get creative! Right after the inline comments, add a second door using the elif statement.

.. code-block:: python

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

    # Exercise C

    else:
        print("You are not so good with numbers, are you?")


2. Variables
============

Now that you created new doors for your player to choose from, let's
personalize the game a little bit. Write the answer to each exercise under its
related inline comment.

A) Ask the name of the player and store the answer on a variable.
B) Use the variable in which you stored the players name to print a welcoming.
C) Customize the replies to the vampire to show the user name like in the code here.
D) Time to get creative! Ask one more question to the player and use their answer.

.. code-block:: python

    print()
    # Exercise A

    # Exercise B

    print("Do you go through door 1 or door 2?")

    door = input("> ")

    if door == "1":
        print("There is a nice vampire asking you if you enjoy life.")
        print("What do you do?")
        print("1. Smile and nod")
        print("2. Scream and run")

        vampire = input("> ")

        if vampire == "1":
            print(f"Congratulations {name}, you found a new friend!")
        elif vampire == "2":
            print(f"Sorry {name}, the vampire is faster. You become a dinner.")
        else:
            print("You are not so good with numbers, are you?")

    # Your code from Task 1 should be here

    else:
        print("You are not so good with numbers, are you?")

    # Exercise D


3. Functions
============

A) Create a function that prints and alert of wrong input (something to substitute the answer of the else).
B) Use your function where it applies.
C) Now think a bit, how would you write a dead-function using an argument called death_message? Create this function.

.. code-block:: python

    # Exercise A

    # Exercise C

    print()
    # Your code from Exercise A on Task 2 should be here

    # Your code from Exercise B on Task 2 should be here

    print("Do you go through door 1 or door 2?")

    door = input("> ")

    if door == "1":
        print("There is a nice vampire asking you if you enjoy life.")
        print("What do you do?")
        print("1. Smile and nod")
        print("2. Scream and run")

        vampire = input("> ")

        if vampire == "1":
            print(f"Congratulations {name}, you found a new friend!")
        elif vampire == "2":
            print(f"Sorry {name}, the vampire is faster. You become a dinner.")
        else:
            # Exercise B

    # Your code from Task 1 should be here

    else:
        wrong_input()

    # Your code from Exercise C on Task 2 should be here


4. Loops and Lists
==================

A) Create a list variable named `friends` that contains names of the user friends.

B) When a user enters some room, print a message saying that her 2nd friend in the list is in the room. Remember: Access list elements like this, eg. friends[0], friends[1]

C) Make this name to be chosen randomly. Import Python library random, that has functions to help with random numbers and use random.randint(a, b) function to give you a random number between a and b. eg. random.randint(1,4) will give a random number among 1, 2, 3, 4.

D) Extend your death function (from functions task before) telling the user that is falling from high:
    Eg. print:

::

    "You are falling for...

    1

    2

    3

    ...

    30

    ...

    meters!

    You are dead!"


Try to print all the numbers up to 30 or 50 with a for loop using range function, eg. range(30) will return some kind of list with numbers from 0-29.

E) Add a delay between the falling with time.sleep(secs), Eg. time.sleep(1) will pause the program for 1 sec. Remember to add import for time library typing `import time` in the beginning of the code.

.. code-block:: python

    # Exercise C the import goes here

    # Exercise A
    # friends =

    print()

    print("Do you go through door 1 or door 2?")

    door = input("> ")

    if door == "1":
        # Exercise B, C
        print("There is a nice vampire asking you if you enjoy life.")
        print("What do you do?")
        print("1. Smile and nod")
        print("2. Scream and run")

        vampire = input("> ")

        if vampire == "1":
            print(f"Congratulations {name}, you found a new friend!")
        elif vampire == "2":
            print(f"Sorry {name}, the vampire is faster. You become a dinner.")
        else:
            # Your code from Task 3 should be here

    # Your code from Task 1 should be here

    else:
        wrong_input()

    # Your code from Task 2 should be here


5. Dictionaries
===============

Dictionaries are super useful python data structures and if you are dealing with data, like
wikipedia data, questionaire data, or anything you can imagine, dictionaries will prove useful.

A) Let's use a dictionary to describe each room. Create a dictionary variable called door_greetings with keys the door numbers and values the door greeting. eg. door_greetings = {'1': "Welcome to the paradise"}.
B) When the user enters each room print the corresponding door greeting from the dictionary.

.. code-block:: python

    # Exercise A
    # door_greetings =

    print()

    print("Do you go through door 1 or door 2?")

    door = input("> ")

    if door == "1":
        # Exercise B - print room greeting
        print("There is a nice vampire asking you if you enjoy life.")
        print("What do you do?")
        print("1. Smile and nod")
        print("2. Scream and run")

        vampire = input("> ")

        if vampire == "1":
            print(f"Congratulations {name}, you found a new friend!")
        elif vampire == "2":
            print(f"Sorry {name}, the vampire is faster. You become a dinner.")
        else:
            # Your code from Task 3 should be here

    # Your code from Task 1 should be here

    else:
        wrong_input()

    # Your code from Task 2 should be here


6. More functions, 'cause functions are fun!
============================================

Practice more functions. Use the code below.

A) Get creative write a function your_room. Check where it is called in the room.

.. code-block:: python

    from sys import exit

    # start room
    def start():

        choice = input("There is a door to your right and left. Which one do you take? ")

        if choice == "left":
            bank_room()
        elif choice == "right":
            your_room()
        else:
            dead("You stumble around the room until you starve.")

    # second room
    def bank_room():

        choice = input("This room is full of money. How many bank note bundles do you take? ")

        if choice.isdigit():

            if int(choice) > 0 and int(choice) < 50:
                print("Nice, you're not greedy, you win!")
                exit(0)
            elif int(choice) > 50:
                dead("You greedy bastard!")

        else:
            dead("Man, learn to type a number.")


    # Exercise A

    def dead(why):
        print(why, "You are dead.")
        exit(0)

    start()


7. More dictionaries for the adventurous ones!
==============================================

Use the dictionary adventure below to control the game play instead of if-else statements.

This task combines for-loops, complex dictionaries and lists. It is recommended after the
concepts of loops and dictionaries and lists are pretty well understood.

In the code below there a complex dictionary named `adventure` that has as values dictionaries as well.
This complex dictionary includes all the text needed to play the game. The value of a door eg door '1' is
also a dictionary, with keys "greeting" that is the text to show when the user enters the room and
"options" which is a list of dictionaries with the "action" to display and then the "result" to show to the
user when they choose this option. Currently only the door 1 is defined.


A) Take some time to understand the structure of the dictionary adventure in the code below. Copy this code to a new file and continue the program in the indicated line and print the greeting of the chosen door, using the value from the dictionary.
    Eg. the greeting of the door '1' can be accessed with adventure['1']['greeting'] or if the door number is in a variable called door, adventure[door]['greeting'] will get the greeting for the variable door from the dictionary. This value can be passed directly into a print statement.

B) Exactly after the print of the greeting print the possible actions for each option of the chosen door.
    eg:

    Options:

    1. Smile and node

    2. Scream and run


    Tips:
        * Accessing the action of the first option of the first door can be done with adventure['1']['options'][0]['action']
        * For loop is needed to go through the list of options.
        * To show the number of each option python enumerate function can be useful, http://book.pythontips.com/en/latest/enumerate.html

C) Add more options to door '1'.

D) Add more doors to adventure dictionary. Tip: Copy paste the structure of door '1' and change the values.

E) If the chosen door is not available in adventure show a message. Tip to check if a value is one of the dictionary keys, the "in" or the "not in" can be used.
    eg. if door in adventure.


.. code-block:: python

    adventure = {
        '1': {
            "greeting": "There is a nice vampire asking you if you enjoy life. What do you do?",
            "options": [
                {
                    "action": "Smile and nod",
                    "result": "Congratulations, you found a new friend!"
                },
                {
                    "action": "Scream and run",
                    "result": "Sorry the vampire is faster, you are dead!"
                },
                # Exercise C
            ]
        },
        # Exercise D
    }

    doors = '/'.join(adventure.keys())   # join() is python method to make one string out of a list of things
                                         # adventure.keys() is a list with all the dictionary keys, in that
                                         # case is only door ['1']
    print(f"Which door do you choose ({doors}) ?")

    door = input("> ")

    # Exercise A - print greeting to the chosen door

    # Exercise B - print user options with their number

    # Exercise C - if the door is not in the available options print a message
