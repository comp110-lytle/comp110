---
title: CQ03 - Lists + Functions
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

This will actually mutate the list used as an argument in the function call!

For this challenge question, you are going to practice writing a function that *mutates* its input!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add file". Your file will be named `mutate.py`.

Set up your document by adding the docstring:
`"""Mutating functions."""` and initializing the `__author__` variable with your PID.

## Part 1. manual_append()

Write a function definition with the following expectations:

- The function name is `manual_append` has a `list[int]` and an `int` as parameters.
- The function should return *nothing*.
- The function should *mutate* its input *appending* the `int` parameter to the end of the `list[int]` parameter.
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> a: list[int] = [1,2,3]
>>> from lessons.mutate import manual_append
>>> manual_append(a, 2)
>>> print(a)
[1,2,3,2]
</div>
</pre>




## Part 2. double()

Write a function definition with the following expectations:

- The function name is `double` and has a `list[int]` as a parameter.
- The function should return *nothing*.
- The function should *mutate* its input by multiplying every element in the `list[int]` parameter by 2
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> a: list[int] = [1,2,3]
>>> from lessons.mutate import double
>>> double(a)
>>> print(a)
[2,4,6]
</div>
</pre>


Hint: You will need to use a `while` loop to iterate over every element in the list. 

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/mutate.py```

Then, drag and drop that .zip file into Gradescope!

