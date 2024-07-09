---
title: Quiz 02 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

<!--
Note: this wkst pulls from the qz02 and qz03 worksheets from resources/practice/fa21 with some
minor changes/additions
-->

# Questions

The quiz itself will be similar in difficulty to this practice worksheet.

Solutions for each problem can be found at the bottom of this page.

## Conceptual Questions

1. Global variables are limited to the scope of the function they are declared in. (T/F)
2. Variables can have the same name but store different values if they are defined in a different scope. (T/F)
3. Named constants should be used to store values that may change throughout the program. (T/F)
4. All pytest test function names must begin with `test`.
5. A test will pass if it does not hit a `False` assertion or some other type of error.
6. Test functions should be written in a file with a name matching the file that the functions are defined in, followed by `_test`.
7. When using a `for...in` loop, on the first line of the loop you must specify the type of the variable (variable refers to `i` in `for i in nums`). (T/F)
8. In Python dictionaries, each dictionary's value type must match its key type. (T/F)
9. Writing a `for...in` loop on a `dict` loops through the keys of a dictionary. (T/F)
10. The values in a dictionary cannot be changed once they are assigned. (T/F)
11. Explain the similarities and differences between Python's `list` and `dict`.

## Memory Diagrams

12. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question11.png)

13. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question12new.png)

<!-- 20. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz03-question12.png) -->

## Code Tracing
14. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question13.png)  
14.1. What is the printed output once the code snippet completes?  
14.2. What are the values of the global variables `a`, `b`, and `c` once the code snippet completes?

15. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question14.png)  
15.1. What is the value of `list_1` once the code snippet completes?  
15.2. What is the value of `i` on line 13 during the _last_ call to `change_and_check`?  
15.3. How many total frames are created on the stack throughout the run of this program (including the globals frame)?

## Function Writing

16. Write a function called `odd_and_even`. Given a list of `ints`, `odd_and_even` should return a new list containing the elements that are odd and have an even index.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question15demo.png)

17. Write a function named `vowels_and_threes`. Given a string, `vowels_and_threes` should return a new string containing the characters that are either at an index that is a multiple of 3 or a vowel (one or the other, not both). You can assume that the input string is all lowercase, for simplicity.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question16demo.png)

18. Write a function called `average_grades`. Given a dictionary with `str` keys and `list[int]` values, `average_grades` should return a new dictionary of type `dict[str, float]` that maps each student to their average.  
![](/static/practice_worksheets/sp22/qz02-solution17.png)

# Solutions

## Conceptual Questions

1. False
2. True
3. False
4. True
5. True
6. True
7. False
8. False
9. True
10. False
11.   
Similarities:  
Both are collections that can be looped through using a `for...in` loop, reference types that live on the heap, mutable, can duplicate values, subscription notation to access values, `.pop()` to remove items  
Differences:  
`list` -- Index by increasing integers, add items with `.append()`, ordered, `for...in` loop gives items  
`dict` -- Matched Key-Value pairs, pair with assignment operator `=` (`dict_name[key] = value`), control over key type (not limited to `int`), `for...in` gives keys  
Note: these are not all of the similarities and differences, just some important ones to remember

## Memory Diagrams

12.   ![](/static/practice_worksheets/fa21/qz02-solution11.png)

13.   ![](/static/practice_worksheets/fa21/qz02-solution12n.png)


## Code Tracing
14.   
14.1. `[3, 7, 10, 13]`  
14.2. a = 3, b = 0, c = 13.5

15.   
15.1. `[6, 7, 5, 3, 0]`  
15.2. 4  
15.3. 4

## Function Writing

Note:  Your solution does not need to be identical to these, these are just two of many possible solutions.

16.  ![](/static/practice_worksheets/fa21/qz02-solution15.png)

17.  ![](/static/practice_worksheets/fa21/qz02-solution16.png)

18.  ![](/static/practice_worksheets/fa21/qz03-solution14.png)