---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Loops Challenge Question

For this challenge question, you are going to practice using for loops to iterate over both lists and dictionaries!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "CQs" folder and select "add file". Your file will be named `cq05_for_loops.py`.

Set up your document by adding the docstring:
`"""Practice for-looping over lists and dicts."""` and initializing the `__author__` variable with your PID.

## Part 1. Summing Over Lists

For this part of the challenge question, you are going to write three different functions that perform the same act, but in different ways!

### Part 1.1 w_sum()


Now, write a function called `w_sum` that takes as input a list of floats `vals: list[float]`, and returns the *sum* of all elements. Loop through the list using a `while` loop.

For example, `w_sum([1.1, 0.9, 1.0])` should compute `1.1 + 0.9 + 1.0` and return the simplified value `3.0`.

The sum of an empty list `w_sum([])` should return `0.0`. 

### Part 1.2. f_sum()

Now, write a function called `f_sum` that performs the same way as `w_sum`, calculating the *sum* of all elements in `vals` but uses a `for ... in ...` loop. (Do NOT use the `range` keyword for this part!)

### Part 1.3. f_range_sum()
Finally, write a function called `f_range_sum` that performs the same way as the two previous functions, calculating the *sum* of all elements in `vals` but uses a `for ... in range(...)` loop. 

## Part 2. Looping Over Dictionaries

### Part 2.1. get_keys()

Write a function definition with the following expectations:

- The function name is `get_keys` and has a `dict[str,int]` parameter.
- The function should return a `list[str]` 
- The function should produce a `list` of all the *keys* in the input dictionary.
- If the input dict is empty, it should return an empty list.
- The function should not mutate (modify) the input dictionary.
- Explicitly type variables, parameters, and return types. 
- Do *not* use the built-in .values() or .keys() methods!

Example usage:
<pre>
<div class="terminal">>>> from CQs.cq05_for_loops import get_keys
>>> test: dict[str, int] = {"Hello" : 1, "World" : 2}
>>> get_keys(test)
['Hello', 'World']
</div>
</pre>



### Part 2.2. get_values()

Write a function definition with the following expectations:

- The function name is `get_values` and has a `dict[str,int]` parameter.
- The function should return a `list[int]` 
- The function should produce a `list` of all the *values* in the input dictionary.
- If the input dict is empty, it should return an empty list.
- The function should not mutate (modify) the input dictionary.
- Explicitly type variables, parameters, and return types. 
- Do *not* use the built-in .values() or .keys() methods!

Example usage:
<pre>
<div class="terminal">>>> from CQs.cq05_for_loops import get_values
>>> test: dict[str, int] = {"Hello" : 1, "World" : 2}
>>> get_values(test)
[1, 2]
</div>
</pre>

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission CQs/cq05_for_loops.py```

Then, drag and drop that .zip file into Gradescope!