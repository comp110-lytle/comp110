---
title: EX07 - `dict` Unit Tests
author:
- Vrinda Desai
page: exercises
template: overview
---

In this exercise, you will return to the dictionary functions you built in the previous exercise. You will practice writing *unit tests* for each of these functions, checking if your solutions work under a variety of circumstances. The unit tests will make testing your functions easier and will reassure you of their correctness.

As a reminder, the autograder from EX06 only tested function signatures and very basic functionality. Thus, you may realize some of your functions do not actually work as you expected! Good test cases will be important, especially as the autograder for EX07 is much more stringent.

Note: Even if your functions are not 100% correct or finished, you can still get full credit for the *unit tests* if you set up a function skeleton and write your tests assuming correct functionality.

Assignment Outline

* `invert`
    * Unit Tests -- 18 Points Autograded
* `count`
    * Unit Tests -- 18 Points Autograded
* `favorite_color` 
    * Unit Tests -- 18 Points Autograded
* `alphabetizer`
    * Unit Tests -- 18 Points Autograded
* `update_attendance`
    * Unit Tests -- 18 Points Autograded
* Style, Linting, Typing -- 10 Points Autograded




## 0. Testing Setup

Inside the `exercises/ex06` directory which you created in the previous exercise, create a file named `dictionary_test.py`. Add a docstring and establish an `__author__` variable to be assigned a string with the digits of your PID. This is where you will write unit tests for the 5 functions defined in the `dictionary.py` file.

## 1. Writing Unit Tests

For each function (`invert`, `favorite_color`, `count`, `alphabetize`, `update_attendance`), you are to define at least **3x unit test** functions. Remember that a unit test function starts with `test_`.

The 3 unit tests should consist of:

- Two use cases: expected use cases of a function
- One edge case: unexpected use cases of a function

Include descriptive function names and docstrings, so that it captures what is being tested.

The command to run your tests is `python -m pytest exercises/ex06/dictionary_test.py` or you can run them using the beaker tab in VSCode if it is working (do note the VSCode testing feature tends to be a bit flaky).

If your screen is large enough, you are encouraged to open these files side-by-side in VSCode by dragging the tab of one to the right side of VSCode so that it changes to a split pane view. Closing your file explorer can help give you additional horizontal space.

#### _Testing for KeyError:_

You may optionally add a test for the invert function to check if the KeyError is being raised. Testing errors requires different syntax than testing normal outputs. If an error is raised then the function never actually returned anything, so we are unable to `assert` a return value. Instead try the following:

1. Make sure to `import pytest`
2. Use the following code as an example:

```{.python }
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)
```


## 2. Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.

## 3. Submit to Gradescope for Grading

Login to Gradescope and select the assignment named "EX07 - Dictionary Unit Tests". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

Type the following command (all on a single line):

`python -m tools.submission exercises/ex06`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex06.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren't receiving full credit and aren't sure what to try next, come give us a visit in office hours!

## Basic Debugging

If you're not passing autograder tests and don't know why, try locally running your pytests to see if that gives you more insight! You can do that with the following command in your terminal: 

`python -m pytest exercises/ex06/dictionary_test.py`