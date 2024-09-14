---
title: While Loops Challenge Question 
author:
- Viktorya Hunanyan
- Alyssa Lytle
page: lessons
template: overview
---

# While Loops 

For this challenge question, you're going to practice using a `while` loop to iterate over a string!

Start by creating a file in your CQs folder called `cq03_while_loops.py`. Initialize with a docstring and an `__author__` variable.

## `num_instances`

For this assignment, you're going to write a function called `num_instances`. Given two strings, `phrase` and `search_char` (a single character), `num_instances` should return the count of occurrences of `search_char` in `phrase`.

<!-- "Non-overlapping occurrences" means that once a match of search_str is found within inp_str, the next search for search_str should start after the end of the current match. For example, in the string "HelloHello", the substring "Hello" appears twice, but only the first occurrence is counted once before moving to the next possible starting position.  -->

Here's an example of what it should look like when tested in your REPL:

<pre>
<div class="terminal">
/workspace (main*) > python
>>> from CQs.cq03_while_loops import num_instances
>>> num_instances(phrase="HelloHeLloHEllo", search_char="e")
2
>>> num_instances(phrase="HelloHelloHello", search_char="e")
3
>>> num_instances(phrase="Happy Tuesday!", search_char="y")
2
>>> num_instances(phrase="Happy Tuesday!", search_char="z")
0
</div>
</pre>

Note that `num_instances` is case-sensitive, so `"e"` doesn't equal `"E"`.

### Guide

If you don't know where to start, try following these steps:

- Start by writing the *signature* of the function.
- Create a local variable called `count` with the initial value of 0. This variable can be increased every time you find an instance of `search_char` in `phrase`.
- Next create another local variable that will track your index so you can loop over every element of `phrase`.
- Now, use a while loop to loop over every element of `phrase` and count the number of times `search_char` appears!


## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission CQs/cq03_while_loops.py```

Then, drag and drop that .zip file into Gradescope!