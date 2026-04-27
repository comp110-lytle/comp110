---
title: EX03 - list Utility Functions
author:
  - Kris Jordan
  - Marlee Walls
  - Alyssa Lytle
  - Viktorya Hunanyan
page: exercises
template: overview
---

# Introduction

Art students intentionally reproduce great works of art to develop their own skills and techniques. The purpose isn't to become an imitator, but to deepen an understanding of important work and styles that came before you.

Reverse engineering algorithms and abstractions in computer science is of the same spirit! In this exercise you will implement algorithms to practice computational thinking. You will gain familiarity with the names and behaviors of commonly useful functions.

Since the work you do is reproducing tried and true abstractions of the past, in the future you can and should use your language's preferred functions and idioms instead. In this exercise we will show you how to achieve the same functionality using idiomatic Python in the future.

## Allowed Constructs

Your function implementations may only make use of the built-in `len` function, and a `list` object's methods `append` and `pop`.

Specifically off-limits in this exercise are the following constructs. You are not expected to know what any of these are, so this only applies to people with outside Python experience. Making use of any of the following will result in no credit for the function you use them in:

- Cannot use other built-in function besides `len` - specifically not `max`, `min`, `slice`
- Cannot use slice notation in conjunction with the subscription operator
- Cannot use the `in` operator of Python (but you can use `for..in` loops!)
- Cannot use the `list` class's `+` or `==` operators nor built-in methods beyond `append` and `pop`
  - Note: You can use + and == for individual elements, just not entire `list`s.

Assignment Outline

- `all` -- 20 Points Autograded
- `max` -- 20 Points Autograded
- `is_equal` -- 20 Points Autograded
- `extend` -- 20 Points Autograded
- Style, Linting, Typing -- 20 Points Autograded

General Notes:

- You are not required to implement a `main` function for this exercise. However, it may be helpful to have one to make test function calls with lists you construct.
- The grader will evaluate your code by **importing your functions** and calling them with our own chosen list inputs. You do not need to create your own lists and call the functions. (However, feel free to for practice!)

## 0. Setup

In Visual Studio Code, be sure your workspace is open.

Open the Explorer pane (the icon with two sheets of paper or menu View > Explorer) and expand the Workspace directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match punctuation:

`ex03_list_utils.py`

Before beginning work on the program, you should add a docstring to the top of your Python module just as you have previously. Then, you should add a line with the special variable named **author** assigned to be a string with your 9-digit student PID.

## 1. `all` -- 20 Points

This is the first function you will write in `ex03_utils.py`. The other two functions will also be defined in this file.

Given a `list` of `ints` and an `int`, `all` should return a bool indicating whether or not all the ints in the list are the same as the given `int`. Example usage:

<pre>
<div class="terminal">
>>> from exercises.ex03_utils import all
>>> all([1, 2, 3], 1)
False
>>> all([1, 1, 1], 2)
False
>>> all([1, 1, 1], 1)
True
</div>
</pre>

Continue by defining a skeleton function with the following signature:

1. Name: `all`
2. Arguments: A list of integers and an int.
3. Returns: A `bool`, `True` if all numbers match the indicated number, `False` otherwise or if the list is empty. This algorithm should work for a list of any length. Hint: remember you can return from inside of a loop to short-circuit its behavior and return immediately.

## 2. `max` -- 20 Points

Next, you will write a function named `max`.

The `max` function is given a `list` of `ints`, `max` should return the largest in the List.

If the `list` is empty, `max` should result in a `ValueError`. We'll show you how! Examples:

<pre>
<div class="terminal">
>>> from exercises.ex03_utils import max
>>> max([1, 3, 2])
3
>>> max([100, 99, 98])
100
>>> max([])
ValueError: max() arg is an empty List
</div>
</pre>

Define a skeleton function with the following signature:

1. Name: `max`
2. Argument: A list of integers.
3. Returns: An `int`, the largest number in the list. If the list is empty, raises a ValueError.

The body of your skeleton function can begin as such, which demonstrates how to `raise` an error:

```{.python}
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
```

## 3. `is_equal` -- 20 Points

Given two `list`s of `int` values, return `True` if _every_ element at _every_ index is equal in both `list`s.

<pre>
<div class="terminal">
>>> from exercises.ex03_utils import is_equal
>>> is_equal([1, 0, 1], [1, 0, 1])
True
>>> is_equal([1, 1, 0], [1, 0, 1])
False
</div>
</pre>

Your implementation should not assume the lengths of each List are equal.

This concept is called _deep equality_. Two separate `list` objects on the _heap_ may be distinct objects, such that if you changed one the other would remain the same. However, two distinct objects can be _deeply equal_ to one another if what they are made of is equal to each other in essence.

Define a function with the following signature:

1. Name: `is_equal`
2. Parameters: Two lists of integers.
3. Returns: `True` if lists are equal, `False` otherwise.

Implement the `is_equal` function as described above.

## 4. `extend` -- 20 Points

Given two `list`s of `int` values, *mutate* the first `list` of `int` values by appending the second `list`'s values to the end of it. (Think of this is something similar to concatentation in `string`s!) **Do *NOT* use the built-in `extend` method for lists!**


Note that this function is not *returning* anything! It is only *mutating* one of the inputs.

<pre>
<div class="terminal">
>>> from exercises.ex03_utils import extend
>>> a: list[int] = [1, 3, 5]
>>> b: list[int] = [2, 4, 6]
>>> extend(a, b)
>>> a
[1, 3, 5, 2, 4, 6]
>>> c: list[int] = [7, 8]
>>> extend(c, b)
>>> c
[7, 8, 2, 4, 6]
</div>
</pre>


Define a function with the following signature:

1. Name: `extend`
2. Parameters: Two lists of integers.
3. Returns: Nothing.

Implement the `extend` function as described above.

## 5. Style and Documentation Requirements 

We will manually grade your code and are looking for good choices of meaningful variable names. Your variable names should be descriptive of their purposes. (Loop indexing variables can be short, such as `i`, or `idx`.) You should also use the Python `snake_case` convention where variable names are all lowercase and new words are separated by underscores. We will also be checking that you are not using anything outside of what we have learned up to the release date of this assignment. 

You should add code comments in your own English words to describe what is happening at important stages of your program.

As part of the manual grading, we will be looking to see if you have commented on your code! No comments imply that there were no challenges or moments spent considering how to approach a code. It is quite rare to complete every exercise, challenge question, and practice problem without engaging in some form of problem-solving. Even the most experienced programmers use a piece of paper to map out their approach when working on practice problems, often leading to comments being added to code. 

As a general rule, if 2 or more minutes are spent thinking about how to write a particular line or block of code, it’s a good idea to add a comment. Explain what’s happening on that line, how the solution was reached, the reasoning behind the approach, or provide a note for future reference to recall the problem-solving steps. If you received help from office hours or tutoring, go back to the code you were stuck on and explain it to yourself. If you see that you need a second to understand what is going on, comment! Essentially, we will be looking to see if you are able to explain your code logically and with reason. 

Comments don't need to be extensive, but they should reflect a genuine effort to explain the process in your own words. Commenting should be an integral part of the problem-solving process.

## 6. Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.

## 7. Submit to Gradescope for Grading

Login to Gradescope and select the assignment named "ex03 - Lists Utils". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex03_list_utils.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex03-utils.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!
