---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Loops Challenge Question

For this challenge question, you are going to write three different functions that perform the same act, but in different ways!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add file". Your file will be named `sum.py`.

Set up your document by adding the docstring:
`"""Summing the elements of a list using different loops"""` and initializing the `__author__` variable with your PID.

## Part 1. w_sum()

Now, write a function called `w_sum` that takes as input a list of floats `vals: list[float]`, and returns the *sum* of all elements. Loop through the list using a `while` loop.

For example, `w_sum([1.1, 0.9, 1.0])` should compute `1.1 + 0.9 + 1.0` and return the simplified value `3.0`.

The sum of an empty list `w_sum([])` should return `0.0`. 

## Part 2. f_sum()

Now, write a function called `f_sum` that performs the same way as `w_sum`, calculating the *sum* of all elements in `vals` but uses a `for ... in ...` loop. (Do NOT use the `range` keyword for this part!)

## Part 3. f_range_sum()
Finally, write a function called `f_range_sum` that performs the same way as the two previous functions, calculating the *sum* of all elements in `vals` but uses a `for ... in range(...)` loop. 

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/sum.py```

Then, drag and drop that .zip file into Gradescope!