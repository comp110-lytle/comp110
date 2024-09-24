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

### Part 0.0 Create Folder

In your **CQs** folder, you're going to want to create *another folder*! Right click on **CQs** and select "New Folder...". Name this folder `cq04`.

### Part 0.1 Create Files

Inside your **cq04** folder, create the following three files (right click and select "New File..." for each one):

- `coordinates.py`
- `concatenation.py`
- `visualize.py`

Initialize each file with a Docstring and the `__author__` variable.

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

Now, still working in the file `concatenation.py`, create the global variables `word1` with the value `"happy"` and `word2` with the value `"tuesday"` print the result of calling `concat` with the arguments `word1` and `word2`.


## Part 2. `visualize.py`

### Part 2.0 Import the function

In `visualize.py` *import* the function `concat` from `concatentation.py`. *Do not call the function yet!* 

Try running your file either in the trailhead or the terminal.

*Reminder:* To run your file in the terminal, use `python -m CQs.cq04.visualize`

What happens? You should see an output! That's because it is running the entire module including the function call from `concatenation.py` when you import the function!

### 2.1 Suppress the function call

Add *something* to `concatenation.py` so that the function call still occurs when you run the `concatentation.py` file, but not when you import it.  *(Hint: We covered this in our previous lesson! It's something you've commonly used in assignments leading up to this one!*)

### 2.2 Global Variables 

Now let's actually *call* the `concat` function in `visualize.py`!

Let's first create some global variables! Create variable `x` with value `"123"` and `y` with value `"abc"`. Call `concat` using `x` and `y` as your arguments and `print` the result!


## Part 3. `coordinates.py` 

### Part 3.0 `get_coords` Function

In `coordinates.py`,  write a function that matches the following description: 

- Name: `get_coords`
- Parameters: `xs: str` and `ys: str`
- Return type: `None`
- Behavior: It should *print* the formatted pairs of each character in the two input strings. (See example.)

<pre>
<div class="terminal">
>>> from CQs.cq04.coordinates import get_coords
>>> get_coords("12","34")
(1,3)
(1,4)
(2,3)
(2,4)
>>> get_coords("hi","bye")
(h,b)
(h,y)
(h,e)
(i,b)
(i,y)
(i,e)
</div>
</pre>

For this, you're going want to use a while loop *inside* another while loop, or a **nested while loop**. Your outer loop will iterate over every character in `xs` and your inner loop will iterate over every character in `ys` and contain the `print` statement.

### Part 3.1 Importing and calling the `get_coords` function

Now, go back to `visualize.py` and *import* the function `get_coords` from `coordinates.py`. 

Call `get_coords` using your existing `x` and `y` global variables!


##  Part 4. Submission

For this assignment, you're actually going to compress the entire `cq04` file to submit! You can do this by using the following command: 

```python -m tools.submission CQs/cq04```

As usual, drop the generated .zip file into Gradescope!