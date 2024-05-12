---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Dictionary Challenge Question

For this challenge question, you are going to write a function that creates a dictionary!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add file". Your file will be named `zip.py`.

Set up your document by adding the docstring:
`"""Combining two lists into a dictionary"""` and initializing the `__author__` variable with your PID.

## Part 1. zip()

Write a function definition with the following expectations:

- The function name is `zip` and is called with a `list[str]` and `list[int]` as arguments.
- The function should return a `dict[str,int]`.
- The function should produce a dictionary where the *keys* are the items of the first list and the *values* are the corresponding items at the same index of the second list.
- If the input lists are different lengths or if they are empty, the function should return an empty dictionary.
- The function should not mutate (modify) the input lists.
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> zip(["Happy", "Tuesday"],[1,2])
{"Happy": 1, "Tuesday":2}
</div>
</pre>


## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/zip.py```

Then, drag and drop that .zip file into Gradescope!

