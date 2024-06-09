# remove_repeats CQ

## Introduction

In this CQ, we will practice writing a function that mutates a list using loops and indexing. The function, remove_repeats, will take a list as input and modify it to remove any duplicate values, ensuring that each value appears only once.

## Part 0. Setup Instructions

Write click on your “lessons” folder and select “New File”. Your new file will be titled list_repeats.py. In this file, start by adding a docstring at the top to describe the file’s purpose. Below the docstring, initialize the __author__ variable to include your name.


## Part 1. remove_repeats

remove_repeats will be a function that takes a list of integers and removes any repeated values from the list. The function does not return anything; instead, it mutates the list to ensure that each number appears only once. The order of the list is preserved, maintaining the first occurrence of each number. Example usage is shown below:

Example 1. 
a: list[int] = [10, 10, 10]
print(remove_repeats(a))  # expect None
print(a)  # expect [10]

Example 2. 
b: list[int] = [40, 10, 10, 10, 20, 30, 40, 20, 9]
print(remove_repeats(a))  # expect None
print(a)  # expect [40, 10, 20, 30, 9]

Now that we understand how we want to mutate our list, the core challenge is determining how to achieve this.

We want to iterate through the list and remove any occurrences of each value beyond its first appearance. For example, in Example 2, if we start with the value at the zeroth index, 40, we will iterate through the rest of the list and remove any subsequent occurrences of 40. After processing the value at zeroth index, we move on to the next value (in Example 2, this would be 10) and repeat the process until we have checked all the list for any occurances of the next value at the next index.

Hint: When you start removing a value from the list, take some paper and sketch out what happens to the list when an element is removed. Consider how the indices of the remaining elements change. How does this affect your strategy for incrementing the index as you iterate through the list?

This function might be more challenging than what you are used to writing, but it's excellent practice for developing problem-solving skills. For many of you, this function will be a milestone in your journey toward becoming more proficient in programming and computational thinking!

## Part 3. Grading and Submission

### Grading
For this assignment we will be checking that your function correctly mutates the input list properly and you are not returning a new list with the expected mutation. 

### Submit to gradescope
Create a .zip file by running the following command in your terminal:

python -m tools.submission lessons/list_repeats.py

Then, go to Gradescope and click on the assignment. Then click on a the file box and search for the zip file you just created. 
Requirements: Technical requirements the unit tests will certainly check for.
Formatting and Documentation:  Expectations for documentation which is standard throughout the semester.
Code Review: Details that TAs may look for in manual grading.