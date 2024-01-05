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

This semester, we will take inspiration from the strategy game of [Battleship](https://www.youtube.com/watch?v=4gHJlYLomrs)! 

This exercise is meant to be the first step to building the full game!
You will prompt Player 1 to input a secret number between 1 and 4. Then, you will prompt Player 2 to guess the secret number. Then you will tell Player 2 whether or not they guessed correctly (aka whether it was a *hit* or a *miss*) using colored boxes. For both player inputs, you will also notify the user if they input a number out of range.

You can follow the steps below for implementing the program one step at a time. 
To get a sense of where you are going, though, consider what we expect the output to be given some example inputs:


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 1
    Guess a number between 1 and 4: 3
    🟦🟦⬜🟦
    Incorrect! You missed the ship.
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 2
    Guess a number between 1 and 4: 2
    🟦🟥🟦🟦
    Correct! You hit the ship.
</div>
</pre>

## Background Lesson: Emoji

In this exercise you will need to make use of an advanced string concepts: emoji! 🤠

Before beginning work on this exercise, read the following lesson and complete the related questions on Gradescope: [Unicode, Emoji, Escape Sequences, and f-Strings](/lessons/strings.html)

## Part 0. Setting up the Python Program - 10 points

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex00_simple_battleship.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you did in EX00. Then, you should add a line with the special variable named `__author__` assigned to be a string with your 9-digit student PID. (Disclaimer: Out in the real world the `__author__` variable is typically your name and e-mail address, but since we will grade your programs we'd like to avoid potential bias in seeing your names as part of the programs as we're grading.) Add the following lines above the line of code that calls the `print` function. Fill in _your_ 9-digit UNC PID number, without any spaces or dashes, in the `__author__` string.


~~~ {.python}
    """EX01 - Simple Battleship - A cute step toward Battleship."""

    __author__ = "1234567890"
~~~

## Part 1. Prompting for Player 1 Input - 15 points
Using the concepts you learned in [User Input and Variables](https://youtu.be/GPpYSDNUtH8), you will want to ask the first user to "Pick a secret boat location between 1 and 4: ", storing their input it as an `int` variable. 
**Please choose meaningful, descriptive names for your variables.** 

If they give a valid input between 1 and 4, the program should exit and print nothing. However, if their input is too low or too high, it should print an error message. Write your prompts and diagnostic message such that you can reproduce the following in the shell after saving and running your program:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 0
    Error! 0 too low!
    
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 5
    Error! 5 too high!

    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 3
</div>
</pre>

*(Hint: f-strings are useful for creating these outputs!)*

**WARNING:** Autograding will very specifically be looking for _exactly_ the format of lines output shown above. You will not see the `$` at your command-line prompt in VSCode, you can ignore that part. Otherwise, when you run the program on your machine with the same inputs as above, your printed results should match exactly.

## Part 2. Prompting for Player 2 Input - 15 points

Now, you will do the same to prompt the second user for input with "Guess a number between 1 and 4: " and store that under a different variable name.
(Imagine Player 1 input their boat location and then passed the computer to Player 2.)

If they give a valid input between 1 and 4, the program should exit and print nothing. However, if their input is too low or too high, it should print an error message. Write your prompts and diagnostic message such that you can reproduce the following in the shell after saving and running your program:


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 1
    Guess a number between 1 and 4: 0
    Error! 0 too low!
    
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 1
    Guess a number between 1 and 4: 5
    Error! 5 too high!
</div>
</pre>

**WARNING:** Autograding will very specifically be looking for _exactly_ the format of lines output shown above. You will not see the `$` at your command-line prompt in VSCode, you can ignore that part. Otherwise, when you run the program on your machine with the same inputs as above, your printed results should match exactly.

## Part 3. Checking User Input for Match - 20 points

Now that you have gathered your inputs from Part 1 and Part 2 and stored them as variables, your task is to check if the Player 2's guess is equivalent to the box where the ship is hidden (hint: _is equal to_). These checks will involve combining concepts you've learned in recent lessons:

* [Expressions](/lessons/expressions.html)
    * Relational Operators - Equality
* [Conditional if-else Statements](https://www.youtube.com/watch?v=395mlzouM00)

You'll have to translate the following English logic into Python:
_If_ the user's input is equal to the secret number, _then_ you should print out a message indicating that the user correctly hit the ship. _Else_, you should print out a statement that they missed the ship.

Your goal in this part is to be able to do the following:


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 2
    Guess a number between 1 and 4: 4
    Incorrect! You missed the ship.
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 3
    Guess a number between 1 and 4: 3
    Correct! You hit the ship.
</div>
</pre>


## Part 4. Printing A String of Boxes - 20 points

Now, let's bring a visual aid to the game! You will need to build up a string of emojis using concatenation to show where the user hit or missed a boat. You can use the following _named constants_ in your program to simplify your implementation. We will learn more about named constants soon, but for now know they are simply variables whose values you will not change later in your program and make your programs easier to read:

~~~
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
~~~

Next, create a `str` guess result variable and modify your current `if` and `else` statements in the following way:

_If_ the Player 2's guess matches Player 1's secret number, make the guess result variable red. _Else_, make the guess result variable white.

Now, you need to start building your string of emoji boxes. Establish another `str` variable to store the resulting emoji string of the guess and initialize it to an empty string.
Essentially, the default box should be blue, unless its the box position that the user correctly or incorrectly picked (red or white, respectively). In the future, you will use _loops_ to make this process more efficient, but for now, you will need a series of `if` statements to check each possible option. Here's an example for the first one:

_If_ Player 2's guess equals 1, concatenate the guess box to the resulting emoji string of boxes. _Else_, contatenate the blue box.

The logic is similar for all other possible box numbers. After checking for each posible box, print the resulting emoji string of boxes.

Your goal in this part is to be able to do the following:

<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 1
    Guess a number between 1 and 4: 3
    🟦🟦⬜🟦
    Incorrect! You missed the ship.
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex00_simple_battleship 
    Pick a secret boat location between 1 and 4: 2
    Guess a number between 1 and 4: 2
    🟦🟥🟦🟦
    Correct! You hit the ship.
</div>
</pre>


## Part 5. Exiting Early for Invalid Inputs - 10 points

Now that you've added more functionality to your program in Parts 3 and 4, what happens when you go back to Parts 1 and 2? If Player 1 inputs the wrong value, what happens? How about when Player 2 inputs the wrong value? You'll notice that you no longer get your expected outputs from Parts 1 and 2. Instead, the program keeps running and doesn't exit immediately.

It's good practice to handle bad input from an end-user gracefully in your programs. Our strategy, for now, will be to simply print an error message and then exit the program early. There is a special built-in function called `exit()` that will send a signal to your system and tell the program to quit at that point, not continuing on further in the program. Before attempting to implement the following behavior in your program, think about where it logically _makes sense_ to try adding these checks for correct input.

Once you make these changes, you should get the expected outputs from Parts 1 and 2 again, while still getting the correct functionality added in Parts 3 and 4.


## Part 6. Type Safety and Linting - 10 points

The autograder uses industry standard tools for checking the type safety of your programs (e.g. being sure you're using variables of the correct data types in valid ways) and linting style rules. If you have point deductions on Type Safety or Linting, read through the feedback the autograder gives and it should direct you to the line number in your program with the issue.

## Part 7. Hand Grading 

Part of this assignment will be hand graded to make sure you only use concepts within the course.

We expect you to implement this exercise using only the concepts covered in COMP110. If you have prior programming experience, restrict your implementation to only the concepts covered. While there are many ways to implement this program with additional concepts beyond those we have covered, you should not attempt to do so until after submitting this exercise for full credit once the autograder is posted. Gaining additional practice with the fundamentals may feel clunky, but will help ensure you have full command over the concepts we expect you to know. Additionally, it is good practice for working in other programming environments which are more constrained and require creativity to overcome restrictions. For this exercise, you will be penalized for using any kind of loop construct.

## Rubric

* Part 0. Setting up the Python Program - 10 points
* Part 1. Prompting for Player 1 Input - 15 points
* Part 2. Prompting for Player 2 Input - 15 points
* Part 3. Checking User Input for Match - 20 points
* Part 4. Printing A String of Boxes - 20 points
* Part 5. Exiting Early for Invalid Inputs - 10 points
* Part 6. Type Safety and Linting - 10 points

## Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Login to Gradescope and select the assignment named "EX01 - Chardle". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex00_simple_battleship.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex01_chardle.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 10 "human graded" points. Thus, you should expect a maximum autograding score of 90 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!