---
title: CQ08 - Lists + Functions
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
    def add_to_end(word: str):
        word += "!"
```

When we call this function on a string, we aren't actually *mutating* the argument. 

However, let's do something similar for a list!

```
    def add_to_end(word: list):
        word.append("!")
```

This will actually mutate the list used as an argument in the function call!

For this challenge question, you are going to practice writing a function that *mutates* its input!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add file". Your file will be named `mutate.py`.

Set up your document by adding the docstring:
`"""Mutating functions."""` and initializing the `__author__` variable with your PID.

## Part 1. double()

Write a function definition with the following expectations:

- The function name is `double` and is called with a `list[int]` as an argument.
- The function should return *nothing*.
- The function should *mutate* its input by multiplying every element in the `list[int]` parameter by 2
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> a: list[int] = [1,2,3]
>>> double(a)
>>> print(a)
[2,4,6]
</div>
</pre>


## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/mutate.py```

Then, drag and drop that .zip file into Gradescope!

