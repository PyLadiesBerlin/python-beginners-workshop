=========================
Create your own adventure
=========================

This set of tasks aims to help you practice basic Python concepts (variables,
printing, user input, if-elif-else condition, list, for loop, dictionary,
libraries).

For the tasks you will create a new python file in which you'll build your text
adventure. In each step you will extend your file with the tasks exercises. Do
not copy paste the code, just use it as a guide. Go back to the presentation
examples to check the syntax and ask coaches for help when you get stuck ;) As
a last resource, there's a file with a possible solution in the end of each task.


.. contents::


1. If/Else
==========

A) Type the following code, save it in a file and try to understand what
   it does.

B) Run the file and check if what you imagined really happens.

C) Get creative! Right after the inline comments, add a second door using
   the elif statement.

.. code-block:: python

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

    # Add code here! Make sure to be indented (vertically aligned) correctly

    else:
        print("You are not so good with numbers, are you?")

See possible solution in `task_1_if_else.py`_.

.. _task_1_if_else.py: adventure_solutions/task_1_if_else.py


2. Variables
============

Continue in your file from the previous exercise or use the solution from the
previous exercise as a basis for this exercise. Now that you created a new door
for your player to choose from, let's personalize the game a little bit. Write
the answer to each exercise under its related inline comment.

A) At the beginning of the program, add code to ask the name of the player and
   store the answer in a variable.

B) Right after the line you added in A, use the variable in which you stored
   the players name to print a welcoming using the name of the user.

C) Customize the replies to the various doors and questions to show the user
   name. For example if the variable `name` holds the name of the user, the
   code could look like that: (for Python 3.6 or greater)


.. code-block:: python


    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")


D) Time to get creative! Ask one more question to the player and use their
   answer. It can be either inside a door, or after the doors a totally
   separate question in the end of the file.

See possible solution in `task_2_variables.py`_.

.. _task_2_variables.py: adventure_solutions/task_2_variables.py


3. Functions
============

Continue in your file from the previous exercise or use the solution from the
previous exercise as a basis for this exercise.

A) Create a function in the begging of your file that prints and alerts of wrong
   input (something to substitute the answer of the else).

B) Use your function where it applies.

C) Change your function to receive an argument called ``valid``.
   eg ``def wrong_input(valid)``. Your function can now print the value of
   ``valid`` options that are passed. For example if the valid options for
   the user to type is `1` or `2`, when the user types something other than 1
   or 2, the `wrong_input` function should be called like that:

.. code-block:: python

    wrong_input("1, 2") # this could print:
                        # "Sorry but the only valid options are: 1, 2."

See possible solution in `task_3_functions.py`_.

.. _task_3_functions.py: adventure_solutions/task_3_functions.py


4. Loops and Lists
==================

Continue in your file from the previous exercise or use the solution from the
previous exercise as a basis for this exercise.

A) At the beginning of the file, create a *list* variable named ``friends`` with
   names of the user's friends.

.. code-block:: python

    # Remember defining a list variable looks like that:
    my_var = ['zero_element', 'first_element']

B) When a user enters some room, print a message saying that her 2nd friend in
   the list is in the room (print the name of the friend from the variable
   ``friends``).

::

    # Remember: Access list elements like this eg. friends[0], friends[1]

C) Make this name be chosen randomly. At the first line of the file, import
   Python library called ``random``. This library has functions to help with
   random numbers and use ``random.randint(a, b)`` function to give you a random
   number between a and b. eg. ``random.randint(1, 4)`` will return a random
   number between 1-4, so one of 1, 2, 3, 4. Use this function to choose a
   random name from the names list.

.. code-block:: python

    # Remember: import statement looks like this:
    import that_awesome_library_name

See possible solution in `task_4_loops_lists.py`_.

.. _task_4_loops_lists.py: adventure_solutions/task_4_loops_lists.py


5. Loop, Range, Function
========================

Continue in your file from the previous exercise or use the solution from the
previous exercise as a basis for this exercise.

A) Now think a bit, how would you write a ``dead`` function using an argument
   called ``death_message``? This function could be called in every point that
   they user dies eg. when the user becomes a dinner for the vampire. To figure
   out where this function should be added, check the structure of a typical
   python file:

.. _file_structure:

::
    # Common Python file structure

    # import statements

    # function definitions

    # global variables (variable outside functions)

    # code outside of a function

B) Extend your ``dead`` function telling the user that is falling from high.
   Make the function print:

::

    "You are falling for...

    1

    2

    3

    ...  # with all the numbers in between

    30

    meters!

    You are dead!"


Print all the numbers up to 10 or 30 with a ``for`` loop using ``range``
function. For example ``range(30)`` will return some kind of list with numbers
from 0-29.

C) Add a delay while falling in each step with ``time.sleep(secs)`, Eg.
   ``time.sleep(1)`` will pause the program for 1 sec. Remember to add import
   for time library with ``import time`` before it is used (see file_structure_).

See possible solution in `task_5_loop_range_function.py`_.

.. _task_5_loop_range_function.py: adventure_solutions/task_5_loop_range_function.py


6. Dictionaries
===============

Dictionaries are super useful python data structures. When dealing with data,
like wikipedia data, questionnaire data, or anything you can imagine,
dictionaries will prove themselves quite useful.

Continue in your file from the previous exercise or use the solution from the
previous exercise as a basis for this exercise.

A) Let's use a dictionary to describe each room greeting. Create a dictionary
   variable called ``door_greetings`` with keys being the door numbers and
   values being the door greeting. It could look like:

.. code-block:: python

   door_greetings = {'1': "Welcome to paradise!"}

::

Tip:
Define the variable near other global variables (see file_structure_).

B) In each room the user enters, print the corresponding door greeting from the
   dictionary. Use the ``door`` variable to show the correct message.

See possible solution in `task_6_dictionaries.py`_.

.. _task_6_dictionaries.py: adventure_solutions/task_6_dictionaries.py


7. While the user types crap keep asking
========================================

So far in the game when the user types something that is not correct, the
program continues giving a message. What if we want the program to keep asking
until the user types something useful? Then the code should be executed again.
Given the example where the program expects only two possible answers:

Example ``Invalid message``:

.. code-block:: python

    number = input('Choose a door (1/2):')

    if number != '1' and number != '2':
        print('Only 1 or 2 is valid!!!!')

The code could be repeated with a `while` loop. Any command inside while
(indented under while) would be repeated while the condition is valid.

Example ``while``:

.. code-block:: python

    number = 0
    while number != 'n':
        number = input('Do you want me to ask you again (y/n)?')

A) In a new file type the code from the example ``Invalid message`` above and
   make it repeat until the user types a valid option.

B) Now that you practiced a bit ``while``, use it in the main adventure file.
   Continue in your file from the previous exercise or use the solution from the
   previous exercise as a basis for this exercise. Make the program keep asking
   for a valid door while the user doesn't give an acceptable answer.

See possible solution in `task_7_while.py`_.

.. _task_7_while.py: adventure_solutions/task_7_while.py


8. More functions, 'cause functions are fun!
============================================

Practice more functions. Make a new file and use the code below. The code is not
valid because the used ``your_room`` function is not yet defined.

A) Get creative, write a function ``your_room``. Check where it is called in the
   room.

.. code-block:: python

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

    def dead(message):
        print(message, "You are dead.")
        exit(0)

    start()


See possible solution in `task_8_more_functions.py`_.

.. _task_8_more_functions.py: adventure_solutions/task_8_more_functions.py

9. More dictionaries for the adventurous ones!
==============================================

Use the dictionary adventure below to control the game play instead of if-else
statements.

The values of a dictionary can be dictionaries as well, that have values lists
with elements that can be lists or dictionaries as well. This can lead to a
pretty complicated data structure. For example:

.. code-block:: python

    map = {
        'sea': [
            {'boat1': ['maria', 'elena', 'stella']},
            {'boat2': ['jose', 'jes', 'katya']}],
        'shore': [
            {'building1': ['irina', 'fei', 'persa']}
        ]
    }


The code above is a representation of  ``map``, with the keys ``sea`` and
``shore``. Each of these keys have as values lists. The value of ``sea`` is
``[{'boat1': ['maria', 'elena', 'stella']}, {'boat2': ['jose', 'jes', 'katya']}]``
which is a list with 2 dictionary elements, each one is a dictionary with the
key being the boat name and the value being the passengers. To print eg the
passengers of ``boat2`` one shall do ``print(map['sea'][0]['boat2'])``.

We will use such a complex dictionary to control the adventure game. Create a
new file and type the code below. The dictionary ``adventure`` that has as
values dictionaries as well, includes all the text needed to play the game. The
value of a door, eg door '1', is also a dictionary, with key ``'greeting'``
which is the text to show when the user enters the room and ``"options"`` which
is a list of dictionaries with the "action" to display and then the "result" to
show to the user when they choose this option. Currently only the door 1 is
defined.


A) Take some time to understand the structure of the dictionary adventure in the
   code below. Copy this code to a new file and continue the program in the
   indicated line and print the greeting of the chosen door, using the value
   from the dictionary. Eg. the greeting of the door '1' can be accessed with
   ``adventure['1']['greeting']`` or if the door number is in a variable called
   door, ``adventure[door]['greeting']`` will get the greeting for the variable
   door from the dictionary. This value can be passed directly into a print
   statement.

B) Exactly after the print of the greeting, print the possible actions for each
   option of the chosen door.
   eg:

::

    1. Smile and node

    2. Scream and run


Tips:
    * Accessing the action of the first option of the first door can be done
      with  ``adventure['1']['options'][0]['action']``
    * ``for`` loop is needed to go through the list of options.
    * To show the number of each option python ``enumerate`` function can be
      useful, http://book.pythontips.com/en/latest/enumerate.html

C) Add more options to door ``'1'``.

D) Add more doors to the ``adventure`` dictionary.

    Tip: Copy paste the structure of door '1' and change the values to avoid
    missing commas and parenthesis, but remember to add a comma before your new
    values.

E) If the chosen door is not available in adventure, show a message. Tip to
   check if a value is one of the dictionary keys, the ``"in"`` or the
   ``"not in"`` can be used. eg. ``if door in adventure``.


.. code-block:: python

    adventure = {
        '1': {
            'greeting': 'There is a nice vampire asking you if you enjoy life.'
                        'What do you do?',
            'options': [
                {
                    'action': 'Smile and nod',
                    'result': 'Congratulations, you found a new friend!'
                },
                {
                    'action': 'Scream and run',
                    'result': 'Sorry the vampire is faster, you are dead!'
                },
                # Exercise C
            ]
        },
        # Exercise D
    }

    doors = '/'.join(adventure.keys())   # join() is python method to make one
                                         # string out of a list of things
                                         # adventure.keys() is a list with all
                                         # the dictionary keys, in that case is
                                         # only door ['1']
    print(f"Which door do you choose ({doors}) ?")

    door = input("> ")

    # Exercise A - print greeting to the chosen door

    # Exercise B - print user options with their number

    # Exercise C - if the door is not in the available options print a message
