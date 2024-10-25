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
8. Variables can have the same name but store different values if they are defined in a different scope. (T/F)
9. Named constants should be used to store values that may change throughout the program. (T/F)
10. All pytest test function names must begin with `test`.
11. A test will pass if it does not hit a `False` assertion or some other type of error.
12. Test functions should be written in a file with a name matching the file that the functions are defined in, followed by `_test`.
13. When using a `for...in` loop, on the first line of the loop you must specify the type of the variable (variable refers to `i` in `for i in nums`). (T/F)
14. In Python dictionaries, each dictionary's value type must match its key type. (T/F)
15. Writing a `for...in` loop on a `dict` loops through the keys of a dictionary. (T/F)
16. The values in a dictionary cannot be changed once they are assigned. (T/F)
17. Explain the similarities and differences between Python's `list` and `dict`.

## Memory Diagrams

18. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question11.png)

19. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question12new.png)

<!-- 20. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz03-question12.png) -->

## Code Tracing
21. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question13.png)  
21.1. What is the printed output once the code snippet completes?  
21.2. What are the values of the global variables `a`, `b`, and `c` once the code snippet completes?

22. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question14.png)  
22.1. What is the value of `list_1` once the code snippet completes?  
22.2. What is the value of `i` on line 13 during the _last_ call to `change_and_check`?  
22.3. How many total frames are created on the stack throughout the run of this program (including the globals frame)?

<!-- ## Function Writing

23. Write a function called `odd_and_even`. Given a list of `ints`, `odd_and_even` should return a new list containing the elements that are odd and have an even index.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question15demo.png)

24. Write a function named `vowels_and_threes`. Given a string, `vowels_and_threes` should return a new string containing the characters that are either at an index that is a multiple of 3 or a vowel (one or the other, not both). You can assume that the input string is all lowercase, for simplicity.  
Example Usage:  
![](/static/practice_worksheets/fa21/qz02-question16demo.png)

25. Write a function called `average_grades`. Given a dictionary with `str` keys and `list[int]` values, `average_grades` should return a new dictionary of type `dict[str, float]` that maps each student to their average.  
![](/static/practice_worksheets/sp22/qz02-solution17.png) -->

# Solutions

## Conceptual Questions

1. False
2. False
3. True
4. True
5. False
6. True
7. False
8. True
9. False
10. True
11. True
12. True
13. False
14. False
15. True
16. False
17.   
Similarities:  
Both are collections that can be looped through using a `for...in` loop, reference types that live on the heap, mutable, can duplicate values, subscription notation to access values, `.pop()` to remove items  
Differences:  
`list` -- Index by increasing integers, add items with `.append()`, ordered, `for...in` loop gives items  
`dict` -- Matched Key-Value pairs, pair with assignment operator `=` (`dict_name[key] = value`), control over key type (not limited to `int`), `for...in` gives keys  
Note: these are not all of the similarities and differences, just some important ones to remember

## Memory Diagrams

18.   ![](/static/practice_worksheets/fa21/qz02-solution11.png)

19.   ![](/static/practice_worksheets/fa21/qz02-solution12n.png)

<!-- 20.   ![](/static/practice_worksheets/fa21/qz03-solution12.png) -->

## Code Tracing
21.   
21.1. `[3, 7, 10, 13]`  
21.2. a = 3, b = 0, c = 13.5

22.   
22.1. `[6, 7, 5, 3, 0]`  
22.2. 4  
22.3. 4

<!-- ## Function Writing

Note:  Your solution does not need to be identical to these, these are just two of many possible solutions.

23.  ![](/static/practice_worksheets/fa21/qz02-solution15.png)

24.  ![](/static/practice_worksheets/fa21/qz02-solution16.png)

25.  ![](/static/practice_worksheets/fa21/qz03-solution14.png) -->