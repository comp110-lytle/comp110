---
title: Quiz 02 Practice
author:
- Megan Zhang
- Jasper Christie
page: quiz2-worksheet
---

# Questions

Below are optional practice problems for Quiz 2. These problems are intended to help you become more familiar with loops and lists.
Solutions for each problem can be found at the bottom of this page.

## Lists T/F
1.	The values in a list cannot be changed while your program is running. (T/F)
2.	You can add, change, and remove items in a list. (T/F)
3.	For the purposes of this class, all items in a list are of the same type. (T/F) 
4.	The first index of a list is 1. (T/F)
5.	The last index of a list is the length of the list. (T/F)
6.	You can initialize an empty list with no items. (T/F)
7.	To remove an item, you input the value of the item that you want to remove into the pop() function. (T/F)
8.  While loops inside a function may continue looping after a return statement is reached. (T/F)
9.  A while loop statement can you used anywhere you can write a statement. (T/F)
10.  You can put any kind of statement in the body of a while loop. (T/F)

## List Diagramming 1
Given the code listing below, draw an environment diagram then answer the questions that follow.

![](/static/practice_worksheets/qz02-question8.png)

11. What is the final value of `x` in the `main` function frame?
12. What is the length of `a_list` after the code has finished running?
13. What are the final items in `a_list`?

## List Diagramming 2
Given the code listing below, draw an environment diagram then answer the questions that follow.

![](/static/practice_worksheets/qz02-question14.png)

14. From the `main` frame is `b[2]` defined?
15. From the `main` frame, what are the final items in `a`?

## List Diagramming 3
Given the code listing below, draw an environment diagram then answer the question that follows.

![](/static/practice_worksheets/qz02-question16.png)

16. What is the final value of `i` in the make_word frame?

## Loops Diagramming 1
Given the code listing below, draw an environment diagram then answer the questions that follow. 

![](/static/practice_worksheets/qz02-question11.png)

17.	What is the printed output?
18. Write a function call to `listFun` that would return the value “saanhaoaawha”.

## Function Writing
19. Write a definition for a function called `reverse`, which has one parameter of type str named `string` and returns a str that has all the characters of `string` in reverse order. Use a while loop. For example, a call to `reverse` with "hello" would return "olleh".

## Global Variables
Base your answers to the following questions on the code listing below. 

![](/static/practice_worksheets/qz02-question20.png)

20. What is the printed output of this code listing?
21. On line 8, the value of `x` is changed. On what line is `x` declared?
22. Two different variables named `y` are declared. What is the final value of the _global_ variable `y`? 
23. On line 11, a variable `y` is changed. On what line is _this_ `y` declared?

# Solutions

## Lists T/F
1.	F
2.	T
3.	T
4.	F
5.	F
6.	T
7.	F
8.  F
9.  T
10. T 

## List Diagramming 1
![](/static/practice_worksheets/qz02-question8-answer.png)

11. 4
12.	7
13.	[0, 1, 10, 2, 12, 5, 8]

## List Diagramming 2
![](/static/practice_worksheets/qz02-question14-answer.png)

14. No
15. [2, 2, 3]

## List Diagramming 3
![](/static/practice_worksheets/qz02-question16-answer.png)

16. 3

## Loops Diagramming 1
![](/static/practice_worksheets/qz02-question11-answer.png)

17. “yaaohadaaaha”
18. listFun(“snow”)

## Function Writing
One possible solution is shown below, but there are multiple solutions!
![](/static/practice_worksheets/qz02-question19-answer.png)

## Global Variables

20. Output:
~~~plaintext
5
5
~~~
21. Line 3
22. 1
23. Line 10
