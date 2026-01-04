---
title: Dictionary Utils
author:
  - Kaki Ryan
  - Vrinda Desai
  - Alyssa Lytle
page: exercises
template: overview
---


# Dictionary Utility Functions

In this exercise you will get some practice with dictionary functions!



## 0. Setup

Create a new **directory** in `exercises` named `ex04`.

Inside the `exercises/ex04` directory, create a file named `dictionary.py`. Add a docstring and establish an `__author__` variable to be assigned a string with the digits of your PID. This is where you will implement the utility functions below.

## 1. `invert`

This is the first function you will write in `dictionary.py`. The other two functions will also be defined in this file.

Given a `dictionary` of `[str, str]`, `invert` should return a `dict[str, str]` that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa.

- Function name: `invert`
- Parameter: `dict[str, str]`
- Return Type: `dict[str, str]`


Remember that **keys in a dictionary are unique.** If you encounter more than one of the same key when trying to invert your dictionary, raise a KeyError. Example usage:

<pre><div class="terminal">>>> invert({'a': 'z', 'b' : 'y', 'c': 'x'})
{'z': 'a', 'y': 'b', 'x': 'c'}
>>> invert({'apple': 'cat'})
{'cat': 'apple'}
>>> invert({'kris': 'jordan', 'michael': 'jordan'})
KeyError
</div>
</pre>

Similar to how you raised a `ValueError` in the `max` function for `list` utils, the syntax for raising a `KeyError` is: `raise KeyError("error message of your choice here!")`

## 2. `favorite colors`



Create a function in your `dictionary.py` file called `favorite_color`. It has the following specifications:

1. It takes as input a `dict[str, str]` of names and favorite colors.
2. It returns a `str` which is the color that appears most frequently.
   1. If there is a tie for most popular color, return the color that appeared in the dictionary first.

- Function name: `favorite_colors`
- Parameter: `dict[str, str]` - dictionary of names and favorite colors
- Return Type: `str` - the most popular color

An example:


<pre>
<div class="terminal">>>> favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
blue
</div></pre>


## 3. `count`

Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list.

- Function name: `count`
- Parameter: `list[str]` - list of values to count the frequencies of
- Return Type: `dict[str, int]` - a dictionary of the counts of each of the items in the input list

Implementation strategy:

1. Establish an empty dictionary to store your built-up result in
2. Loop through each item in the input list
   1. Check to see if that item has already been established as a key in your dictionary. Try the following boolean conditional: `if <item> in <dict>:` -- replacing `<item>` with the variable name of the current value and `<dict>` with the name of your result dictionary.
   2. If the item is found in the dict, that means there is already a key/value pair where the item is a key. Increase the value associated with that key by 1 (counting it!)
   3. If the item is not found in the dict, that means this is the first time you are encountering the value and should assign an initial count of `1` to that key in the result dictionary.
3. Return the resulting dictionary.

## 4. `alphabetizer`

Given a `list[str]`, this function will produce a `dict[str, list[str]]` where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter.

- Function name: `alphabetizer`
- Parameter: `list[str]` - list of words to categorize into different lists
- Return Type: `dict[str, list[str]]` - a dictionary of the letters and the lists of words that belong to that letter

Example usage:

<pre>
<div class="terminal">>>> alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"])
{'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
>>> alphabetizer(["Python", "sugar", "Turtle", "party", "table"])
{'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}
>>> alphabetizer(["Hello", "#COMP110", "hello"])
{'h': ['Hello', 'hello']}
</div>
</pre>

Hint 1: The built-in Python method `.lower()` takes in no arguments and returns the lower cased string of a given string.

Hint 2: The built-in Python method `.isalpha()` can be called on any string and returns `True` if all characters in the string are alphabetic. 

## 5. `update_attendance`

Given a `dict[str, list[str]]`, this function will _mutate_ and return None. It should meet the following specifications:

1. It has three parameters:
   - `dict[str, list[str]]` - an existing dictionary that contains days of the week as keys and a list of students who were in _attendance_ as the values
   - `str` - a day of the week
   - `str` - a student who attended class
2. Update the `dict[str, list[str]]` that was passed in with the new attendance information, then return `None`.

An example:

<pre>
<div class="terminal">>>> attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
>>> update_attendance(attendance_log, "Tuesday" , "Vrinda")
>>> update_attendance(attendance_log, "Wednesday" , "Kaleb")
>>> attendance_log
{'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}
</div>
</pre>

## 6. Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise 3" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.

## 7. Submit to Gradescope for Grading

Login to Gradescope and select the assignment named "EX04 - Dictionary Utility Functions.". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

```
python -m tools.submission exercises/ex04
```

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex04.zip". The "yy", "mm", "dd", and so on, are timestamps with the current month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!

<!-- NOTE: The autograder for this assignment will only test for correct function signatures and basic functionality. You are encouraged to think about edge cases and the robustness of your code on your own. In the next part of this assignment, you will write your own unit tests to ensure that your functions work under a variety of circumstances. -->