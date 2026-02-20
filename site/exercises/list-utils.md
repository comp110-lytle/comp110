---
title: EX04 - `list` Utility Functions
author:
  - Kris Jordan
  - Marlee Walls
page: exercises
template: overview
---

# List Utility Functions

## Introduction

Art students intentionally reproduce great works of art to develop their own skills and techniques. The purpose isn't to become an imitator, but to deepen an understanding of important work and styles that came before you.

Reverse engineering algorithms and abstractions in computer science is of the same spirit! In this exercise you will implement algorithms to practice computational thinking. You will gain familiarity with the names and behaviors of commonly useful functions.

Since the work you do is reproducing tried and true abstractions of the past, in the future you can and should use your language's preferred functions and idioms instead. In this exercise we will show you how to achieve the same functionality using idiomatic Python in the future.

### Allowed Constructs

Your function implementations may only make use of the built-in `len` function, and a `list` object's methods `append` and `pop`.

Specifically off-limits in this exercise are the following constructs. You are not expected to know what any of these are, so this only applies to people with outside Python experience. Making use of any of the following will result in no credit for the function you use them in:

- Cannot use other built-in function besides `len` - specifically not `max`, `min`, `slice`, `range`
- Cannot use slice notation in conjunction with the subscription operator
- Cannot use `for` loops
- Cannot use the `in` operator of Python
- Cannot use the `list` class's `+` or `==` operators nor built-in methods beyond `append` and `pop`
  - Note: You can use + and == for individual elements, just not entire `list`s.

<!-- Note from Alyssa - I commented this out to give us more leniency in constructing the autograder, but feel free to put back in!

### Assignment Outline



- `all` -- 30 Points Autograded
- `max` -- 30 Points Autograded
- `is_equal` -- 20 Points Autograded
- Typing Checking -- 20 Points Autograded
- Checks for off-limits usage -- Penalties applied through manual checks after the deadline -->

### General Notes:

- You are not required to implement a `main` function for this exercise. However, it may be helpful to have one to make test function calls with lists you construct.
- The grader will evaluate your code by **importing your functions** and calling them with our own chosen list inputs. You do not need to create your own lists and call the functions. (However, feel free to for practice!)

## 0. Establish the Python Module

In Visual Studio Code, be sure your workspace is open.

Open the Explorer pane (the icon with two sheets of paper or menu View > Explorer) and expand the Workspace directory.

Right click on the `exercises` directory and select "New File". Enter the following filename, being careful to match punctuation:

`ex04_list_utils.py`

Before beginning work on the program, you should add a docstring to the top of your Python module just as you have previously. Then, you should add a line with the special variable named **author** assigned to be a string with your 9-digit student PID.

## 1. `all` 

This is the first function you will write in `ex04_list_utils.py`. The other two functions will also be defined in this file.

Given a `list` of `ints` and an `int`, `all` should return a bool indicating whether or not all the ints in the list are the same as the given `int`. Example usage:

<pre>
<div class="terminal">
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

## 2. `max` 

Next, you will write a function named `max`.

The `max` function is given a `list` of `ints`, `max` should return the largest in the List.

If the `list` is empty, `max` should result in a `ValueError`. We'll show you how! Examples:

<pre>
<div class="terminal">
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

## 3. `is_equal`

Given two `list`s of `int` values, return `True` if _every_ element at _every_ index is equal in both `list`s. This is an implementation of how the `==` operator works with two lists under the hood and in your implementation you are not allowed to use `==` to compare equality of lists directly. Your goal is to test for equality of each item in the list, one-by-one.

<pre>
<div class="terminal">
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

## 4. `extend` 

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

## 5. Submit to Gradescope for Grading

Login to Gradescope and select the assignment named "EX04 - List Utils". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex04_list_utils.py`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex04-utils.py.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. If yours times out, that means there is an infinite list. Try using the debugger to check each of your functions for infinite loops. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!
