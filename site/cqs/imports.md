---
title: Challenge Question 
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Importing + Scope Challenge Question

For this assignment, we're going to practice *importing* functions from different files!

## Part 0. Setup

### Create Folder

In your **CQs** folder, you're going to want to create *another folder*! Right click on **CQs** and select "New Folder...". Name this folder `cq04`.

### Create Files

Inside your **cq04** folder, create the following three files (right click and select "New File..." for each one):

- `coordinates.py`
- `concatenation.py`
- `visualize.py`

## Part 1. `concatenation.py`

### Part 1.1 `concat` Function

In `concatenation.py`, write a function that matches the following description:

- Name: `concat`
- Parameters: two `str`s
- Return type: `str`
- Behavior: It should return the *concatenation* of the two input strings.

#### Example behavior in REPL

<pre>
<div class="terminal">
/workspace (main*) > python
>>> from CQs.cq04.concatenation import concat
>>> concat("hello","world")
'helloworld'
>>> concat("123","4567")
'1234567'
</div>
</pre>

### Part 1.2 Calling the `concat` Function

Now, still working in the file `concatenation.py`, print the result of calling `concat` with the arguments `"happy"` and `"tuesday"`.


## Part 2. `visualize.py`

### Part 2.1 Import the function

In `visualize.py` *import* the function `concat` from `concatentation.py`. *Do not call the function yet!* 

<!-- ## Part 2. `get_coords` Function

In `coordinates.py`,  write a function that matches the following description: -->