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

You will find the starter files needed by "pulling" from the course workspace repository. Follow these steps: 

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex07`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `ex07` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Troubleshooting
If you're having trouble pulling:

* Make sure you PUSHED all of your changes to backup first!!!
* In your terminal, type `git config pull.rebase false`
* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`. (If not an option, do `Origin` -> `Main`.) 

If you're still having issues, come to office hours!


## Part 1. Implementing Sort Algorithms

### 1a. Selection Sort

The first algorithm you're going to be implementing is Selection Sort!

The *skeleton* for this function already exists in `sort_functions.py`. *This is the only file in the EX07 directory you should worry about at this point! We will get to the rest later!* You will add functionality to it by completing the body of the code!

Based on our class discussion, selection sort is an algorithm that repeatedly finds the minimum element in an unsorted portion of a list and if it is smaller, it will be swapped with the current element (the first elememt in the unsorted portion). Selection sort is an in-place sorting aglorithm which means it will modify and return the list that is passed in as an argument. It also means you will not create additional instances of lists in your implementation. Your implementation can be broken down into a few steps:

1. Create a counter variable to track the indices of the list. 
2. Set up an overaching loop to iterate through the list. 
3. Find the index of the minimum element only from the portion of your list that is greater than the counter value (the unsorted portion). 
    3.1 You cannot use Python's built-in `min()` function. You will need another loop, a secondary counter set to the value of the first counter, and a variable to store the index of the minimum element. 
4. Note that the current element is the value in the list at the index of the counter value.
5. Compare the minumum element to the current element, if the minumum element is smaller, swap them.
    5.1 Swapping means taking the value at two different indices and replacing the first index with element at the second while also replacing the second index with the element that was at the first. You will need a temporary `int` variable to accomplish this.
6. Increment your counter (if necessary), the indices in the list that are less than the counter value are the sorted portion. 

<pre>
<div class="terminal">
>>> from exercises.ex07.sort_functions.py import selection_sort
>>> list1: list[int] = [2, 4, 3, 6]
>>> selection_sort(list1)
>>> list1
[2, 3, 4, 6]
>>> list2: list[int] = [-7, -8, -9, -10]
>>> selection_sort(list2)
>>> list2
[-10, -9, -8, -7]
</div>
</pre>

### 1b. Insertion Sort

The second algorithm you're going to implement is Insertion Sort.

The *skeleton* for this function already exists in `sort_functions.py`. You will add functionality to it by completing the body of the code!

Rather than finding the minimum element in the unsorted portion of the list, you will iterate through the unsorted portion and place elements where they belong in the sorted portion. Just like selection sort, insertion sort is also an in-place sorting aglorithm. Keep in mind the zeroeth element in a list is already "sorted" before you've even started. Your implementation can be broken down into a few steps:

1. Create a index variable to track the sorted indicies in the list. 
2. Set up an overaching loop to iterate through the list excluding the final element. Create another index variable to track the unsorted indices in the list, it is 1 greater than the value of the sorted index. 
3. Note that the current element is the value in the list at the index of the unsorted index value.
4. Now, moving "backwards" (by descending indices), you will compare the current element to all elements in the sorted part of the list and make swaps as you go.
    4.1 Set up a loop that checks if your unsorted index is greater than zero and the current element is less than the one directly before it.
    4.2 Just as you did in selection sort, swap the two elements. 
    4.3 Decrement the unsorted index variable. 
5. Increment the sorted index variable. 

<pre>
<div class="terminal">
>>> from exercises.ex07.sort_functions.py import insertion_sort
>>> list1: list[int] = [2, 4, 3, 6]
>>> insertion_sort(list1)
>>> list1
[2, 3, 4, 6]
>>> list2: list[int] = [-7, -8, -9, -10]
>>> insertion_sort(list2)
>>> list2
[-10, -9, -8, -7]
</div>
</pre>

## Part 2. Generating Worst-Case Inputs

For both selection and insertion sort, we want to analyze how *fast* they are in terms of runtime. More specifically, we want to measure their Big-O runtime. This is the amount of time it would take to run this algorithm given the *worst possible input*.

For example, a list in decreasing order would be the worst possible input (i.e. [6, 5, 4, 3, 2]). For insertion sort, we would need to compare every number in the list to all of the numbers in the sorted portion and also make as many swaps (discounting the zeroeth number). Consider how many comparisons and swaps would be needed for an already sorted list (a list in increasing order). That's right, there would be as many comparisons as numbers in the list (discounting the zeroeth number) and no swaps! 

### 2a. Random Descending List

In `runtime_analysis_functions.py` you will see the skeleton for a function called `random_descending_list`. (There are other functions in there, too, but we will talk about those in a bit!) 

The goal is to **create** and **return** a list of length `n` of random numbers in decreasing order. You will see a global constant established of MAX_VAL. Let that be the *first* element of your list, and then append randomly decreasing numbers. 

<pre>
<div class="terminal">
>>> from exercises.ex07.runtime_analysis_functions.py import random_descending_list
>>> random_descending_list(3)
[27044, 19412, -79086]
>>> random_descending_list(4)
[4535, -74690, -157006, -183592]
</div>
</pre>

(Hint: You will want to import and use the `randint` function from the `random` library.)

Before you move on to the next portion, feel free to submit your code to Gradescope under the assignment EX07 - Part A. The autograder for this assignment will merely check the basic functionality of the functions you have written, it does not ensure you have the correct, canonical implementation. 

## Part 3. Analyzing Runtime + Memory Usage

Now that you've written your sort algorithms and have a way of generating a worst-case input, we are going to test the *runtime* and *memory usage* of these inputs. 

### 3a. Analyzing Runtime

For this part, you are going to *use* the `evaluate_runtime` function defined in `runtime_analysis_functions.py`. This function has already been written for you, so you just need to implement it. It takes a function as input and computes its runtime for inputs of increasing size.

Create a new file in your `ex07` directory called `evaluate_algorithms.py`.

Start by adding an `__author__` variable and the following constants:

```
    START_SIZE: int = 0
    END_SIZE: int = 1000
```

Then import `evalute_runtime` from `runtime_analysis_functions.py`. Finally, call the `evaluate_runtime` function and visualize the result with the following code. Replace ONYEN in line 3 with your ONYEN:

```
    times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
    plt.plot(times)
    plt.title("Runtime Analysis of Selection Sort - ONYEN")
    plt.show()
```

It should generate an image that looks something like this:

![example-pic](../static/assets/ex-runtime/sel_sort_runtime.png)

Save this image and upload it to Gradescope under the assignment EX07 - Part B.

Now, repeat these steps, but for insertion sort!

```
    times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
    plt.plot(times)
    plt.title("Runtime Analysis of Insertion Sort - ONYEN")
    plt.show()
```


### 3B. Analyzing Memory Usage

Now, we are going to analyze the memory usage of the algorithms! You will import and call the `evaluate_memory_usage` function from `runtime_analysis_functions.py`. This function uses a python library called `tracemalloc` to measure how many blocks of memory your function call is using. Similar to `evaluate_runtime`, it measures memory usage for an increasing number of input sizes so we can visualize how memory usage changes as input size changes.

This graph should look *linear*!

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

Save these images and upload them to Gradescope under the assignment EX07 - Part B.

## Submission

To produce a zip file for `ex07`, type the following command (all on a single line):

`python -m tools.submission exercises/ex07`

Upload this to Gradescope under "EX07 - Part A".