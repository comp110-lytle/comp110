---
title: EX03 - Structured Wordle
author:
- Kris Jordan
- Alyssa Byrnes
- Viktorya Hunanyan
page: exercises
template: overview
---

In this exercise, you will use the concept of *loops*, as well as the concepts from previous units. Please complete all lessons before beginning this exercise.

The next step in our journey to implementing [Wordle](https://www.powerlanguage.co.uk/wordle/) is to create a program that allows the player to make six guesses at your program's secret word and provides an emoji representation of the accuracy of each guess, just like in the real game.

In this exercise, you will prompt the user for a word that matches the length of your secret word. We'll use `"codes"` for the purposes of our examples and autograding. Just like in the previous exercise, your program should work with a secret word of any length! After submitting to autograding for full credit, you should change your word and let your friends play your new and improved game.

Follow the steps below to implement the program, one function at a time. To get a sense of where you are headed, here are two examples of the final game:

~~~ {.plaintext}
    $ python -m exercises.ex03_wordle
    === Turn 1/6 ===
    Enter a 5 character word: dukes
    🟨⬜⬜🟩🟩
    === Turn 2/6 ===
    Enter a 5 character word: gonna
    ⬜🟩⬜⬜⬜
    === Turn 3/6 ===
    Enter a 5 character word: lose
    That wasn't 5 chars! Try again: loser
    ⬜🟩🟨🟩⬜
    === Turn 4/6 ===
    Enter a 5 character word: tounc
    ⬜🟩⬜⬜🟨
    === Turn 5/6 ===
    Enter a 5 character word: saturday
    That wasn't 5 chars! Try again: sat 
    That wasn't 5 chars! Try again: stday
    🟨⬜🟩⬜⬜
    === Turn 6/6 ===
    Enter a 5 character word: biscuits
    That wasn't 5 chars! Try again: bscts
    ⬜🟨🟨⬜🟩
    X/6 - Sorry, try again tomorrow!

    $ python -m exercises.ex03_wordle
    === Turn 1/6 ===
    Enter a 5 character word: ideas
    ⬜🟨🟨⬜🟩
    === Turn 2/6 ===
    Enter a 5 character word: doges
    🟨🟩⬜🟩🟩
    === Turn 3/6 ===
    Enter a 5 character word: codes
    🟩🟩🟩🟩🟩
    You won in 3/6 turns!
~~~

## Background Lesson: Advanced String Concepts

In this exercise you will need to make use of a few advanced string concepts:

1. Emoji! 🤠
2. Formatted Strings (f-Strings)

Before beginning work on this exercise, read the following lesson and complete the related questions on Gradescope: [LS11 - Unicode, Emoji, Escape Sequences, and f-Strings](/lessons/strings.html)

## Permitted Constructs

We expect you to implement this exercise using only the concepts covered in COMP110. If you have prior programming experience, restrict your implementation to only the concepts covered. While there are many ways to implement this program with additional concepts beyond those we have covered, you should not attempt to do so until after submitting this exercise for full credit once the autograder is posted. Gaining additional practice with the fundamentals may feel clunky, but will help ensure you have full command over the concepts we expect you to know. Additionally, it is good practice for working in other programming environments which are more constrained and require creativity to overcome restrictions. For this exercise, you will be penalized for using any kind of loop construct other than a `while` loop. Additionally, the `in` operator, the `break` operator, and string methods (such as `.count` and `.format`) are not permitted.

## Overview

In this program you will implement a `main` function that contains Wordle's "game loop". The game loop is what controls the overall game logic:

The `main` flow of the game works as follows:

1. You have up to six turns
2. Each turn, the player gets to `input_guess` of the same length of the secret word
    1. If the guess is a different length than the secret word, you get to make additional guesses
3. The guess is compared with the secret and `emojified` / "codified" boxes are output
    1. White for letters that don't exist in the secret
    2. Green for letters that match the secret at the same position
    3. Yellow for each guessed letter the secret `contains_char`, but at a different position
4. If the guess was correct, the game is over and the player wins
5. If the guess was incorrect, the game loops back to step 2 and continues with the next turn

Each of the four `monospace font-face` words above (`main`, `input_guess`, `emojified`, and `contains_char`) will be implemented as a _function_ definition to more logically structure the process of your program into simpler abstractions that can be reused.

Along the way, you will be refining the same algorithmic ideas you implemented in EX02, but in a more versatile and structured program.

**Important:** As you progress through the exercise, comment your code! As a general rule, if 2 or more minutes are spent thinking about how to write a particular line or block of code, it’s a good idea to add a comment. Commenting is mandatory as it should be an integral part of the problem-solving process. More information on how commenting will be graded can be found in part 5. 

## Part 0. Setting up the Python Program

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match capitalization and punctuation:

* `ex03_wordle.py`

Before beginning work on the program, you should add a _docstring_ to the top of your Python _module_ just as you have previously. Then, you should add a line with the special variable named `__author__` assigned to a **string** containing your 9-digit student PID.


## Part 1. `input_guess` -- 10 Points

Declare a function named `input_guess`. This function will prompt the user to enter a guess and continue prompting them until they provide a guess of the correct length, specified by the function's parameter. The parameter is an `int` that holds the value of the number of characters the guess should contain, which corresponds to the length of the secret word.

In the previous exercise, EX02, we prompted the user for a secret word using the `input_word` function and then prompted the user for a character guess through the `input_letter` function. In both cases, we checked the validity of the length of the input. This time, since we are replicating the game Wordle, the guess word must be the same length as the secret word. Therefore, we only need one function to ensure the guess matches the length of the secret word. Everything in this game is relative to the secret word!

Once you have implemented this function, you can import it for use in the REPL just like the examples above. Be sure to save your work before restarting the `python` REPL, then try the following:

~~~ {.plaintext}
    $ python
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_wordle import input_guess
    >>> print(input_guess(secret_word_len=5))
    Enter a 5 character word: gthd
    That wasn't 5 chars! Try again: gdtbath
    That wasn't 5 chars! Try again: gounc
    gounc
    >>> print(input_guess(secret_word_len=5))
    Enter a 6 character word: gthd
    That wasn't 6 chars! Try again: gdtbath
    That wasn't 6 chars! Try again: goheel
    goheel
    >>> print(input_guess(secret_word_len=5))
    Enter a 7 character word: goheels
    goheels
    >>> quit()
~~~

As seen in the example usage, if the user provides a guess with an incorrect length, the function will *loop*, prompting them to try again until they provide a word of the correct length.

Notice that as the function receives new inputs, the string outputs adjust accordingly. Be sure to use `f-string` templates for this output, as introduced in the background lesson, rather than using string concatenation.


## Part 2. `contains_char` - 10 points

In EX02, we defined a function `contains_char`. This function was designed to check whether a specific character (provided as a single-character string) was present at any index within a given word (provided as a string). The function manually checked each index of the word (using multiple `if` statements), assuming a fixed length of 5 for the word. If the character was found, it printed a message indicating the index or indices where the match occurred.

Now, we will be defining a similar function with some modifications. Instead of printing the indices where the character is found, this new function will test each index of the first parameter string to see if it matches the second parameter. If a match is found, the function should return `True`. If the character is not found after checking all indices, the function should return `False`. Additionally, this function will be versatile, meaning it should work with words of any length, not just those of a fixed length.

Declare a function named `contains_char` with the following specifications:

1. It has two parameters (name them descriptively)
    1. A string that is being searched through for occurences of the second parameter. 
    2. A string that is expected to be a single character in length and is the character being searched for
2. A boolean return type
3. A docstring describing the purpose of the function in your own words

Since the caller of this function can be expected to provide the correct arguments, specifically a second argument whose length is one, we will "assert" this assumption in our code such that an error is raised if it is not found to be true. As the first line of code in your function's body, add the following assert statement and fill in the blank (`_____`) with your second parameter's name:

`assert len(_______) == 1`

Once you have your best first attempt to implement this function, you can import it for use in the REPL to test it out. Save your work and then run the following commands:

~~~ {.plaintext}
    $ python                         
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from exercises.ex03_wordle import contains_char
    >>> print(contains_char(secret_word="abc", char_guess="b"))
    True
    >>> print(contains_char(secret_word="abc", char_guess="c"))
    True
    >>> print(contains_char(secret_word="abc", char_guess="a"))
    True
    >>> print(contains_char(secret_word="abc", char_guess="z"))
    False
    >>> print(contains_char(secret_word="abc", char_guess="zz"))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "......../exercises/ex03_wordle.py", line 48, in contains_char
        assert len(needle) == 1
    AssertionError
    >>> quit()
~~~

Notice, in the REPL, the line `from exercises.ex03_wordle import contains_char` will `import` your function definition `from` your `exercises.ex03_wordle` so that you can make use of your function in the REPL. You can then type out example _function calls_ to test your implementation and be sure your function definition is returning the correct and expected values, as shown above. Your results must match exactly (except for the ellipses File details near the AssertionError).

## Part 3. `emojified` - 20 points

For this next part, we will use emojis to visually represent the accuracy of a guess in relation to a secret word. The function will use colored emojis to indicate whether a character in the guess is in the correct position (green), present but in the wrong position (yellow), or not present at all (white). Unlike the previous functions, this concept introduces a new way to visualize the results using emojis!

Declare a function named `emojified`. Its purpose is to compare two strings of equal length—-the first being the user's guess and the second being the secret word. The function will return a string composed of emojis. Go ahead and add a docstring describing what the function will do (you can do this at the end once you get a better idea of how the function works but don't forget). 

Since you can reasonably expect anyone using this function to provide strings of equal length, you can add the following assertion as the first line of your function implementation following your docstring, replacing the capitalized words with your function's parameter's names:

`assert len(REPLACE_THIS_WITH_YOUR_GUESS_PARAMETERS_NAME) == len(REPLACE_THIS_WITH_YOUR_SECRET_PARAMETERS_NAME)`

For each index you check, you will need to build up a string using concatenation of emojis. You can use the following _named constants_ in your program to simplify your implementation. We will learn more about named constants soon, but for now know they are simply variables whose values you will not change later in your program and make your programs easier to read:

~~~ {.plaintext}
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
~~~

Your function should use a `while` loop to test each index of secret words of arbitrary lengths. Additionally, the body of this function must use `contains_char` to determine whether to use yellow or white box emojis. Consider the following scenarios to guide you toward the correct implementation:

1. *If* the character at the current index of the guess word matches the character at the same index in the secret word, what should you do?

2. **When** the _first scenario is not met_, you should check if the character of the guess word is present in the secret word. *If* it is, what should you do? How will you know the character at the current index is present in the secret word?

3. **When** _neither of the above scenarios are met_, this means the character at the current index in the guess word is not present in the secret word at all. In this case, what should you do?


Once you have implemented this function, you can import it for use in the REPL to test it out, just like above. Be sure to save your work each time before restarting the `python` REPL, then try the following:
~~~ {.plaintext}
    $ python
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_wordle import emojified
    >>> print(emojified(guess="hello", secret="world"))
    ⬜⬜🟨🟩🟨
    >>> print(emojified(guess="elloh", secret="hello"))
    🟨🟨🟩🟨🟨
    >>> print(emojified(guess="python", secret="wohoo"))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "......../exercises/ex03_wordle.py", line 33, in emojified
        assert len(guess) == len(secret)
    AssertionError
    >>> print(emojified(guess="python", secret="woohoo"))
    ⬜⬜⬜🟩🟩⬜
    >>> print(emojified(guess="python", secret="python"))
    🟩🟩🟩🟩🟩🟩
    >>> print(emojified(guess="yikyak", secret="tiktok"))
    ⬜🟩🟩⬜⬜🟩
    >>> quit()
~~~

Now you have a function that, given a guess and a secret of the same length, will Wordle emojify the results of the guess! Notice how your `emojified` function makes use of the simpler `contains_char` function to build up more complex behavior. This is the beauty of abstraction!

Once your `emojified` function is working correctly, as shown above, continue on.


## Part 4. `main` -- 30 Points

Now it’s time to bring together your functions into a `main` function that handles the high-level logic of the Wordle game loop. The `main` function will set the secret word as a variable (use `"codes"` for autograding), track the number of turns the user has taken, determine if the user has won the game, and manage the flow of the game.

The declaration of your `main` function is unlike the functions above because it will not have any parameters and it will return `None`. You can decare your main function as follows:

~~~ {.plaintext}
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
~~~

The "state" of a game refers to the variables you need to keep track of in memory in order to run the game. What variables do you need to keep track of? Define those inside of `main`'s body first.

Then, begin the game loop `while` the user still has turns left to play _and_ has not yet won, you will want to do the following:

1. Print the current turn number in a format such as `=== Turn 1/6 ===`
2. Prompt the user for a guess, relying on your function `input_guess` to obtain a guess of the correct length.
3. Codify the emoji results of the user's guess versus the secret by making use of your `emojified` function. Print the resulting codified string.
3. If the user's guess _is_ the secret, the user has won!
5. Otherwise, move on to the next turn.

After the game loop, if the user won, print `You won in N/6 turns!` where N is replaced with the number of guesses it took to get the word. Otherwise, when the user does not guess the word in 6 or fewer guesses, print the following message: `X/6 - Sorry, try again tomorrow!` where `X` is literally the character `X`.

As you are working on `main`, you can save your work and import the `main` function just like the others to try calling it:

~~~ {.plaintext}
    $ python
    Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from exercises.ex03_wordle import main
    >>> main()
    === Turn 1/6 ===
    Enter a 5 character word: ideas
    ⬜🟨🟨⬜🟩
    === Turn 2/6 ===
    Enter a 5 character word: codes
    🟩🟩🟩🟩🟩
    You won in 2/6 turns!

    >>> main()
    === Turn 1/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    === Turn 2/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    === Turn 3/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    === Turn 4/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    === Turn 5/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    === Turn 6/6 ===
    Enter a 5 character word: wohoo
    ⬜🟩⬜🟨🟨
    X/6 - Sorry, try again tomorrow!

    >>> quit()
~~~

Once you have your `main` function and game loop working, there's only one last part. Just like with EX02, add the following snippet of code as the last 2 lines of your program (notice, there are two underscores _on both sides_ of the words `name` and `main`):

~~~ {.plaintex}
if __name__ == "__main__":
    main()
~~~

As mentioned before, we will fully explain what is going on in the following code snippet soon, but for now note that this is an idiom common to Python programs like the one you have written. We will learn it does two things: 1. it makes it possible to run your Python program as a module (if you tried `python -m exercises.ex03_wordle` right now you would see nothing happens), and 2. it makes it possible for other modules to _import_ your functions and reuse them. 

Now you can try running your game as a module and it should work: `python -m exercises.ex03_wordle`

Congratulations on writing your first _structured_ program in COMP110!

## Part 5. Style and Documentation Requirements -- 20 Points (Manually Graded)

We will manually grade your code and are looking for good choices of meaningful variable names. Your variable names should be descriptive of their purposes. (Loop indexing variables can be short, such as `i`, or `idx`.) You should also use the Python `snake_case` convention where variable names are all lowercase and new words are separated by underscores.

You should add code comments in your own English words to describe what is happening at important stages of your program.

Your program should work regardless of the secret's length. Thus, you should not have any hard-coded numbers (such as `6` for `"python"`). All numbers that appear in output and the boundaries of loops should be based on the `len`-gth of your secret word.

As part of the manual grading, we will be looking to see if you have commented on your code! No comments imply that there were no challenges or moments spent considering how to approach a code. It is quite rare to complete every exercise, challenge question, and practice problem without engaging in some form of problem-solving. Even the most experienced programmers use a piece of paper to map out their approach when working on practice problems, often leading to comments being added to code. 

As a general rule, if 2 or more minutes are spent thinking about how to write a particular line or block of code, it’s a good idea to add a comment. Explain what’s happening on that line, how the solution was reached, the reasoning behind the approach, or provide a note for future reference to recall the problem-solving steps. If you received help from office hours or tutoring, go back to the code you were stuck on and explain it to yourself. If you see that you need a second to understand what is going on, comment! 

Comments don't need to be extensive, but they should reflect a genuine effort to explain the process in your own words. Commenting should be an integral part of the problem-solving process. 

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

`python -m tools.submission exercises/ex03_wordle.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex01_chardle.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 20 "human graded" points. Thus, you should expect a maximum autograding score of 80 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!