---
title: EX00 - Hello, world.
author:
- Kris Jordan
- Kaki Ryan
- Alyssa Byrnes
page: exercises
template: overview
---

Welcome to COMP110 - Introduction to Programming at UNC Chapel Hill!

## 0. Complete the Prerequisites

Before continuing on, be sure you've completed each of the following steps to prepare your computer for the course's programming assignments:

0. [Update your Operating System](/resources/setup/os-update.html)
1. [Install Needed Software Development Tools (Python 3.11, Visual Studio Code, and git)](/resources/setup/software.html)
2. [Setup a Workspace](/resources/setup/workspace.html)

## 1. Write Your First Program!

Now for the main attraction! Let's write a classic "hello world" program.

In Visual Studio Code, be sure your workspace is open. (Reminder: File > Open Recent > comp110-YYS-workspace is a quick way to reopen it! Where YY is the current year and S is the semeseter: S for Spring, F for Fall, SSX for Summer Session X.)

Open the Explorer pane (click the icon with two sheets of paper or to to _View_ > _Explorer_) and expand the _Workspace_ directory.

Right click on the `exercises` directory, then select create new file and name it `ex00_hello_world.py`.

An empty file opens. The `.py` file extension is standard for Python programs.

For the past 50 or so years it's a tradition in the programming world for your first program to print the words "Hello, world." We won't break it.

Write the line of code below in your file:

~~~ {.python .numberLines startFrom="1"}
print("Hello, world.")
~~~

Next, **save your program** (shortcuts on Windows: `Control+S`, Mac: `Command+S`).

To run your program, first open a terminal: _Terminal_ > _New Terminal_

Then, in the Terminal, type out the following command and press enter: 

`python -m exercises.ex00_hello_world`

If it works, you should see the text "Hello, world." printed in your terminal! If it doesn't work, it's likely a minor issue somewhere. Programming is very precise, go back through and try each instruction again checking for exact punctuation, capitalization, and spelling matches. Even a minor discrepency will cause it to go awry. On a Mac, you _may_ need to run `python3 -m exercises.ex00_hello_world` instead. If that works, from here on use the command `python3` wherever you see us use `python`.

If you are stuck, come see us in office hours by following the instructions posted on the support page. We'll be able to work it out with you! As you know, there were a lot of steps to get to this point, so it's not uncommon for something super minor to be off somewhere. The good news is, once your setup is working you'll be in good shape moving forward for the course.

Congratulations, you've written and run your first Python program! Try running it again by pressing the up arrow on your keyboard, noticing the same command you ran last is filled in, and pressing enter again.

What is the command you wrote doing? The first word `python` is the program responsible for interpretting your code. The second symbol, `-m`, is what we call an "option" that is short for "run as _`m`odule_". You'll learn all about modules soon. Lastly, `exercises.ex00_hello_world` is referring to the file you created! Notice you created the file `ex00_hello_world.py` in the `exercises` directory, or "folder". This is the module you are asking `python` to interpret!

Try changing the text inside of the double quotes (but be sure to keep the words `hello` and `world` somewhere), saving again, and rerunning your program.

What is this line of code doing? You are _calling_ a _function_ named `print`. The `print` function is [built-in to the Python programming language](https://docs.python.org/3/library/functions.html#print) and results in data being "printed" out _somewhere_. By default, that _somewhere_ is on your screen in the Terminal. The parentheses following the word `print` indicate extra information being given to the `print` function. In this example, you are giving a piece of textual information to print which is called a "string" and denoted by the double quotes surrounding the textual data. Don't worry, we will break down all of this into more tangible detail soon!

Your first program is _almost complete_! However, before submitting it there are a couple more style and documentation steps to complete.

First, you should add a special kind of string value, called a _docstring_ short for documentation string, to the top of your program file, which is a Python _module_. Then, you should add a line with a special variable named `__author__` assigned to be your 9-digit student PID. (Disclaimer: Out in the real world the `__author__` variable is typically your name and e-mail address, but since we will grade your programs we'd like to avoid potential bias in seeing your names as part of the programs as we're grading.) Add the following lines above the line of code that calls the `print` function. Fill in _your_ 9-digit UNC PID number, without any spaces or dashes, in the `__author__` string.

~~~ {.python .numberLines startFrom="1"}
"""My first program for COMP110."""

__author__ = "1234567890"


~~~

Save your program again and re-run it. You should still only see your printed output message. What must that mean about the two lines of code you just added? They're for documentation purposes and must not impact the _printed output_ of the program.

## 3. Make a Backup Checkpoint "Commit"

Now that your first program is complete, let's practice making a backup. Visual Studio Code has built-in support for `git` source control management (SCM). SCM tools are made to help create versioned checkpoints of a project's source code (your program is source code!) amont other uses. The current de facto SCM is called `git`. As one more piece of terminology, a checkpointed version in git is called a `commit`. Once your work is in a `commit` checkpoint, you can always return back to your project at that point in time without the risk of losing work. We encourage committing work to backup _at least_ each time you submit a project for grading or are finishing out a working session for the day. Commits are free to make and can only help you avoid losing work; use them liberally!

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Finished Exercise 00!" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Open the _View_ menu and select _Command Palette_, the shortcut for this menu is:
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
7. Begin typing in: `Git: Push to...` and press `Enter` once it is the first option.
8. Select the `backup` remote that is your personal workspace on GitHub. If you do not see `backup` listed, see the instructions below on _Setup Backup Course Material Repository_.
   - You may see a spinning "refresh" icon in your status bar at the bottom of VSCode. Unless an error backing up occurs, you will not see any confirmation.

To see your commit on Github, in a web browser, navigate to `https://github.com/comp110-23f/comp110-workspace-USERNAME` and substitute `USERNAME` with your GitHub username. Open the `comp110` directory, then `exercises`, and `ex0_hello_world.py` you'll see the work you just completed backed up to GitHub. Notice above the file's content's you'll see your commit message.

## 4. Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Before doing so, you need to know that _before_ an assignment's deadline you can resubmit work as many times as you need to _without penalty_. Portions of assignments are autograded and will provide near-immediate feedback. We _want_ you to resubmit as many times as it takes you in order to earn full autograding credit!

Login to Gradescope and select the assignment named "EX00 - Hello, world.". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex00_hello_world.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex00_hello_world.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be no "human graded" component, but in future exercises and projects there will. Thus, you should expect to score 100 out of 100 possible points on this assignment. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!

## 5. Congratulations!

There were _a lot_ of steps and new concepts thrown at you in this initial exercise. Gearing up is half the battle! The amount of setup involved in a modern development environment can be a little overwhelming to a first-time programmer. You are not expected to understand the intricacies of all the processes and software you just followed and setup. That will come with time. For now, focus on the big win that is having written a Python program in a professional code editor, run it, and backed it up using git! Programming gets way more fun, and way more creatively rewarding, as we make our way up the mountain from here.