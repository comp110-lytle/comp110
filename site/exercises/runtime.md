---
title: EX07 - Runtime Analysis
author:
- Alyssa Lytle
- Vrinda Desai
page: exercises
template: overview
---

 
## Introduction

In this assignment, you're going to be modifying an existing code base to add implementation of some basic sorting algorithms. Then you will analyze and *visualize* their runtime!

Note that there are *two* types of submission for this assignment! (You will see this on Gradescope as well!)

### Learning Objectives

- Learn to modify an existing code base
- Learn to implement an existing algorithm
- Visualize worst case runtimes and gain a better understanding of "Big-O" notation


## 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex07`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `ex07` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Troubleshooting
If you're having trouble pulling, try:

* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`

If you're still having issues, come to office hours!


## Part 1. Implementing Sort Algorithms

### 1a. Selection Sort

The first algorithm you're going to be implementing is Selection Sort!

The *skeleton* for this function already exists in `sort_functions.py`. *This is the only file in the EX07 directory you should worry about at this point! We will get to the rest later!* You will add functionality to it by completing the body of the code!

*TODO: add more instruction and usage example*

### 1b. Insertion Sort

The first algorithm you're going to be implementing is Selection Sort!

The *skeleton* for this function already exists in `sort_functions.py`. You will add functionality to it by completing the body of the code!

*TODO: add more instruction and usage example*

## Part 2. Generating Worst-Case Inputs

For both selection and insertion sort, we want to analyze how *fast* they are in terms of runtime. More specifically, we want to measure their Big-O runtime. This is the amount of time it would take to run this algorithm given the *worst possible input*.

(TODO: add explanation of why decreasing is worst possible input.)

In `runtime_analysis_functions.py` you will see the skeleton for a function called `random_descending_list`. (There are other functions in there, too, but we will talk about those in a bit!)
You are going to give `random_descending_list` some functionality!
The goal is to **create** and **return** a list of length `n` of random numbers in decreasing order. You will see a global constant established of MAX_VAL. Let that be the *first* element of your list, and then append randomly decreasing numbers. 

(Hint: You will want to import and use the `randint` function from the `random` library.)

You can implement the "randomness" how you choose. The main goal is that the output is different each time and strictly decreasing!

Here's an example of usage. (Note that your results will be different since this is a *randomized* function.)

<pre>
<div class="terminal">    $ python
    >>> from exercises.ex07.runtime_analysis_functions import random_descending_list
    >>> random_descending_list(10)
    [100000, 99987, 99957, 99919, 99905, 99892, 99809, 99742, 99684, 99662]
    >>> random_descending_list(10)
    [100000, 99920, 99876, 99848, 99814, 99747, 99701, 99691, 99596, 99502]
    >>> random_descending_list(3)
    [100000, 99988, 99906]
</div>
</pre>



## Part 3. Analyzing Runtime + Memory Usage

Now that you've written your sort algorithms and have a way of generating a worst-case input, we are going to test the *runtime* and *memory usage* of these inputs. 

### 3A. Analyzing Runtime

For this part, you are going to *use* the `evaluate_runtime` function defined in `runtime_analysis_functions.py`. This function has already been written for you, so you just need to implement it. It takes a function as input and computes its runtime for inputs of increasing size.

Create a new file in your `EX07` directory called `evaluate_algorithms.py`.

Start by adding an `__author__` variable and the following constants:

```
    START_SIZE: int = 0
    END_SIZE: int = 1000
```


You can call this function and visualize the result with the following code. *Replace ONYEN in line 3 with your ONYEN!*
(You will need to import `evalute_runtime` from `runtime_analysis_functions.py` first!)

```
    times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
    plt.plot(times)
    plt.title("Runtime Analysis of Selection Sort - ONYEN")
    plt.show()
```

It should generate an image that looks something like this:

<img class="img-fluid" src="/static/assets/ex-runtime/sel_sort_runtime.png" />

Save this image and upload it to Gradescope under the assignment EX07 - Part A.

Now, repeat these steps, but for insertion sort!

```
    times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
    plt.plot(times)
    plt.title("Runtime Analysis of Insertion Sort - ONYEN")
    plt.show()
```


### 3B. Analyzing Memory Usage

Now, we are going to analyze the memory usage of the algorithms! You will import and call the `evaluate_memory_usage` function from `runtime_analysis_functions.py`. This function uses a python library called `tracemalloc` to measure how many blocks of memory your function call is using. Similar to `evaluate_runtime`, it measures memory usage for an increasing number of input sizes so we can visualize how memory usage changes as input size changes.

```
    usage = evaluate_memory_usage("selection_sort", [l], START_SIZE, END_SIZE)
    plt.plot(usage)
    plt.title("Memory Usage Analysis of Selection Sort - ONYEN")
    plt.show()

    usage = evaluate_memory_usage("insertion_sort", [l], START_SIZE, END_SIZE)
    plt.plot(usage)
    plt.title("Memory Usage Analysis of Insertion Sort - ONYEN")
    plt.show()
```

## Submission

TODO