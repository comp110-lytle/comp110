---
title: EX02 - One Shot Battleship
author:
- Camilla Fratta
- Audrey Salmon
page: exercises
template: overview
---

## Overview

Please complete all lessons before attempting to begin this exercise.

The next step on our journey to implementing Battleship is to produce a program that gives the player one shot at guessing your program's secret word. (Of couse, they can play the game multiple times in order to have multiple chances.)

In this exercise, you will print out a grid of boxes instead of just one line, and prompt the user for a **row** and **column** for their guess. Level up!

You should follow the steps below for implementing the program one step at a time. To get a sense of where you are going, here is an example of a final game ():

<pre>
<div class="terminal">
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 2
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 1
    Guess a column: 2
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Close! Right column, wrong row.

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 3
    Guess a column: 3
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Close! Right row, wrong column.
    
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 5
    The grid is only 4 by 4.
    Guess a row: 3
    Guess a column: 6
    The grid is only 4 by 4.
    Guess a column: 2
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟥🟦🟦
    🟦🟦🟦🟦
    Hit!
</div>
</pre>

Note: each time you run the game, the random secret row and column are regenerated. You might want to hard code your secret row and column for the testing of your program and then switch them back to random at the end!

## Permitted Constructs

We expect you to implement this exercise using only the concepts covered in COMP110. If you have prior programming experience, restrict your implementation to only the concepts covered. While there are many ways to implement this program with additional concepts beyond those we have covered, you should not attempt to do so until after submitting this exercise for full credit once the autograder is posted. Gaining additional practice with the fundamentals may feel clunky, but will help ensure you have full command over the concepts we expect you to know. Additionally, it is good practice for working in other programming environments which are more constrained and require creativity to overcome restrictions. For this exercise, you will be penalized for using any kind of loop construct other than a `while` loop. Additionally, string methods (such as `.count` and `.format`) are not permitted.

## Background Lesson: Formatted Strings (f-Strings)

In this exercise, you will need to make use of another advanced string concept: formatted Strings (f-Strings)

Before beginning work on this exercise, you might want to reread the following lesson: [LS11 - Unicode, Emoji, Escape Sequences, and f-Strings](/lessons/strings.html)

## Part 0. Setting up the Python Program

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex02_one_shot_battleship.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you did in EX00 and EX01. Then, you should add a line with the special variable named `__author__` assigned to be a **string** with your 9-digit student PID. (Disclaimer: Out in the real world the `__author__` variable is typically your name and e-mail address, but since we will grade your programs we'd like to avoid potential bias in seeing your names as part of the programs as we're grading.) Fill in _your_ 9-digit UNC PID number, without any spaces or dashes, in the `__author__` string.

## Part 1. Print a Grid -- XX Points

In battleship, you normally have a grid instead of just one row of ocean. Using the concept of `while` loops, you'll be able to print out a grid of the size of your choice!

First, you'll need to establish a few variables: an `int` for the size of your grid, `int` for secret row, `int` for secret column, `i` as a counter, and `bool` for whether the user has made a correct guess (initialize that to `False`).

For debugging purposes, hard code your secret row and secret column to 3 and 2 respectively.

Since loops are new to your repertoire, in this exercise we will give you a general strategy for accomplishing this task. Your job will be to translate this plan in English into working Python code.

1. First, establish a variable to keep track how many times you've gone through the loop to print a row.
2. _While_ the counter variable is less than the size of the grid you specified, do as follows:
    1. Test to see if the user guess for row is equal to the counter + 1 -- This is because :
        1. If so, create a another counter variable to count how many times you've printed a row.
            1. You'll also want to create a `str` to keep track of your emoji boxes.
            2. _While_ your row counter variable is less than the size of the grid, do as follows (creates a row):
                1. If the user guess for column is equal to the counter + 1, concatenate the user guess box (red or white)
                2. Else, add a blue box.
                3. After the test, increase your counter variable by one so that you do not have an infinite loop.
            3. Once the loop completes, print the emoji string. (One row.)
        2. Otherwise, still create the counter variable and the `str` variable, but this time, use the following `while` loop logic:
            1. _While_ the counter variable is less than the size of the grid, do the following (prints each row as its created):
                1. Concatenate a blue box.
                2. Increment your counter variable by one to avoid an infinite loop.
            2. When you exit the while loop, print the emoji string.
    2. Increment your first counter variable by one to avoid an infinite loop.

Once you have completed this part of the program, your output should look as follows (should the secret row be 3 and column be 2.)

<pre>
<div class="terminal">
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 2
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 3
    Guess a column: 3
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Miss!
    
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 3
    Guess a column: 2
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟥🟦🟦
    🟦🟦🟦🟦
    Hit!
</div>
</pre>


## Part 2. Establishing a Secret and Prompting for a Guess -- 30 Points

Now that you have your grid printing out, how about we add some hints to help your user. First one, the ability to try again after an invalid input!

In simple battleship, you would exit if the user gave an invalid input. Now, with the help of `while` loops, see if you can continue to prompt the player until the provide a guess that within the bounds of the size of the grid you pick. Here's how your program should perform after this step:

<pre>
<div class="terminal">
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 5
    The grid is only 4 by 4. Try again:
    Guess a row: 3
    Guess a column: 6
    The grid is only 4 by 4. Try again:
    Guess a column: 2
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟥🟦🟦
    🟦🟦🟦🟦
    Hit!

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 5
    The grid is only 4 by 4. Try again:
    Guess a row: 12390
    The grid is only 4 by 4. Try again:
    Guess a row: 3
    Guess a column: 123589
    The grid is only 4 by 4. Try again:
    Guess a column: 2
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Miss!
</div>
</pre>

Before you continue on, does this step of your program work correctly if you change the value for the size of your grid? What if you make the size 5, and thus the grid 5 by 5? Make sure you're using the variable for size to compare, and not hard code it!

Additionally, be sure you are using `f-String` templates rather than conatenation for this text output (not the grid), as introduced in the background lesson.

**WARNING:** Autograding will very specifically be looking for _exactly_ the format of lines output shown above. You will not see the `$` at your command-line prompt in VSCode, you can ignore that part. Otherwise, when you run the program on your machine with the same inputs as above on the first two lines, your printed results should look exactly like it.

## Part 3. Giving A Hint to Your User -- XX Points

What if your user was so close? Correct row, but wrong column? Correct column, but wrong row?

Add a couple `elif` statements to your user feedback ("Hit!" and "Miss" logic). Your program should perform like this after this step (if the secret row is 3 and column is 2):

<pre>
<div class="terminal">
    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 2
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Miss!

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 1
    Guess a column: 2
    🟦⬜🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    Close! Right column, wrong row.

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 3
    Guess a column: 4
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦🟦⬜
    🟦🟦🟦🟦
    Close! Right row, wrong column.

    $ python -m exercises.ex01_one_shot_battleship
    Guess a row: 5
    The grid is only 4 by 4. Try again:
    Guess a row: 3
    Guess a column: 3
    🟦🟦🟦🟦
    🟦🟦🟦🟦
    🟦🟦⬜🟦
    🟦🟦🟦🟦
    Close! Right row, wrong column.
</div>
</pre>

And there you have your one-shot battleship! Feel free to add the randomization back in for your secret row and secret column. Make sure that your keeping into account the size of your grid, which is flexible . . . what should the max value be for secret row and secret column?

## Part 4. Style and Documentation Requirements -- 20 Points (Manually Graded)

We will manually grade your code and are looking for good choices of meaningful variable names. Your variable names should be descriptive of their purposes. (Loop indexing variables can be short, such as `i`, or `idx`.) You should also use the Python `snake_case` convention where variable names are all lowercase and new words are separated by underscores.

You should add code comments in your own English words to describe what is happening at important stages of your program.

Your program should work regardless of the secret's length. Thus, you should not have any hard-coded numbers (such as `3` for the secret row). All numbers that appear in output and the boundaries of loops should be based on the size of your grid (of your choice).

## Part 5. Type Safety and Linting - 9 Points

The autograder uses industry standard tools for checking the type safety of your programs (e.g. being sure you're using variables of the correct data types in valid ways) and linting style rules. If you have point deductions on Type Safety or Linting, read through the feedback the autograder gives and it should direct you to the line number in your program with the issue.

## Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise 1" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.


## Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Login to Gradescope and select the assignment named "EX02 - One-shot Wordle". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex02_one_shot_battleship.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex02_one_shot_wordle.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 20 "human graded" points. Thus, you should expect a maximum autograding score of 80 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!