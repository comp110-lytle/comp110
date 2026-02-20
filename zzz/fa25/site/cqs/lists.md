---
title: CQ02 - Lists Practice
author:
  - Alyssa Lytle
page: lessons
template: overview
---

# Introduction

In our previous lesson, we discussed the many capabilities of functions with lists. 

They can:

- Take lists as arguments
- Return (or create and return) lists 
- Modify (or mutate) lists

This last capability, *mutating* lists, is actually quite surprising! We aren't able to do this with our previous data types, like strings. 

For example, observe the following function:

```
    def emphasize(word: str):
        word += "!"
```

When we call this function on a string, we aren't actually *mutating* the argument. 

However, let's do something similar for a list!

```
    def emphasize(word: list[str]):
        word.append("!")
```

This will actually *mutate* the list used as an argument in the function call!

<!-- To get more comfortable with this idea, you can watch [this video](https://www.youtube.com/watch?v=DuSEcQMsZRE) to see how this works in memory! -->

For this challenge question, you are going to practice writing a function that *mutates* its input!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "CQs" folder and select "add file". Your file will be named `cq02_lists.py`.

Set up your document by adding the docstring:
`"""Mutating functions."""` and initializing the `__author__` variable with your PID.

## Part 1. manual_append()

Write a function definition with the following expectations:

- The function name is `manual_append`. It has a `list[int]` and an `int` as parameters.
- The function should return *nothing*.
- The function should *mutate* its input by *appending* the `int` parameter to the end of the `list[int]` parameter.
- Make sure to explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> a: list[int] = [1,2,3]
>>> from CQS.cq02_lists import manual_append
>>> manual_append(a, 2)
>>> print(a)
[1,2,3,2]
</div>
</pre>




## Part 2. double()

Write a function definition with the following expectations:

- The function name is `double` and has a `list[int]` as a parameter.
- The function should return *nothing*.
- The function should *mutate* its input by looping through the list and multiplying every element in the `list[int]` parameter by 2
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> a: list[int] = [1,2,3]
>>> from CQs.cq02_lists import double
>>> double(a)
>>> print(a)
[2,4,6]
</div>
</pre>


Hint: You will need to use a `while` loop to iterate over every element in the list. 

## Part 3. Calling double()
Let's see an example of how lists work in memory.

1. Create a global variable called  `list_1` that is a `list[int]` and has a value of `[1, 2, 3]`.

2. Create another global variable called `list_2` that is also a `list[int]` and set it equal to `list_1`. 

3. Call the `double` function with `list_2` as the argument.

4. Add two print statements for `list_1` and `list_2`. 

__Before you continue: What will be printed for `list_1`? What will be printed for `list_2`?__

5. Test out your theory by running your code either in Trailhead or the REPL.

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission CQs/cq02_lists.py```

Then, drag and drop that .zip file into Gradescope!

