---
title: EX10 - Data Wrangling
author:
- Kaki Ryan
- Izzy Ford
- Kris Jordan
page: exercises
template: overview
---

## Overview

In Exercise 10, you will write some additional utility functions for _wrangling_ data from a raw CSV data file into representations more conducive for computing. In the process, you will gain experience and comfort working with `dict` and `list` data structures.

In order to complete this exercise, you **must** watch and follow along with Thursday's (11/30) lecture, where we provide you with the code for several of the necessary functions to complete this assignment.

In this exercise, you will move through a very common first set of steps when working with a new data set:

1. Read the data
2. Transform it to be in a "shape" that is easier to work with
3. Preview and select just the parts of the dataset you are interested in
4. Run (simple, in this notebook) analyses

The sample data set provided alongside this exercise is police stop data from Durham, as compiled by the [Stanford Open Policing Project](https://openpolicing.stanford.edu/data/). 

There are two files you will be working in: `data_utils.py` and `data_wrangling.ipynb`. The first is where you will be writing your function definitions. You should copy over your functions from the lesson on CSV file reading into this file. The Jupyter notebook will guide you through the exercise and lead you through a simple analysis. All you need to do here is run the cells. You will get some baseline credit just for running them and moving through the steps as instructed.

Assignment Outline

* `head` -- 30 Points Autograded
* `select` -- 25 Points Autograded
* `concat` -- 15 Points Autograded

* Did you run the notebook cells and save the values of outputs before submission? -- 10 Points Handgraded
* Style, Linting, Typing -- 20 Points Autograded

This means anything in the notebook that is not included in this outline was either provided to you in one of the earlier videos or is optional!

## 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex10`. If you expand that directory, you should see the starter file for the three functions you'll be writing.
4. If you do not see the `ex10` directory, try once more but selecting `"Pull From"` and select `origin` in step 2. If you expand that directory, you will see the starter files: `data_utils.py` and `data_wrangling.ipynb`. Additionally, you will see a CSV file in the `data/` directory with the sample traffic stops from one week in Durham in 2015.

## 1. Starter Files

Note, this exercise makes use of functions that were first introduced in the lesson on CSV file Reading. You will use files defined in `data_utils.py` from that lesson and additional functions to it in this exercise.

Your work in this exercise will be completed across two files:

1. `data_utils.py` - This is the Python module where you will implement utility functions for working with data.

2. `data_wrangling.ipynb` - This is the Jupyter Notebook file that makes use of the utility functions 

The descriptions of the functions you will need to implement, as well as example code that makes use of those functions once they are correctly implemented, can be found in the `data_wrangling.ipynb` file.

If your screen is large enough, you are encouraged to open these files side-by-side in VSCode by dragging the tab of one to the right side of VSCode so that it changes to a split pane view. Closing your file explorer can help give you additional horizontal space.

**Be sure to save your work in `data_utils.py` before reevaluating cells in `data_wrangling.ipynb`.**

## Autograding

**BEFORE SUBMITTING YOUR ASSIGNMENT FOR SUBMISSION, BE SURE TO SAVE YOUR WORK IN YOUR JUPYTER NOTEBOOK!!!** After submission, view the files of your submission to be sure your notebook's cells' output is visible in the submission on Gradescope. If not, save your notebook and resubmit.

Login to Gradescope and select the assignment named "ex10 - Data Wrangling". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

To produce a zip file for `ex10`, type the following command (all on a single line):

`python -m tools.submission exercises/ex10`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex10.zip". The "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be points manually graded for style – using meaningful variable names and snake_case. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren’t receiving full credit and aren’t sure what to try next, come give us a visit in office hours!