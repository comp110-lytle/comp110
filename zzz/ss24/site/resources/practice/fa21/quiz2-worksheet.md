---
title: Quiz 02 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Concepts on Quiz 2

Before working through these practice questions, you should first carefully read this page on [Quiz Expectations](/resources/quiz-expectations.html).

Quiz 2 will cover the following concepts:

* Lessons 13 through 17

# Questions

The quiz itself will be similar in difficulty but longer in length than this practice worksheet.

Solutions for each problem can be found at the bottom of this page.

## Conceptual Questions

1. The values in a list cannot be changed while your program is running. (T/F)
2. The last index of a list is the length of the list. (T/F)
3. You can initialize an empty list with no items. (T/F)
4. For the purposes of this class, all items in a list are of the same type. (T/F)
5. While loops inside a function may continue looping after a return statement is reached. (T/F)
6. The condition of a while loop must be a boolean expression (T/F)
7. Global variables are limited to the scope of the function they are declared in. (T/F)
8. Variables can have the same name but store different values as long as they are defined in the same scope. (T/F)
9. Named constants should be used to store values that may change throughout the program. (T/F)
10. When using a for in loop, on the first line of the loop you must specify the type of the variable (variable refers to `i` in `for i in nums`). (T/F)

## Memory Diagrams

11. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question11.png)

12. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question12new.png)

## Code Tracing
13. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question13.png)  
13.1. What is the printed output once the code snippet completes?  
13.2. What are the values of the global variables `a`, `b`, and `c` once the code snippet completes?

14. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question14.png)  
14.1. What is the value of `list_1` once the code snippet completes?  
14.2. What is the final value of `i` in line 13?  
14.3. How many total frames are created on the stack throughout the run of this program (including the globals frame)?

## Function Writing

15. Write a function called `odd_and_even`. Given a list of `ints`, `odd_and_even` should return a new list containing the elements that are odd and have an even index.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question15demo.png)

16. Write a function named `vowels_and_threes`. Given a string, `vowels_and_threes` should return a new string containing the characters that are either at an index that is a multiple of 3 or a vowel (one or the other, not both). You can assume that the input string is all lowercase, for simplicity.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question16demo.png)

# Solutions

## Conceptual Questions

1. False
2. False
3. True
4. True
5. False
6. True
7. False
8. False
9. False
10. False

## Memory Diagrams

11. ![](/static/practice_worksheets/fa21/qz02-solution11.png)

12. ![](/static/practice_worksheets/fa21/qz02-solution12n.png)

## Code Tracing
13.  
13.1. `[3, 7, 10, 13]`  
13.2. a = 3, b = 0, c = 13.5

14.  
14.1. `[6, 7, 5, 3, 0]`  
14.2. 3  
14.3. 4

## Function Writing

Note:  Your solution does not need to be identical to these, these are just two of many possible solutions.

15. ![](/static/practice_worksheets/fa21/qz02-solution15.png)

16. ![](/static/practice_worksheets/fa21/qz02-solution16.png)