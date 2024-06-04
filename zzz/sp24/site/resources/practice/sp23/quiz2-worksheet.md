---
title: Quiz 02 Practice
author:
- Megan Zhang
- David Karash
- Coralee Vickers
- Alyssa Byrnes
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

12. Produce a memory diagram for the following code snippet, being sure to include its stack, heap, and output.  
![](/static/practice_worksheets/fa21/qz02-question11.png)

13. Produce a memory diagram for the following code snippet, being sure to include its stack, heap, and output.  
![](/static/practice_worksheets/fa21/qz02-question12new.png)

14. Produce a memory diagram for the following code snippet, being sure to include its stack, heap, and output.  
<img class="img-fluid" src="/static/practice_worksheets/sp23/cora1.png"/>

<!-- 20. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz03-question12.png) -->

## Code Tracing
15. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question13.png)  
15.1. What is the printed output once the code snippet completes?  
15.2. What are the values of the global variables `a`, `b`, and `c` once the code snippet completes?

16. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question14.png)  
16.1. What is the value of `list_1` once the code snippet completes?  
16.2. What is the value of `i` on line 13 during the _last_ call to `change_and_check`?  
16.3. How many total frames are created on the stack throughout the run of this program (including the globals frame)?

## Function Writing



17. Odd and Even: [instructions](/static/practice_worksheets/sp23/qz02-pp1.pdf)
18. Value Exists: [instructions](/static/practice_worksheets/sp23/qz02-pp2.pdf) 
19. Short Words: [instructions](/static/practice_worksheets/sp23/qz02-pp3.pdf) 

### Autograder instructions:
Join the Gradescope class for practice problems with the code: 4V7PB5
(Do this by going to your [Gradescope](https://www.gradescope.com/) homepage and clicking on "Enroll in Course")
**Do not compress these files before submitting. Simply submit the `.py` files.**

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

14.   <img class="img-fluid" src="/static/practice_worksheets/sp23/cora1_sol.png" />

## Code Tracing
15.   
15.1. `[3, 7, 10, 13]`  
15.2. a = 3, b = 0, c = 13.5

16.   
16.1. `[6, 7, 5, 3, 0]`  
16.2. 4  
16.3. 4

## Function Writing

Note:  Your solution does not need to be identical to these, these are just examples of one of many possible solutions.

17.  ![](/static/practice_worksheets/fa21/qz02-solution15.png)


18. ![](/static/practice_worksheets/sp23/coding2_sol.png)

19. ![](/static/practice_worksheets/sp23/coding3_sol.png)