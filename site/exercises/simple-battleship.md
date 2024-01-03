---
title: EX01 - Simple Battleship
author:
- Camilla Fratta
- Audrey Salmon
- Vrinda Desai
- Alyssa Lytle
page: exercises
template: overview
---


## Introduction

This semester, we will take inspiration from the stategy game of Battleship. It's usually a two-player game, but you will be coding a single-player version!

In this exercise, you will have a row of boxes (blue for the sea) and you will prompt the user for a number between 1 and 4, corresponding to their guess of at which box a ship is lurking behind. You will then test to see if the user input matches the square with the ship and print out whether it was a hit or a miss, along with a visual of the boxes. You will also notify the user if they inputed a number out of range.

You should follow the steps below for implementing the program one step at a time. To get a sense of where you are going, though, consider what we expect the output to be given some example inputs:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 5
    Error! There are only 4 squares.
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 3
    🟦🟦⬜🟦
    Incorrect! You missed the ship.
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 2
    🟦🟥🟦🟦
    Correct! You hit the ship.
</div>
</pre>

## Background Lesson: Emoji

In this exercise you will need to make use of an advanced string concepts: emoji! 🤠

Before beginning work on this exercise, read the following lesson and complete the related questions on Gradescope: [Unicode, Emoji, Escape Sequences, and f-Strings](/lessons/strings.html)

## Part 0. Setting up the Python Program

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex00_simple_battleship.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you did in EX00. Then, you should add a line with the special variable named `__author__` assigned to be a string with your 9-digit student PID. (Disclaimer: Out in the real world the `__author__` variable is typically your name and e-mail address, but since we will grade your programs we'd like to avoid potential bias in seeing your names as part of the programs as we're grading.) Add the following lines above the line of code that calls the `print` function. Fill in _your_ 9-digit UNC PID number, without any spaces or dashes, in the `__author__` string.


~~~ {.python}
    """EX01 - One-Shot Battleship - A cute step toward Battleship."""

    __author__ = "1234567890"
~~~

## Part 1. Establishing a Secret and Prompting for Inputs -- XX Points

In your program, establish an `int` variable to hold your secret number (which box the ship is hidden behind) and initialize it to a secret number of your choice. For troubleshooting purposes, in the Part 1 and 2, please use a secret number of `2`. You will then level up the game in Part 3 so that you yourself can play the game!

The first task of this program is to decide at which number box the ship is hidden and to gather an input guess from the user. Using the concepts you learned in [User Input and Variables](https://youtu.be/GPpYSDNUtH8), you will want to ask the user to enter a number, storing it as an `int` variable. **Please choose meaningful, descriptive names for your variables.** Write your prompts and diagnostic message such that you can reproduce the following in the shell after saving and running your program:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 3
    User's guess is 3. Ship is at box 2.
    
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 2
    User's guess is 2. Ship is at box 2.
</div>
</pre>

**WARNING:** Autograding will very specifically be looking for _exactly_ the format of lines output shown above. You will not see the `$` at your command-line prompt in VSCode, you can ignore that part. Otherwise, when you run the program on your machine with the same inputs as above on the first two lines, your printed results should look exactly like the 3rd line and 7th line.

## Part 2. Checking User Input for Match -- XX Points

Now that you have gathered your input from Part 1 and stored it as a variable, your task is to check if the user input is equivalent to the box where the ship is hidden (hint: _is equal to_). These checks will involve combining concepts you've learned in recent lessons:

* [Expressions](/lessons/expressions.html)
    * Relational Operators - Equality
* [Conditional if-else Statements](https://www.youtube.com/watch?v=395mlzouM00)

You'll have to translate the following English logic into Python:
_If_ the user's input is equal to the secret number, _then_ you should print out a message indicating that the user correctly hit the ship. _Else_, you should print out a statement that they missed the ship.

Your goal in this part is to be able to do the following:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 3
    Incorrect! You missed the ship.
    
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 2
    Correct! You hit the ship.
</div>
</pre>

Note: You will be modifying some of your previous print statements. They were there in Part 1 to help you troubleshoot and make sure you were saving the numbers correctly.

## Part 3. Random! - XX points

Okay, wouldn't be fun if you didn't know the correct box ahead of time? That way _you_ can play the game! Instead of setting the secret number to 2, make it pick a random integer between 1 and 4. Remember, you need to import the `randint` function from the `random` package before calling it.

It's important that you didn't hard code the secret number and instead used its variable name in the checks in Part 2.

## Part 3. Printing A String of Boxes - XX points

Now, let's bring a visual aid to the game! You will need to build up a string of emojis using concatenation to show where the user hit or missed a boat. You can use the following _named constants_ in your program to simplify your implementation. We will learn more about named constants soon, but for now know they are simply variables whose values you will not change later in your program and make your programs easier to read:

~~~{.python}
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
~~~

Next, create a `str` guess result variable and modify your current `if` and `else` statements in the following way:

_If_ the user's guess matches your secret number, make the guess result variable red. _Else_, make the guess result variable white.

Now, you need to start building your string of emoji boxes. Establish another `str` variable to store the resulting emoji string of the guess and initialize it to an empty string.
Essentially, the default box should be blue, unless its the box position that the user correctly or incorrectly picked (red or white, respectively). In the future, you will use _loops_ to make this process more efficient, but for now, you will need a series of `if` statements to check each possible option. Here's an example for the first one:

_If_ the user input guess equals 1, concatenate the guess box to the resulting emoji string of boxes. _Else_, contatenate the blue box.

The logic is similar for all other possible box numbers. After checking for each posible box, print the resulting emoji string of boxes.

Your goal in this part is to be able to do the following (if the random number picked is 2):

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 3
    🟦🟦⬜🟦
    Incorrect! You missed the ship.

    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 1
    ⬜🟦🟦🟦
    Incorrect! You missed the ship.

    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 2
    🟦🟥🟦🟦
    Correct! You hit the ship.
</div>
</pre>

If you're struggling to test and guess the correct number, you can comment out the `randint` call and hard code any value between 1 and 4 (like we did in the beginning for 2). Your code should still work! Note: when you submit to gradescope, make sure to turn the `randint` back on.

## Part 4. Exiting Early for Invalid Inputs - 10 points

What happens if you input a number that's larger than 4, that's out of bounds? It's good practice to handle bad input from an end-user gracefully in your programs. Our strategy, for now, will be to simply print an error message and then exit the program early. There is a special built-in function called `exit()` that will send a signal to your system and tell the program to quit at that point, not continuing on further in the program. Before attempting to implement the following behavior in your program, think about where it logically _makes sense_ to try adding these checks for correct input.

Here is how your program should work after completing this part:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Guess a number between 1 and 4: 5
    Error! There are only 4 squares.
</div>
</pre>

## Part 6. Type Safety and Linting - XX Points

The autograder uses industry standard tools for checking the type safety of your programs (e.g. being sure you're using variables of the correct data types in valid ways) and linting style rules. If you have point deductions on Type Safety or Linting, read through the feedback the autograder gives and it should direct you to the line number in your program with the issue.

## Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Login to Gradescope and select the assignment named "EX01 - Chardle". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex00_simple_battleship.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex01_chardle.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 10 "human graded" points. Thus, you should expect a maximum autograding score of 90 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!