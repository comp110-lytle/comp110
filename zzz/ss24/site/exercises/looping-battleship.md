---
title: EX03 - Functional Battleship
author:
- Camilla Fratta
- Audrey Salmon
page: exercises
---

In this exercise, you will use the concept of *functions*, as well as those of the previous units. Please complete all lessons before attempting to begin this exercise.

In this exercise, you will prompt the user for a word that matches the length of your secret word. We'll use `"codes"` for the purposes of our examples and autograding. Just like in the previous exercise, your program will be able to work with a secret word of any length, though! After submitting to autograding for full credit, you should change your word and let your friends play your new and improved game.

You should follow the steps below for implementing the program function at a time. To get a sense of where you are going, here are two examples of the final game:

<pre>
<div class="terminal">
    $ python -m ex03_battleship
    Turn 1/6
    Guess a column: 1
    Guess a row: 2
    🟦🟦🟦🟦🟦
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Miss!
    Turn 2/6
    Guess a column: 4
    Guess a row: 2
    🟦🟦🟦🟦🟦
    🟦🟦🟦⬜🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Close! Correct column, wrong row.
    Turn 3/6
    Guess a column: 1
    Guess a row: 2
    🟦🟦🟦🟦🟦
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 4/6
    Guess a column: 9
    The grid is only 5 by 5.
    Guess a column: 6
    The grid is only 5 by 5.
    Guess a column: 4
    Guess a row: 3
    Hit!
    You won in 4/6 turns!
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟥🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦

    $ python -m ex03_battleship
    Turn 1/6
    Guess a column: 1
    Guess a row: 1
    Close! Right row, wrong column.
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 2/6
    Guess a column: 2
    Guess a row: 2
    🟦🟦🟦🟦🟦
    🟦⬜🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 3/6
    Guess a column: 3
    Guess a row: 3
    Close! Right column, wrong row.
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦⬜🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 4/6
    Guess a column: 4
    Guess a row: 4
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦⬜🟦
    🟦🟦🟦🟦🟦
    Turn 5/6
    Guess a column: 5
    Guess a row: 5
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦⬜
    Turn 6/6
    Guess a column: 6
    The grid is only 5 by 5.
    Guess a column: 6
    The grid is only 5 by 5.
    Guess a column: 5
    Guess a row: 4
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦⬜
    🟦🟦🟦🟦🟦
    Miss!
    X/6 - Sorry, try again tomorrow!
</div>
</pre>

## Permitted Constructs

We expect you to implement this exercise using only the concepts covered in COMP110. If you have prior programming experience, restrict your implementation to only the concepts covered. While there are many ways to implement this program with additional concepts beyond those we have covered, you should not attempt to do so until after submitting this exercise for full credit once the autograder is posted. Gaining additional practice with the fundamentals may feel clunky, but will help ensure you have full command over the concepts we expect you to know. Additionally, it is good practice for working in other programming environments which are more constrained and require creativity to overcome restrictions. For this exercise, you will be penalized for using any kind of loop construct other than a `while` loop. Additionally, the `in` operator, the `break` operator, and string methods (such as `.count` and `.format`) are not permitted.

## Overview

In this program, you will implement a `main` function that contains Battleship's "game loop". The game loop is what controls the overall game logic:

The `main` fow of this game works as follows:

1. You have up to six turns
2. Each turn the player gets to `input_row` and `input_column` each within the bounds of the size of the grid.
    1. If either guess is out of bounds, you get to make additional guesses
3. The guess is compared with the secret row and column and `print_grid` / "codified" boxes are output
    1. Blue for rows & columns that don't exist in the secret.
    2. White for misses. If either the row or column match, provide a hint to the user.
    3. Red for hits where both the row and column match (`correct_guess`).
4. If the guess was correct, the game is over and the player wins
5. If the guess was incorrect, the game loop goes back to step 2 for another `one_turn` and continues with next turn

Each of the five `monospace font-face` words above (`main`, `input_row`, `input_column`, `print_grid`, `correct_guess`, and `one_turn`) will be implemented as a _function_ definition to more logically structure the process of your program into simpler abstractions that can be reused.

You will start by building the smaller, simpler building-block functions first (`input_row`, `input_column`, `print_grid`, and `correct_guess` which helps you build `one_turn`), before finally bringing together `one_turn` for use in `main`'s game loop. This bottoms-up process helps us break down the problem into more manageable steps. Along the way, you will be refashioning the same algorithmic ideas you have already implemented in EX02, but in a program structured with functions.

## Part 0. Setting up the Python Program

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall, SS# for Summer Session.)

Open the Explorer pane (click the icon with two sheets of paper or to  _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click in the workspace directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex03_battleship.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you have previously. Then, you should add a line with the special variable named `__author__` assigned to be a **string** with your 9-digit student PID.

## Part 1. `input_row` and `input_column` - 10 points

Declare a function named `input_row`. Its purpose is when given the size of the grid, it will return an integer to get the user's guess for the row. It allows the user to guess until they choose a number within the bounds of the size of the grid.

More specifically, declare your `input_row` function such that:

1. It has one parameter (name it descriptively) that is an `int` the size of the grid.
2. An `int` return type
3. A doctring description the purpose of the function in your own words

The algorithm of this function is _very similar_ to the user input logic you have already used in EX02.

Once you have your best first attempt to implement this function, you can import it for use in the REPL to test it out. Save your work and then run the following commands:

<pre>
<div class="terminal">
    $ python                         
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from ta.battleship_3 import input_row
    >>> print(input_row(4))
    Guess a row: 4
    4

    >>> from ta.battleship_3 import input_row
    >>> print(input_row(3))
    Guess a row: 3
    3
</div>
</pre>

Notice, in the REPL, the line `from ex03_battleship import input_row` will `import` your function definition `from` your `ex03_battleship` so that you can make use of your function in the REPL. You can then type out example _function calls_ to test your implementation and be sure your function definition is returning the correct and expected values, as shown above. Your results must match exactly.

You will need to do essentially the same function for `input_columns`. Give it a whirl!

<pre>
<div class="terminal">
    $ python                         
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from ta.battleship_3 import input_column
    >>> print(input_row(4))
    Guess a row: 4
    4
    >>> from ta.battleship_3 import input_column
    >>> print(input_row(3))
    Guess a row: 3
    3
    >>>quit()
</div>
</pre>

## Part 2. `print_grid` - 20 points

Declare a function named `print_grid`. Its purpose is given a red or white box (hit or miss), the size of the grid, and the user's guess for the row and column, it will return a grid of boxes with the user's red or white box included. It _codifies_ the same as you previously implemented in EX02. You should reuse the name constants you setup in EX02 for the colored emoji boxes. The body of this function must make user of your `input_row` and `input_column` functions definitions by calling it to test for the user's input. Using this description, write your function header and docstring.

Once you have implemented this function, you can import it for use in the REPL to test it out, just like above. Be sure to save your work each time before restarting the `python` REPL, then try the following:

<pre>
<div class="terminal">
$ python
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from ta.battleship_3 import print_grid
>>> BLUE_BOX: str = "\U0001F7E6"
>>> RED_BOX: str = "\U0001F7E5"
>>> WHITE_BOX: str = "\U00002B1C"
>>> print(print_grid(RED_BOX,4,3,2))
🟦🟦🟦🟦
🟦🟦🟦🟦
🟦🟥🟦🟦
🟦🟦🟦🟦
None
>>> print(print_grid(RED_BOX,4,3,2))
🟦🟦🟦🟦
🟦🟦🟦🟦
🟦🟥🟦🟦
🟦🟦🟦🟦
None
>>> print(print_grid(WHITE_BOX,4,3,2))  
🟦🟦🟦🟦
🟦🟦🟦🟦
🟦⬜🟦🟦
🟦🟦🟦🟦
None
</div>
</pre>

Now you have a function that, given a row and column guess, will print out a resulting grid. Notice how your `print_grid` function makes use of the simpler `input_row` and `input_column` funtion to build up more complex behavior. This is the beauty of _abstraction_!

Once your `print_grid` function is working correctly as shown above, continue on.

## Part 3. `correct_guess` -- 10 Points

Declare a function named `correct_guess`. Its purpose is given a row and column, as well as a user's guess for a row and column, it one of four statement options: "Hit!", "Close! Right row, wrong column.", "Close! Right column, wrong row.", and "Miss!". It also returns a `bool` whether the user has won (`True`) or not (`False`).

<pre>
<div class="terminal">
    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ta.battleship_3 import correct_guess
    >>> print(correct_guess(3,2,3,1))  
    Close! Right row, wrong column.
    False
    >>> print(correct_guess(3,2,1,2))  
    Close! Right column, wrong row.
    False
    >>> print(correct_guess(3,2,1,1))  
    Miss!
    False
    >>> quit()
    >>> print(correct_guess(3,2,3,2))
    Hit!
    True
</div>
</pre>

## Part 4. `one_turn` - 10 Points

Declare a function named `one_turn`. Its purpose is given the size of a grid, a row and column where the boat is hidden, it will prompt the user for a guess row and column, and execute one round of the game, including printing the grid. Make `one_turn` return a `str` (you'll get why below). The implementation of this function will behave very similarly to your logic in EX02.

In this version of battleship, you will allow the user to have 6 turns before exiting the game. In order to keep track of previous guesses (that are misses), create a new empty string variable in the function. Then, if the guess is a miss, update that variable with an f-string of the "coordinates" of the guess. Then, return that string. In the game loop, you'll improve this tracking.

Once you have implemented this function, you can import it for use in the REPL just like the examples above. Be sure to save your work before restarting the `python` REPL, then try the following:

<pre>
<div class="terminal">
    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ta.battleship_3 import one_turn
    >>> print(one_turn(4,3,2))
    Guess a row: 1
    Guess a column: 1
    Miss!
    ⬜🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    (row: 1, column: 1)
    >>> print(one_turn(4,3,2))
    Guess a row: 2
    Guess a column: 3
    Miss!
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    (row: 2, column: 3)
    >>> print(one_turn(4,3,2))
    Guess a row: 6
    The grid is only 4 by 4.
    Guess a row: 4
    Guess a column: 9
    The grid is only 4 by 4.
    Guess a column: 2
    Close! Right column, wrong row.    
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦⬜🟦🟦
    (row: 4, column: 2)
    >>> print(one_turn(4,3,2))
    Guess a row: 3
    Guess a column: 2
    Hit!
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟥🟦🟦
    🟦🟦🟦🟦
    >>> quit()
</div>
</pre>

## Part 5. `main` -- 20 Points

Now it's time to pull together your functions, which are building blocks, into a `main` function that implements the high-level logic of the World game loop. The purpose of the `main` function is to establish what the secret row and columns are as a variable, keep track of how many turns the user has spent, whether the use has won the game, and control the flow of the game.

The declaration of your `main` function is unlike the functions above because it will not have any parameters and it will return `None`. You can declare your main function as follows:

<pre>
<div class="terminal">
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
</div>
</pre>

The "state" of a game refers to the variables you need to keep track of in memory in order to run the game. What variables do you need to keep track of? Define those inside of `main`'s body first.

Then, begin the game loop `while` the user still has turns left to play _and_ the user hasn't won yet, you will want to do the following:

1. Print the current turn number in a format such as `=== Turn 1/6 ===`
2. Prompt the user for a row and column guess, relying on your functions `input_row` and `input_column` to obtain a guess within bounds.
3. Codify the emoji results of the user's guess by making use of your `print_grid` function. Print the resulting codified string.
4. If the user's guess _is_ the secret, the user has won!
5. Otherwise, move on to the next turn, making use of your `one_turn` function.

After the game loop, if the user won, print `You won in N/6 turns!` where N is replaced with the number of guesses it took to get the word. Otherwise, when the user does not guess the word in 6 or fewer guesses, print the following message: `X/6 - Sorry, try again tomorrow!` where `X` is literally the character `X`.

Let's also come back to the previous guesses. Add a new `str` variable in `main` which you'll be updating with other guesses. You should be able to update this string with simple concatination. Hint: check the return type of `one_turn`.

As you are working on `main`, you can save your work and import the `main` function just like the others and try calling it:

<pre>
<div class="terminal">
    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ex03_battleship import main
    >>> main()
    === Turn 1/6 ===
    Guess a row: 3
    Guess a column: 3
    Miss!
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 3, column: 3)
    === Turn 2/6 ===
    Guess a row: 4
    Guess a column: 4
    Miss!
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    Previous guesses: (row: 3, column: 3) (row: 4, column: 4)
    === Turn 3/6 ===
    Guess a row: 2
    Guess a column: 2
    Close! Right row, wrong column.
    🟦🟦🟦🟦
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 3, column: 3) (row: 4, column: 4) (row: 2, column 2)
    === Turn 4/6 ===
    Guess a row: 2
    Guess a column: 1
    Hit!
    🟦🟦🟦🟦
    🟥🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    You won in 4/6 turns!
    >>> quit()

    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ex03_battleship import main
    >>> main()
    === Turn 1/6 ===
    Guess a row: 1
    Guess a column: 2
    Close! Right row, wrong column.
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 1, column: 2)
    === Turn 2/6 ===
    Guess a row: 3
    Guess a column: 4
    Close! Right column, wrong row.
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    Previous guesses: (row: 1, column: 2) (row: 3, column: 4)
    === Turn 3/6 ===
    Guess a row: 5
    The grid is only 4 by 4.
    Guess a row: 2
    Guess a column: 4
    Close! Right column, wrong row.
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 1, column: 2) (row: 3, column: 4) (row: 2, column: 4)
    === Turn 4/6 ===
    Guess a row: 2
    Guess a column: 3
    Miss!
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 1, column: 2) (row: 3, column: 4) (row: 2, column: 4) (row: 2, column: 3)
    === Turn 5/6 ===
    Guess a row: 1
    Guess a column: 2
    Close! Right row, wrong column.
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Previous guesses: (row: 1, column: 2) (row: 3, column: 4) (row: 2, column: 4) (row: 2, column: 3) (row: 1, column: 2)

    === Turn 6/6 ===
    Guess a row: 4
    Guess a column: 3
    Miss!
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    Previous guesses: (row: 1, column: 2) (row: 3, column: 4) (row: 2, column: 4) (row: 2, column: 3) (row: 1, column: 2) (row: 4, column: 3)
    X/6 - Sorry, try again!
    >>> quit()
</div>
</pre>

Once you have your `main` function and game loop working, there's only one bit of icing left to add to your delicious code cake. We will fully explain what is going on in the following code snippet soon, but for now note that this is an idiom common to Python programs like the one you have written. We will learn it does two things: 1. it makes it possible to run your Python program as a module (if you tried `python -m ex03_battleship` right now you would see nothing happens), and 2. it makes it possible for other modules to _import_ your functions and reuse them. Add the following snippet of code as the last 2 lines of your program (notice, there are two underscores _on both sides_ of the words `name` and `main`):

<pre>
<div class="terminal">
    if __name__ == "__main__":
        main()
</div>
</pre>

Now you can try running your game as a module and it should work: `python -m ex03_battleship`

Congratulations on writing your first _structured_ program in COMP110!

## Part 5. Style and Documentation Requirements -- 20 Points (Manually Graded)

We will manually grade your code and are looking for good choices of meaningful variable names. Your variable names should be descriptive of their purposes. (Loop indexing variables can be short, such as `i`, or `idx`.) You should also use the Python `snake_case` convention where variable names are all lowercase and new words are separated by underscores.

You should add code comments in your own English words to describe what is happening at important stages of your program.

Your program should work regardless of the size of the grid. Thus, you should not have any hard-coded numbers (such as `3` for `guess_row`). All numbers that appear in output and the boundaries of loops should be based on the `size` of your grid.

## Part 6. Type Safety and Linting - 9 Points

The autograder uses industry standard tools for checking the type safety of your programs (e.g. being sure you're using variables of the correct data types in valid ways) and linting style rules. If you have point deductions on Type Safety or Linting, read through the feedback the autograder gives and it should direct you to the line number in your program with the issue.

## Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise N" will suffice, where N is the current exercise.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.


## Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Login to Gradescope and select the assignment named "EX03 - Structured Wordle". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission ex03_battleship.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-ex03_battleship.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 20 "human graded" points. Thus, you should expect a maximum autograding score of 80 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!