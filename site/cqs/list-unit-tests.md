---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Unit Test Challenge Question

This challenge question serves two functions: to get more practice writing a function that modifies a list and to practice writing unit tests!

## Part 0. Setup.

Write click on your "lessons" folder and select "New Folder". Your new folder will be titled "CQ05". Then right click on "CQ05" and select "New File". Your new file will be called `find_max.py`. Then, click on "CQ05" and select "New File" again. This file will be called `max_test.py`. Go ahead and initialize both files with your `__author__` variable.

## Part 1. `find_and_remove_max`

In this file, you will write one function definition called `find_and_remove_max`. The function will have the following behavior:

- It will take a `list[int]` as input and return an `int`.
- It will *find* and *return* the largest number in the input list.
- It will also *remove* all instances of the largest number from the input list.
- If the input list is empty, return -1 and don't modify the input list.

Here is some example behavior: 

<pre>
<div class="terminal">python
>>> from lessons.CQ05.find_max import find_and_remove_max
>>> a: list[int] = []
>>> find_and_remove_max(a)
-1
>>> a
[]
>>> b: list[int] = [10,9,8,7,10]
>>> find_and_remove_max(b)
10
>>> b
[9, 8, 7]
</div>
</pre>

*(Hint 0: I recommend using a `while` loop for the part in the function where you are removing the max value.)*



## Part 2. Unit Tests

Now, in `max_test.py`, you are going to write unit tests that test `find_and_remove_max`!

You should write: 

- One *use case* that ensures `find_and_remove_max` *returns* the expected value.
- One *use case* that ensures `find_and_remove_max` *mutates* the input in the expected way.
- One *edge* case that ensures `find_and_remove_max` *returns* the correct value in case of an unconventional input.

(Do *not* copy the use case from the REPL example in Part 1!)

## Part 3. Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons.CQ05```

(For this assignment, you'll have to submit your entire CQ05 folder!)

Then, drag and drop that .zip file into Gradescope!