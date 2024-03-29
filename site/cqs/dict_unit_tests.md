---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Unit Test Challenge Question

For this challenge question, you are going to *test* the functions we just wrote in class!

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "garden" folder in "lessons" and select "add file". Your file will be named `garden_helpers_test.py`.

Set up your document by adding the docstring:
`"""Test my garden functions."""` and initializing the `__author__` variable with your PID.

Also don't forget to import your functions from `lessons.garden.garden_helpers`!

## Part 1-3. unit tests

Write 2 unit tests for each of the 3 functions defined in class. Remember that a unit test function name starts with `test_`.

The 2 unit tests should consist of:

* One edge case
* One use case

Include descriptive function names and docstrings, so that it captures what is being tested.

*Also, be sure to not just copy the examples used in class for your cases! We will be checking for that!*

### Try your unit tests!

You can try your unit tests to see if they work by running:

`python -m pytest lessons/garden/garden_helpers_test.py`

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/garden```


Then, drag and drop that .zip file into Gradescope!