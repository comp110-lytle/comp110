---
title: EX00 - Hello, world.
author:
- Kris Jordan
- Kaki Ryan
- Aneka Happer
page: exercises
template: overview
site-branch: public
---

Welcome to COMP110 - Introduction to Programming at UNC Chapel Hill!

## 0. Complete the Prerequisites

Before continuing on, make sure you have set up your account on Repl!

## 1. Write Your First Program!

Now for the main attraction! Let's write a classic "hello world" program.

In your repl project, navigate to the menu on the left and select the "files" tab. Create a new folder called `exercises.`

Click the three dots on the right of `exercises` folder and select "Add File". Name your file:

* `ex00_hello_world.py`

An empty file opens. The `.py` file extension is standard for Python programs.

For the past 50 or so years it's a tradition in the programming world for your first program to print the words "Hello, world." We won't break it.

Write the line of code below in your file:

~~~ {.python .numberLines startFrom="1"}
print("Hello, world.")
~~~

Replit should automatically will save your work as long as you are connected to the internet. 

To run your program, navigate to the right of the page and click on the `shell` tab.

Then, after the prompt "~/Comp110-Workspace$ ", type out the following command and press enter: 

`python -m exercises.ex00_hello_world`

If it works, you should see the text "Hello, world." printed in the shell! If it doesn't work, it's likely a minor issue somewhere. Programming is very precise, go back through and try each instruction again checking for exact punctuation, capitalization, and spelling matches. Even a minor discrepency will cause it to go awry.

Congratulations, you've written and run your first Python program! Try running it again by pressing the up arrow on your keyboard, noticing the same command you ran last is filled in, and pressing enter again.

What is the command you wrote doing? The first word `python` is the program responsible for interpretting your code. The second symbol, `-m`, is what we call an "option" that is short for "run as _`m`odule_". You'll learn all about modules soon. Lastly, `exercises.ex00_hello_world` is referring to the file you created! Notice you created the file `ex00_hello_world.py` in the `exercises` directory, or "folder". This is the module you are asking `python` to interpret!

Try changing the text inside of the double quotes (but be sure to keep the words `hello` and `world` somewhere), saving again, and rerunning your program.

What is this line of code doing? You are _calling_ a _function_ named `print`. The `print` function is [built-in to the Python programming language](https://docs.python.org/3/library/functions.html#print) and results in data being "printed" out _somewhere_. By default, that _somewhere_ is on your screen in the Terminal. The parentheses following the word `print` indicate extra information being given to the `print` function. In this example, you are giving a piece of textual information to print which is called a "string" and denoted by the double quotes surrounding the textual data. Don't worry, we will break down all of this into more tangible detail soon!

## 2. Congratulations!

There were _a lot_ of steps and new concepts thrown at you in this initial exercise. Gearing up is half the battle! The amount of setup involved in a modern development environment can be a little overwhelming to a first-time programmer. You are not expected to understand the intricacies of all the processes and software you just followed and setup. That will come with time. For now, focus on the big win that is having written a Python program in a professional code editor, run it, and backed it up using git! Programming gets way more fun, and way more creatively rewarding, as we make our way up the mountain from here.