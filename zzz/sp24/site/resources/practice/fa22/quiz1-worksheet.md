---
title: Quiz 01 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

<!--
Note: this is a copy of the qz01 worksheet from resources/practice/fa21
-->

# Questions

The quiz itself will be similar in difficulty but longer in length than these practice questions. 

Solutions for each problem can be found at the bottom of this page.
  
## Memory Diagrams
1. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz01-question1.png)

<!-- 2. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz01-question2.png)   -->

## Boolean Operators
3. What is the result of the following boolean expressions?  
3.1. `((not False) and True) == True`  
3.2. `(not False) or (True and False)`  
3.3. `True and (7 < 3 * 4 / 6)`  
3.4. `(not False) != True`  
3.5. `not(True and False) and (False or not False)`  

## Conditionals
4. Every `if` statement must have a paired `else` branch. (T/F)
5. Lines contained in an `else` branch in Python do not have to be indented. (T/F)
6. You can name a variable `else` in your program without Python confusing your variable's name and the `else` keyword. (T/F)
7. Given the following code snippet, what is the printed output with the specified values for `x` and `y`?  
![](/static/practice_worksheets/fa21/qz01-question7.png)  
7.1. When x = 3, y = 5?  
7.2. When x = 5, y = 3?  
7.3. When x = -5, y = 1?  
7.4. When x = 13, y = 8?  
7.5. When x = 4, y = 3?

## While Loops
8. Given the following code snippet, what is the printed output once it completes?  
![](/static/practice_worksheets/fa21/qz01-question8.png)

9. Given the following code snippet, what is the printed output once it completes?  
![](/static/practice_worksheets/fa21/qz01-question9.png)

## Lists
10.1. The values in a list cannot be changed while your program is running. (T/F)  
10.2. The last index of a list is the length of the list. (T/F)  
10.3. You can initialize an empty list with no items. (T/F)  
10.4. For the purposes of this class, all items in a list are of the same type. (T/F)  
10.5. While loops inside a function may continue looping after a return statement is reached. (T/F)  
10.6. The condition of a while loop must be a boolean expression (T/F)  

## List Memory Diagrams

11. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question11.png)

12. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz02-question12new.png)

## List Code Tracing

13. Given the following code snippet, answer the questions below.  
![](/static/practice_worksheets/fa21/qz02-question14.png)  
13.1. What is the value of `list_1` once the code snippet completes?  
13.2. What is the value of `i` on line 13 during the _last_ call to `change_and_check`?  
13.3. How many total frames are created on the stack throughout the run of this program (including the globals frame)?

# Solutions

## Memory Diagrams
1. ![](/static/practice_worksheets/fa21/qz01-solution1.png)  

<!-- 2. ![](/static/practice_worksheets/fa21/qz01-solution2.png)   -->

## Boolean Operators
3. 
3.1. `True`  
3.2. `True`  
3.3. `False`  
3.4. `False`  
3.5. `True`

## Conditionals
4. False
5. False
6. False
7. 
7.1. 16.0  
7.2. 2.0  
7.3. -3.0  
7.4. 3.0  
7.5. 1

## While Loops
8. 3   
3  
"1303132"
9. "036910875421"

## Lists
10.1. False  
10.2. False  
10.3. True  
10.4. True  
10.5. False  
10.6. True  

## List Memory Diagrams

11. ![](/static/practice_worksheets/fa21/qz02-solution11.png)

12. ![](/static/practice_worksheets/fa21/qz02-solution12n.png)

## List Code Tracing

13.   
13.1. `[6, 7, 5, 3, 0]`  
13.2. 4  
13.3. 4