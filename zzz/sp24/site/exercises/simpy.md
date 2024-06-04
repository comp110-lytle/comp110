---
title: EX09 - Simpy
author:
- Kris Jordan
- Kaki Ryan
page: exercises
template: overview
---

## Overview

In Exercise 09, you will write a utility class for working with a column of numerical values. This will give practice with constructors, methods, operator overloading and more. In the process, you will develop a keen understanding for the intuition and abstractions provided by a highly popular and valuable to understand library called `NumPy`. We will explore _NumPy_ later in the course!

In this exercise, you will build-up an abstraction, with many powerful capabilities, in the form of a class called `Simpy`.

<!-- ** There are some new concepts in this exercise, for more info on them, check out Campuswire! ** -->


## 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex09`. If you expand that directory, you should see the starter file for the three functions you'll be writing.
4. If you do not see the `ex09` directory, try once more but selecting `"Pull From"` and select `origin` or `upstream` in step 2. If you expand that directory, you will see the starter files: `Simpy.py` and `SimpyDemos.ipynb`.

Assignment Outline

* Parts 0 through 10 -- 80 Points Autograded
* Checks for Understanding #1 and # 2 -- 10 Points Handgraded
* Style, Linting -- 10 Points Autograded

## 1. Starter Files

Your work in this exercise will be completed across two files:

1. `Simpy.py` - This is the Python module where your `Simpy` class is implemented.

2. `SimpyDemos.ipynb` - This is the Jupyter Notebook file that walks you through each of the methods of `Simpy` and provides sample uses. There are additionally a few _check for understanding_ cells that will ask you to solve problems in terms of methods you previously implemented. (If you are having getting Jupyter notebooks running, you can work in the alternative `SimpyDemos.py` file.)

The descriptions of the functions you will need to implement, as well as example code that makes use of those functions once they are correctly implemented, can be found in the `SimpyDemos.ipynb` file.

If your screen is large enough, you are encouraged to open these files side-by-side in VSCode by dragging the tab of one to the right side of VSCode so that it changes to a split pane view. Closing your file explorer can help give you additional horizontal space.

**Be sure to save your work in `Simpy.py` before reevaluating cells in `SimpyDemos.ipynb`. Sometimes the Jupyter Notebook can reach a bad state and the only way to fix is to close your `ipynb` tab and reopen a new one, thus restarting the kernel.**

## Autograding

Save your `.ipynb` file before submission! You should have _Run All_ cells to do so.

Login to Gradescope and select the assignment named "EX09 - Simpy". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

To produce a zip file for `ex09`, type the following command (all on a single line):

`python -m tools.submission exercises/ex09`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex09.zip". The "mm", "dd", and so on, are timestamps with the current month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be 10 points manually graded for the `Checks for Understanding` cells in the notebook being completed. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren’t receiving full credit and aren’t sure what to try next, come give us a visit in office hours!