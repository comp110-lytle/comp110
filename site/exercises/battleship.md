---
title: EX03 - Battleship
author:
- Camilla Fratta
- Audrey Salmon
- Vrinda Desai
page: exercises
---

In this exercise, you will use the concept of *functions* to organize much of the functionality we developed in EX02. Moreover, rather than only getting one-attempt at guessing the secret boat location, you will get five! To get a sense of where you are going, here are two examples of the final game:

<pre>
<div class="terminal">
    $ python -m exercises.ex03_battleship
    Turn 1/5
    Guess a row: 2
    Guess a column: 1
    🟦🟦🟦🟦🟦
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Miss!
    Turn 2/5
    Guess a row: 2
    Guess a column: 4
    🟦🟦🟦🟦🟦
    🟦🟦🟦⬜🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Close! Correct column, wrong row.
    Turn 3/5
    Guess a row: 2
    Guess a column: 1
    🟦🟦🟦🟦🟦
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 4/5
    Guess a row: 3
    Guess a column: 9
    The grid is only 5 by 5. Try again: 6
    The grid is only 5 by 5. Try again: 4
    Hit!
    You won in 4/5 turns!
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟥🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦

    $ python -m exercises.ex03_battleship
    Turn 1/5
    Guess a column: 1
    Guess a row: 1
    Close! Right row, wrong column.
    ⬜🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 2/5
    Guess a column: 2
    Guess a row: 2
    🟦🟦🟦🟦🟦
    🟦⬜🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 3/5
    Guess a column: 3
    Guess a row: 3
    Close! Right column, wrong row.
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦⬜🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    Turn 4/5
    Guess a column: 4
    Guess a row: 4
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦🟦🟦
    🟦🟦🟦⬜🟦
    🟦🟦🟦🟦🟦
    Turn 5/5
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
    X/5 - Sorry, better luck next time!
</div>
</pre>

## Permitted Constructs

We expect you to implement this exercise using only the concepts covered in COMP110. If you have prior programming experience, restrict your implementation to only the concepts covered. While there are many ways to implement this program with additional concepts beyond those we have covered, you should not attempt to do so until after submitting this exercise for full credit once the autograder is posted. Gaining additional practice with the fundamentals may feel clunky, but will help ensure you have full command over the concepts we expect you to know. Additionally, it is good practice for working in other programming environments which are more constrained and require creativity to overcome restrictions. For this exercise, you will be penalized for using any kind of loop construct other than a `while` loop.

## Overview

In this program, you will implement a `main` function that contains Battleship's "game loop". The game loop is what controls the overall game logic:

The `main` fow of this game works as follows:

1. You have up to five turns
2. Each turn the player gets to `input_row` and `input_column` each within the bounds of the size of the grid.
    1. If either guess is out of bounds, you get to make additional guesses
3. The guess is compared with the secret row and column and `print_grid` / "codified" boxes are output
    1. Blue for rows & columns that don't exist in the secret.
    2. White for misses. If either the row or column match, provide a hint to the user.
    3. Red for hits where both the row and column match (`correct_guess`).
4. If the guess was correct, the game is over and the player wins
5. If the guess was incorrect, the game loop goes back to step 2 to continue with the next turn

Each of the four `monospace font-face` words above (`input_row`, `input_column`, `print_grid`, `correct_guess`) will be implemented as _functions_ to better structure your program into simple, reusable abstractions. Once you have created these building-blocks, you will put the together by calling them within the main function.

## Part 0. Setting up the Python Program

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex03_battleship.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you have previously. Then, you should add a line with the special variable named `__author__` assigned to be a **string** with your 9-digit student PID.

## Part 1. `input_row` and `input_column` - 10 points

Declare a function named `input_row`. The function will prompt for and eventually return the user's row guess. More specifically, the function takes in an `int` parameter, representing the size of the grid and has an `int` return type. The algorithm of this function is _very similar_ to the user input logic you have already used in EX02.

Once you have tried implementing the function, import it for use in the REPL to test it out. As featured in the example below, run the `python` command to start the REPL. Subsequently, the command `from exercises.ex03_battleship import input_row` will `import` your function definition `from` your `exercises.ex03_battleship`. Type out the example _function calls_ to check that your function returns the expected values. 

<pre>
<div class="terminal">
    $ python                         
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from exercises.ex03_battleship import input_row
    >>> input_row(4)
    Guess a row: 4
    4
    >>> input_row(3)
    Guess a row: 4
    The grid is only 3 by 3. Try again: 2
    2
    >>>quit()
</div>
</pre>

You will do essentially the same for the `input_columns` function. Give it a whirl!

<pre>
<div class="terminal">
    $ python                         
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from exercises.ex03_battleship import input_column
    >>> input_column(4)
    Guess a column: 0
    The grid is only 4 by 4. Try again: 1
    1
    >>> input_column(3)
    Guess a column: 3
    3
    >>>quit()
</div>
</pre>

## Part 2. `print_grid` - 20 points

Declare a function named `print_grid`. Given the size of the grid, the user's row and column guesses, and whether the guesses were correct, the function will print a grid of boxes to represent the game board. The function has:

1. An `int` parameter representing the size of the grid.
2. An `int` parameter representing the row guess.
3. An `int` parameter representing the column guess.
4. A `bool` parameter representing if the user's guess was correct.
5. A `None` return type. 

The body of this function should utilize the named constants you setup in EX02 for the colored emoji boxes. Just as before, you may test out this function in the REPL.

<pre>
<div class="terminal">
$ python
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from exercises.ex03_battleship import print_grid
>>> print_grid(4,3,2,True)
🟦🟦🟦🟦
🟦🟦🟦🟦
🟦🟥🟦🟦
🟦🟦🟦🟦
>>> print_grid(5,1,1,True)
🟥🟦🟦🟦🟦
🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦
>>> print_grid(4,3,2,False)
🟦🟦🟦🟦
🟦🟦🟦🟦
🟦⬜🟦🟦
🟦🟦🟦🟦
</div>
</pre>

Notice how your `print_grid` function contains all of the logic needed to create any sort of grid representation, given just a few pieces of information. This is the beauty of _abstraction_!

## Part 3. `correct_guess` -- 10 Points

Declare a function named `correct_guess`. Given the secret boat location and the user's guess, the function will return if the user was correct or not. The function should take in four `int` parameters representing the secret row, the secret column, the row guess, and the column guess, and it will return a `bool`.

<pre>
<div class="terminal">
    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_battleship import correct_guess
    >>> correct_guess(4,4,3,1) 
    False
    >>> correct_guess(3,2,1,2)
    False
    >>> correct_guess(1,1,1,1)
    True
    >>> correct_guess(2,3,2,3)
    True
    >>> quit()
</div>
</pre>

## Part 4. `main` -- 20 Points

Now, it's finally time to implement the `main` function that will pull together each of the smaller pieces that you created in your program. Similar to your other functions, the `main` functions has certain specifications including:

1. An `int` parameter for grid size.
2. An `int` paraemeter for secret row.
3. An `int` parameter for secret column.
4. A return type of `None`.

The "state" of a game refers to the variables you need to keep track of in memory in order to run the game. What variables do you need to keep track of? Define those inside of `main`'s body first.

Then, begin the game loop `while` the user still has turns left to play _and_ the user hasn't won yet, you will want to do the following:

1. Print the current turn number in a format such as `=== Turn 1/5 ===`
2. Prompt the user for a row and column guess, relying on your functions `input_row` and `input_column` to obtain a guess within the proper bounds.
3. Verify the user's guess using `correct_guess`.
4. Codify the emoji results of the user's guess by making use of your `print_grid` function. 
4. If the user's guess is correct, the user has won! Print `Hit!` and `You won in N/6 turns!` where N is replaced with the number of guesses it took. End the loop by updating the appropriate variables.
5. Otherwise, print `Miss!` and move on to the next turn.
6. If the user has exhuasted all turns,  print `X/6 - Better luck next time!` where `X` is literally the character `X` and end the game.

As you are working on `main`, you can save your work and import the `main` function just like the others and try calling it:

<pre>
<div class="terminal">
    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_battleship import main
    >>> main(4, 2, 1)
    === Turn 1/5 ===
    Guess a row: 3
    Guess a column: 3
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Miss!
    === Turn 2/5 ===
    Guess a row: 4
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    Miss!
    === Turn 3/5 ===
    Guess a row: 2
    Guess a column: 2
    🟦🟦🟦🟦
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!
    === Turn 4/5 ===
    Guess a row: 2
    Guess a column: 1
    🟦🟦🟦🟦
    🟥🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Hit!
    You won in 4/5 turns!
    >>> quit()

    $ python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_battleship import main
    >>> main(4, 4, 4)
    === Turn 1/5 ===
    Guess a row: 1
    Guess a column: 2
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!
    === Turn 2/5 ===
    Guess a row: 3
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    Miss!
    === Turn 3/5 ===
    Guess a row: 5
    The grid is only 4 by 4.
    Guess a row: 2
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!
    === Turn 4/5 ===
    Guess a row: 2
    Guess a column: 3
    Miss!
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    === Turn 5/5 ===
    Guess a row: 1
    Guess a column: 2
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!
    X/6 - Better luck next time!
    >>> quit()
</div>
</pre>

Once you have your `main` function and game loop working, there's only one bit of icing left to add to your delicious code cake. We will fully explain what is going on in the following code snippet soon, but for now note that this is an idiom common to Python programs like the one you have written. We will learn it does two things: 1. it makes it possible to run your Python program as a module (if you tried `python -m exercises.ex03_battleship` right now you would see nothing happens), and 2. it makes it possible for other modules to _import_ your functions and reuse them. Add the following snippet of code as the last 2 lines of your program (notice, there are two underscores _on both sides_ of the words `name` and `main`):

<pre>
<div class="terminal">
    if __name__ == "__main__":
        main()
</div>
</pre>

Now you can try running your game as a module and it should work: `python -m exercises.ex03_battleship`

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

Login to Gradescope and select the assignment named "EX03 - Structured Battleship". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex03_battleship.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex01_chardle.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 20 "human graded" points. Thus, you should expect a maximum autograding score of 80 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!