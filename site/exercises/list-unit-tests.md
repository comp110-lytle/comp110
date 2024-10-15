---
title: EX05 - `list` Utility Functions
author:
- Marlee Walls
- Kris Jordan
- Kaki Ryan
- Alyssa Byrnes
- Sophie Jiang
- Izzi Hinks
- Viktorya Hunanyan
page: exercises
template: overview
---

# List Unit Tests

In this exercise you will continue building list utility functions. In contrast with the previous exercise, for EX05 you will get practice writing unit tests for your functions which gives you more reassurance of their correctness and makes testing your functions easier. 

## Forbidden Constructs

Your function implementations may only make use of subscription notation, the built-in `len` function, and a `list` object's methods `append` and `pop`.

Specifically off-limits in this exercise are the following capabilities which you would only know if you have prior experience in Python. Making use of any of the following will result in no credit for the function you use them in:

* Cannot use other built-in function besides `len` - specifically not `max`, `min`, `slice`
* Cannot use slice notation in conjunction with the subscription operator
* Cannot use the `in` operator of Python with lists (but you can use `for..in` loops!)
* Cannot use the `list` class's `+` or `==` operators (you can still use `+` with `int` and `str` types, though!) nor built-in methods beyond `append` and `pop`
    * Note: You can use + and == for _individual items_ and values, just not entire `list` objects.

Note: Even if your functions are not 100% correct or finished, you can get full credit for the unit tests if you set up a function skeleton and write your tests assuming correct functionality.

## 0. Skeleton Code and Testing Setup

Create a new **directory** in `exercises` named `ex05`. (Right click on `exercises` and select `new folder`.)

Inside the `exercises/ex05` directory, create two files: `utils.py` and `utils_test.py`. The first file will be where you implement some more list utility functions, and the second will be where you define unit tests for them! Add a docstring and establish an `__author__` variable to be assigned a string with the digits of your PID. 


## 1. `only_evens` 

This is the first function you will write in `utils.py`. The other two functions will also be defined in this file.

Given a `list` of `ints`, `only_evens` should return a new `list` containing only the elements of the input list that were even. *The `only_evens` function must not mutate (modify) its input list.* 

Example usage:
<pre>
<div class="terminal">>>>from exercises.ex05.utils import only_evens
>>> only_evens([1, 2, 3])
[2]
>>> only_evens([1, 5, 3])
[]
>>> only_evens([4, 4, 4])
[4, 4, 4]
</div>
</pre>

Continue by defining a skeleton function with the following signature:

1. Name: `only_evens`
2. Arguments: A list of integers. 
3. Returns: A list of integers, containing only the even elements of the input parameter.


<!--  This is a repeat of extend
## 2. `concat` -- 25 Points

In this exercise you will write a function named `concat`. Given two `Lists` of `ints`, `concat` should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list. Your `concat` function may not mutate ("modify") either of its list parameters.

Define your function with the following signature.

1. Name: `concat`
2. Parameters: Two lists of ints. 
3. Returns: A `list` containing all elements of the first list, followed by all elements of the second list. 
    
`concat` _must NOT_ mutate (modify) either of the arguments passed to it.  
 -->

## 2. `sub`

In this exercise you will write a function named `sub`. Given a `list` of `ints`, a start index, and an end index (not inclusive), `sub` should generate a list which is a subset of the input list, between the specified start index and the end index - 1. *The `sub` function must not mutate (modify) its input list.* 


Example usage:
<pre>
<div class="terminal">>>>from exercises.ex05.utils import sub
>>> a_list = [10, 20, 30, 40]
>>> sub(a_list, 1, 3)
[20, 30]
>>> sub(a_list, -1, 6)
[10, 20, 30, 40]
>>> list2 = []
>>> sub(list2, 1, 3)
[]
</div>
</pre>

Next, define a skeleton function with the following signature in `ex05/utils.py`:

1. Name: `sub`
2. Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index (not inclusive). 
3. Returns: A list which is a subset of the given list, between the specified start index and the end index - 1.
    
If the start index is negative, start from the beginning of the list. If the end index is greater than the length of the list, end with the end of the list.

If the length of the list is 0, start is greater than or equal to the length of the list, or end is at most 0, return the empty list.


## 3. `add_at_index`
Given a list of ints, an int element, and an index, `add_at_index` should modify the input list to place the element at the given index. `add_at_index` should return nothing. *The `add_at_index` function **should** mutate its input list.* 


If the index is out of range (index < 0 or index > len(list)), `add_at_index` should throw an IndexError.

Example usage:
<pre>
<div class="terminal">>>> from exercises.ex05.utils import add_at_index
>>> list_1 = [1, 2, 3, 5]
>>> add_at_index(list_1, 4, 3)
>>> list_1
[1, 2, 3, 4, 5]
>>> list_2 = [1]
>>> add_at_index(list_2, 2, 1)
>>> list_2
[1, 2]
>>> list_3 = []
>>> add_at_index(list_3, 1, 1)
IndexError: Index is out of bounds for the input list
</div>
</pre>

Next, define a skeleton function with the following signature in `ex05/utils.py`:

1. Name: `add_at_index`
2. Parameters: A list and two ints, where the first int is the element to be added and the second int is the index at which it should be added. 
3. Returns: None

If the index given is invalid (out of range), raise the following error: 
```{.python}
raise IndexError("Index is out of bounds for the input list")
```

*Hint:* For most cases, you will need to add space at the end of the list (i.e. append something to the end of the list), then shift everything to the right of the index in order to make space for the input element, before you can insert the new element at the correct index.

## 4. Unit Tests

Now inside `utils_test.py`, you will write unit tests.

For each function from (`only_evens`, `sub`, `add_at_index`), you are to define at least **3x unit test** functions. Remember that a unit test function starts with `test_`.

The 3 unit tests should consist of:

* At least one edge case
* At least two use cases: one that tests what the function should return and one that tests how it should mutate (or not mutate) its input.

Include descriptive function names and docstrings, so that it captures what is being tested. **Use different use cases than the usage examples provided in this writeup!**

The command to run your tests is `python -m pytest exercises/ex05` or you can run them using the beaker tab in VSCode if it is working (do note the VSCode testing feature tends to be a bit flaky). 

Once you're ready to import and begin testing your skeletons, you can add the following import lines to your test file, corresponding to the functions you have completed, to do so:

<pre>
<div class="terminal">from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
</div>
</pre>


Once you have completed all functions, you can reduce the three import lines down into a single one for less redundancy in your testing code:

<pre>
<div class="terminal">from exercises.ex05.utils import only_evens, sub, add_at_index
</div>
</pre>

If your screen is large enough, you are encouraged to open these files side-by-side in VSCode by dragging the tab of one to the right side of VSCode so that it changes to a split pane view. Closing your file explorer can help give you additional horizontal space.

For the `add_at_index` function, when testing that the function raises an `IndexError`, a different approach is used. An `IndexError` is an *exception*, and in order to catch an exception, the `pytest.raises` context manager is employed.

Here is a skeleton code of how to *raise* or catch this exception:

```python
import pytest

def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(<list_object>, <index_to_insert_num>, <value_to_add>) 
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num> 
        # that is greater than the length of our <list_object>
```

What this is saying:
- The code inside the `with pytest.raises(IndexError):` block expects an `IndexError` to be raised. If the exception occurs as expected, the test passes. 
- If the exception is not raised, or if a different exception is raised, the test will fail, indicating that the function is not handling the invalid input correctly.

We use `pytest.raises` instead of testing for equality using `==` because exceptions are not returned values; they are events that interrupt the normal flow of execution. When testing for errors, it is not possible to check for an error by comparing a return value. Instead, `pytest.raises` allows testing that the correct exception is triggered during the execution of a function.

Notice that in order to use `pytest`, it must be imported. As shown in the example structure above, add the import line for pytest along with the other import lines at the top of the test file.

## 5. Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.


## 6. Submit to Gradescope for Grading

Login to Gradescope and select the assignment named "EX05 - List Utils and Unit Tests". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex05`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex05.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!
