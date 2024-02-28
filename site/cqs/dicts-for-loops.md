---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Dictionary Challenge Question

For this challenge question, you are going to write a function that iterates over a dictionary!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add file". Your file will be named `unzip.py`.

Set up your document by adding the docstring:
`"""Splitting a dictionary into two lists"""` and initializing the `__author__` variable with your PID.

## Part 1. get_keys()

Write a function definition with the following expectations:

- The function name is `get_keys` and has a `dict[str,int]` parameter.
- The function should return a `list[str]` 
- The function should produce a `list` of all the *keys* in the input dictionary.
- If the input dict is empty, it should return an empty list.
- The function should not mutate (modify) the input dictionary.
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> from lessons.unzip import get_keys
>>> test: dict[str, int] = {"Hello" : 1, "World" : 2}
>>> get_keys(test)
['Hello', 'World']
</div>
</pre>



## Part 2. get_values()

Write a function definition with the following expectations:

- The function name is `get_values` and has a `dict[str,int]` parameter.
- The function should return a `list[int]` 
- The function should produce a `list` of all the *values* in the input dictionary.
- If the input dict is empty, it should return an empty list.
- The function should not mutate (modify) the input dictionary.
- Explicitly type variables, parameters, and return types. 

Example usage:
<pre>
<div class="terminal">>>> from lessons.unzip import get_values
>>> test: dict[str, int] = {"Hello" : 1, "World" : 2}
>>> get_values(test)
[1, 2]
</div>
</pre>


## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/unzip.py```

Then, drag and drop that .zip file into Gradescope!

