---
title: Quiz 01 Practice
author:
- Megan Zhang
- Jasper Christie
page: quiz2-worksheet
---

# Questions

Below are optional practice problems for Quiz 1. These problems are intended to help you become more familiar with loops, functions, lists and dictionaries.
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

## Dictionaries T/F
1.	To access a value in a dictionary, you use the format `<dictionary_name>{key}`. (T/F)
2.	One value can be associated with multiple keys. (T/F)
3.	Dictionaries are mutable. In other words, the values in a dictionary can be changed after they are constructed. (T/F)
4.	Dictionaries can have lists or other dictionaries as their _keys_. (T/F)
5.	The `not in` operator can be used to check whether a specific key exists in a dictionary or not. (T/F)
6.	For the purposes of this course, all values in a dictionary are of the same type. (T/F)

## List Diagramming 1
Given the code listing below, draw an environment diagram then answer the questions that follow.

![](/static/practice_worksheets/qz02-question8.png)

1. What is the final value of `x` in the `main` function frame?
2. What is the length of `a_list` after the code has finished running?
3. What are the final items in `a_list`?

## List Diagramming 2
Given the code listing below, draw an environment diagram then answer the questions that follow.

![](/static/practice_worksheets/qz02-question14.PNG)

1. From the `main` frame is `b[2]` defined?
2. From the `main` frame, what are the final items in `a`?

## List Diagramming 3
Given the code listing below, draw an environment diagram then answer the question that follows.

![](/static/practice_worksheets/qz02-question16.PNG)

1. What is the final value of `i` in the make_word frame?

## Loops Diagramming 1
Given the code listing below, draw an environment diagram then answer the questions that follow. 

![](/static/practice_worksheets/qz02-question11.png)

1.	What is the printed output?
2. Write a function call to `listFun` that would return the value “saanhaoaawha”.

## Dictionary Diagramming 1
Given the following code listing, draw an environment diagram.
![](/static/practice_worksheets/qz03-question9.PNG)

## Dictionary Diagramming 2
Given the following code listing, draw an environment diagram and answer the questions that follow.
![](/static/practice_worksheets/qz03-codelisting1.PNG)

1. When `item` is incremented by `1` on line 9, is `a_table["c"]` mutated?
2. How many arrows come out of the `fill` frame?

## Function Writing 1
1. Write a definition for a function called `reverse`, which has one parameter of type str named `string` and returns a str that has all the characters of `string` in reverse order. Use a while loop. For example, a call to `reverse` with "hello" would return "olleh".


## Global Variables
Base your answers to the following questions on the code listing below. 

![](/static/practice_worksheets/qz02-question20.PNG)

1. What is the printed output of this code listing?
2. On line 8, the value of `x` is changed. On what line is `x` declared?
3. Two different variables named `y` are declared. What is the final value of the _global_ variable `y`? 
4. On line 11, a variable `y` is changed. On what line is _this_ `y` declared?

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

## Dictionaries T/F
1.	F
2.	T
3.	T
4.	F
5.	T
6.	T

## List Diagramming 1
![](/static/practice_worksheets/qz02-question8-answer.png)

1. 4
2.	7
3.	[0, 1, 10, 2, 12, 5, 8]

## List Diagramming 2
![](/static/practice_worksheets/qz02-question14-answer.png)

1. No
2. [2, 2, 3]

## List Diagramming 3
![](/static/practice_worksheets/qz02-question16-answer.png)

1. 3

## Loops Diagramming 1
![](/static/practice_worksheets/qz02-question11-answer.png)

1. “yaaohadaaaha”
2. listFun(“snow”)

## Dictionary Diagramming 1 
![](/static/practice_worksheets/qz03-question9-answer.png)

## Dictionary Diagramming 2 
![](/static/practice_worksheets/qz03-question10-answer.png)

1. No. As the loop iterates over `a_table["c"]`, which is a list, `item` is assigned the same value as each value in the list. So for example, in the first iteration of the loop, `item` has the same value as `a_table["c"][0]`, but adding 1 to `item` doesn't change `a_table["c"][0]`.
10. 2

## Function Writing 1
One possible solution is shown below, but there are multiple solutions!
![](/static/practice_worksheets/qz02-question19-answer.PNG)

## Global Variables

1. Output:
~~~plaintext
5
5
~~~
2. Line 3
3. 1
4. Line 10
