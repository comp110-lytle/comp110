---
title: CQ12 - Sorting Algorithms 
author:
- Viktorya Hunanyan
page: exercises
template: overview
---

In this challenge question, you will create two functions that do the same thing except in two different ways! You will implement a selection sort and insertion sort. Both algorithms organize a list of numbers in non-decreasing order, but they do so in distinct ways. Before you being, in create a python file called `sorting_algorithms` in your `CQs` folder. You will write your functions in this file. 

# selectrion_sort()

The *Selection Sort* algorithm sorts a list by repeatedly finding the smallest element from the unsorted portion and swapping it with the first unsorted element. For each pass through the list, it identifies the minimum value in the remaining unsorted elements and positions it at the correct location.

Your task is to define the funciton `selection_sort()`. This function should: 

- 1. Iterate through the list to find the minimum value in the unsorted part. 
- 2. Swap this minimum value with the first unsorted element.

Continue this process until the entire list is sorted.

Here’s a visual representation of the *Selection Sort* process for the list `[29, 10, 14, 37, 14]`:

| **Pass** | **Current List**          | **Comparison**                    | **Min Element** | **Swap (if needed)**      | **Resulting List**       |
|----------|---------------------------|-----------------------------------|-----------------|---------------------------|--------------------------|
| Pass 1   | `[29, 10, 14, 37, 14]`     | `29 > 10 → min = 10` <br> `10 < 14` <br> `10 < 37` <br> `10 < 14` | `10`            | Swap `29` and `10`         | `[10, 29, 14, 37, 14]`   |
| Pass 2   | `[10, 29, 14, 37, 14]`     | `29 > 14 → min = 14` <br> `14 < 37` <br> `14 < 14` | `14`            | Swap `29` and `14`         | `[10, 14, 29, 37, 14]`   |
| Pass 3   | `[10, 14, 29, 37, 14]`     | `29 < 37` <br> `29 > 14 → min = 14` | `14`            | Swap `29` and `14`         | `[10, 14, 14, 37, 29]`   |
| Pass 4   | `[10, 14, 14, 37, 29]`     | `37 > 29 → min = 29`              | `29`            | Swap `37` and `29`         | `[10, 14, 14, 29, 37]`   |
| Pass 5   | `[10, 14, 14, 29, 37]`     | No comparisons (only one element) | `—`             | No swap (already sorted)   | `[10, 14, 14, 29, 37]`   |

Here is an example usage of your function: 

~~~ {.plaintext}
>>> from CQs.sorting_algorithms import selection_sort
>>> x: list[int] = [4, 6, 8, 89, 0, -1]
>>> selection_sort(x)
>>> print(x)
[-1, 0, 4, 6, 8, 89]
>>> y: list[int] = [0, -5, -4, -100, 0, -1]
>>> selection_sort(y)
>>> print(y)
[-100, -5, -4, -1, 0, 0]
~~~

# insertion_sort()

The *Insertion Sort* algorithm sorts a list by building a sorted portion of the list one element at a time. For each element in the unsorted part, it places it in the correct position relative to the already sorted part of the list. This is done by shifting elements that are greater than the current element to the right to make room for it.

Your task is to define the function `insertion_sort()`. This function should:

1. Begin at the second element in the list and treat the element as the "key."
2. Shift elements of the sorted portion that are greater than the key one position to the right.
3. Insert the key in its correct sorted position.

Continue this process until the entire list is sorted.

Here's a visual representation of the *Insertion Sort* process for the list `[29, 10, 14, 37, 14]`:

| **Pass** | **Current List**          | **Key Element** | **Shifts**                          | **Resulting List**       |
|----------|---------------------------|-----------------|-------------------------------------|--------------------------|
| Pass 1   | `[29, 10, 14, 37, 14]`    | `10`           | `29` shifts right                  | `[10, 29, 14, 37, 14]`   |
| Pass 2   | `[10, 29, 14, 37, 14]`    | `14`           | `29` shifts right                  | `[10, 14, 29, 37, 14]`   |
| Pass 3   | `[10, 14, 29, 37, 14]`    | `37`           | No shifts                          | `[10, 14, 29, 37, 14]`   |
| Pass 4   | `[10, 14, 29, 37, 14]`    | `14`           | `37` shifts right, `29` shifts right | `[10, 14, 14, 29, 37]`   |
| Pass 5   | `[10, 14, 14, 29, 37]`    | —              | List is already sorted             | `[10, 14, 14, 29, 37]`   |

Here is an example usage of your function: 

~~~ {.plaintext}
>>> from CQs.sorting_algorithms import insertion_sort
>>> x: list[int] = [4, 6, 8, 89, 0, -1]
>>> insertion_sort(x)
>>> print(x)
[-1, 0, 4, 6, 8, 89]
>>> y: list[int] = [0, -5, -4, -100, 0, -1]
>>> insertion_sort(y)
>>> print(y)
[-100, -5, -4, -1, 0, 0]
>>> z: list[int] = [1, 0, 0, 1, 0, -1]
>>> insertion_sort(z)
>>> print(z)
[-1, 0, 0, 0, 1, 1]
~~~

Again, notice that the you will result in the same sorted lists for both `insertion_sort()` and `selectrion_sort()` as they do the same thing excpet in two different ways.

# Submission 

Create a .zip file by running the following command in your terminal:

python -m tools.submission CQs/sorting_algorithms.py

Then, drag and drop that .zip file into Gradescope!

