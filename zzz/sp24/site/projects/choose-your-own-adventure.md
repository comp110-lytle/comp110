---
title: PJ00 - Choose Your Own Adventure
author:
- Kris Jordan
page: projects
template: overview
---

In the first open-ended programming project, you will create a text-driven, "Choose Your Own Adventure" experience. 

Your project will need to satisfy many specifications, so before you begin programming be sure to read this project's write-up in full.

You are free to use your imagination to design and implement any experience you would like, as long as it meets the requirements. For some inspiration, here are some example ideas the UTA team and I came up with, if you are not feeling the spark of creativity:

1. Taking care of a virtual pet like a [tamagotchi](https://en.wikipedia.org/wiki/Tamagotchi). You are free to introduce additional variables, global or otherwise, for keeping track of a pet's health.
2. Some kind of role playing game where you choose what kinds of attacks or defenses to use and the opposing creature randomly chooses theirs. Points could be health or damage inflicted.
3. A number guessing game such as the generating a random number and asking the user to guess it and counting the number of attempts it takes them to guess it correctly.
4. A "buzzfeed quiz" that determines which Disney Princess character are (or anything else).
5. A coinflip guessing game where you have to choose heads or tails and see how many you can guess in a row correctly.
6. Some kind of mystery that involves searching a sequence of rooms.
7. Something heavily emoji based, perhaps as surprising as a [Japanese Game Show](https://en.wikipedia.org/wiki/Category:Japanese_game_shows)
8. A parody of something that is poignant satire (a student once made a ConnectCarolina registration parody that was pure, comedic gold)

Again, feel encouraged to come up with an idea that is uniquely your own!

## Background Lessons

The conceptual purpose of the game is to help you practice the concepts you have learned up to this point and explore some additional, related topics, including:

1. String Escape Sequences (for Emoji!)
2. String Interpolation (better than concatenation!)
3. Named Constants
4. Global Variables

As background preparation for this project, you should first complete the following lessons linked below:

1. [Strings](/lessons/strings.html)
2. [Scopes, Constants, Globals](/lessons/scopes-constants-globals.html)


## Getting Started

In your workspace's `projects` directory, create a file named `cyoa.py` for this Choose Your Own Adventure experience.

Begin by defining a `main` procedure that serves as the "entrypoint" to the program. The initial _call_ to `main` should be found at the end of your program, following Python's idiom:

~~~plaintext
if __name__ == "__main__":
  main()
~~~

## Specifications

These are the requirements for your project. Please read them in full and have a rough plan for how you will satisfy them all, before you begin working on your project.

### 0. Required Global variables (10 points total):

  0.0 Establish a global variable named `points` to track "adventure points". How you choose to use these adventure points is up to you. Initialize your global `points` variable from within your `main` function. (5 points -- autograded)

  0.1 Establish a global variable named `player` to track the player's name. (5 points -- autograded)

  These variables must have an explicit type declaration.

### 1. `main` function (10 points total):

  1.0 Define a `main` function, that returns `None`, and follows the Python idiom for calling `main` at the end of the program based on the dunderscore variable `__name__` being equal to `"__main__"`. (5 points -- autograded)

  1.1 After greeting the player using a call to the `greet` procedure, your `main` function should enter your experience. You should present the player with at least three options of where to go next and ask them to choose one. One of the three options should be to end the experience and print a goodbye message that includes the number of "adventure points" they accumulated in the experience. The other options should result in function calls which set the user off in different directions on the adventure. You will need to define appropriate functions for these distinct paths. (5 points -- hand graded)
  
### 2. `greet` procedure and welcome message (15 points total):

  2.0 Define a procedure, meaning a function that returns `None`, named `greet`. (5 points -- autograded)
  
  2.1 The `greet` function must print a welcome message to give some context to your game and asks the player for their name. You should call this procedure at the beginning of your `main` procedure. (5 points -- autograded)
  
  2.2 The `greet` function should assign the name input by the user to the global variable named `player`. (5 points -- hand graded)

### 3. At least one custom procedure (15 points total):
  One of the possible directions the player is set off in from `main` must be a procedure call.

  3.1 The procedure should lead to textual interaction(s) that make use of players name and ask the player for additional `input`. (10 points -- hand graded)

  3.2 The procedure should have logic to reassign the `points` global variable directly based on the user's choices. At a minimum, increase the adventure's points each time the player makes a choice.  (5 points -- hand graded)
  
  What happens within this procedure is up to you and you are free for this procedure call to lead to others, make use of loops, and so on. Get creative!

### 4. At least one custom function (15 points total):

  One of the other possible directions the player can choose to set off in from `main` should be a call to a function that takes an integer as a parameter and returns an integer. 
  
  4.1 The function takes at least one `int` as a parameter and returns an `int`. The call to this function from `main` should _pass_ the player's `points` value as an argument to the function call. (5 points -- hand graded)

  4.2 Like the previous procedure, you should make use of the `player` name in some output and have the user make at least one interaction choice that results in the points _parameter (local variable)_ changing. Ultimately, this function should return the player's total points after any interactions it leads to.  (5 points -- hand graded)
  
  4.3 The `main` function should use the returned value to update the global variable `points`. (5 points -- hand graded)

> Note: Requirements 3 and 4 are intentionally asking you to implement the same kinds of behavior but using two very different strategies in code for achieving them. The strategy in #3 relies on global variables shared between the main procedure and the function(s) you write. The strategy in #4 avoids the function(s) from directly accessing or reassigning the `points` global variable. There are trade-offs to each strategy. It is valuable to think through the trade-offs of both! 

### 5. Game loop (10 points total):

  5.0  Introduce a "game loop" in your `main` function. The game loop should allow the user to continue your experience and choose the same initial branch, or another branch, or to stop playing. Before looping, each time, you should update the user on their total number of points. (10 points -- hand graded)

### 6. Misc. Requirements (15 points total):

  6.0  You must make use of f-strings (formatted string literals) described in lecture 6 to produce any output that would otherwise require concatenation.  (5 points -- hand graded)

  6.1 You must define at least one global `NAMED_CONSTANT` and assign it the unicode escape sequence `"\U00000000"` for each Emoji you use. Strings such as these are considered "_magic numbers_", too! You are encouraged to make liberal use of Emoji throughout your adventure, they are fun!  (5 points -- hand graded)

  6.2 At least one path in your adventure must incorporate some element of randomness from the `random` library. (5 points -- hand graded)


Note: Your program should not have any global calls to the `input` function. Any user prompting/interaction should be inside of a function.

If you get an OSError from the grader, double check you have no global `input` calls and that your idiom is set up correctly per the "Getting Started" section above.


## Rubric

* 5 Points - Static Type Checks
* 5 Points - Linting
* 10 Points - `player` and `points` global variables correctly declared
* 10 points - `main` function allows user to choose one of three options
* 15 Points - `greet` function meets specification #2 above
* 15 Points - Procedure meeting specification #3 above
* 15 Points - Function meeting specification #4 above
* 10 Points - Game loop
* 5 Points - Used at least one emoji and setup a named constant for it
* 5 Points - Used f-strings for building string outputs rather than concatenation
* 5 Points - Incorporated randomness

## 3. Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged. Note that you do not have to make a backup in order to submit your work, though you are encouraged to before each submission so that you can revert back to a previous point in your project if you accidentally change something you did not intend to.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise 2" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.

## Submission Instructions

To prepare your scene for submission, be sure to add a docstring to your module (at the top of the file) and a global `__author__` variable set to a string which contains your 9-digit PID. Linting will also look for docstrings in your function definitions, per usual. 35 points of this assignment will be autograded, and the remaining 65 hand-granded.

Run `python -m tools.submission projects/cyoa.py` to build your submission zip for upload to Gradescope. Don't forget to backup your work by creating a commit and pushing it to GitHub. For a reminder of this process, see the previous exercises.