---
title: Quiz 03 Practice
author:
- Megan Zhang
- Jasper Christie
page: quiz3-worksheet
---

# Questions

Below are optional practice problems for Quiz 03. These problems are intended to help you become more comfortable working with dictionaries and lists. This practice is intended to reinforce important concepts and does not necessarily reflect the format of the questions on the quiz.
Solutions for each problem can be found at the bottom of this page.

## Dictionaries T/F
1.	To access a value in a dictionary, you use the format `<dictionary_name>{key}`. (T/F)
2.	One value can be associated with multiple keys. (T/F)
3.	Dictionaries are mutable. In other words, the values in a dictionary can be changed after they are constructed. (T/F)
4.	Dictionaries can have lists or other dictionaries as their _keys_. (T/F)
5.	The `not in` operator can be used to check whether a specific key exists in a dictionary or not. (T/F)
6.	For the purposes of this course, all values in a dictionary are of the same type. (T/F)

## Function Writing 1
7.	Write a function called dictTransform that takes in a dictionary of integer keys and values that are lists of integers (e.g. `dict[int, list[int]]`) and returns a transformed dictionary with every value in a list multiplied by its corresponding key. For example:
`d: dict[int, list[int]] = { 2:[1, 2] , 5:[3, 4] }`
`dictTransform(d) # returns { 2:[2, 4] , 5:[15, 20] }`

## Function Writing 2
8.	Write a function called `listTransform` that takes in a list of dictionaries (e.g. `list[dict[int, str]]`) and returns a transformed list with changes to every even-indexed dictionary. The even-indexed dictionaries should have the odd key values reduced to their first letter and even key values reduced to their last letter. For example:
`l: list[dict[int, str]] = [ { 3:‘roy’ , 2:‘unc’ } , { 1:‘kris’ } , { 9:‘hello’, 11:‘there’, 2:‘!!’ } ]`
`listTransform(l) # returns [ { 3:‘r’ , 2:‘c’ } , { 1:‘kris’ } , { 9:‘h’, 11:‘t’, 2:‘!’} ]`

## Diagramming 1
Given the following code listing, draw an environment diagram.
![](/static/practice_worksheets/qz03-question9.PNG)

## Diagramming 2
Given the following code listing, draw an environment diagram and answer the questions that follow.
![](/static/practice_worksheets/qz03-codelisting1.PNG)

9. When `item` is incremented by `1` on line 9, is `a_table["c"]` mutated?
10. How many arrows come out of the `fill` frame?

# Solutions

## Dictionaries T/F
1.	F
2.	T
3.	T
4.	F
5.	T
6.	T

## Function Writing 1
7. ![](/static/practice_worksheets/qz03-question7-answer.png)

## Function Writing 2
8. ![](/static/practice_worksheets/qz03-question8-answer.png)

## Diagramming 1 
![](/static/practice_worksheets/qz03-question9-answer.png)

## Diagramming 2 
![](/static/practice_worksheets/qz03-question10-answer.png)

9. No. As the loop iterates over `a_table["c"]`, which is a list, `item` is assigned the same value as each value in the list. So for example, in the first iteration of the loop, `item` has the same value as `a_table["c"][0]`, but adding 1 to `item` doesn't change `a_table["c"][0]`.
10. 2

## Lecture Diagrams

## Diagram 3

![](/static/practice_worksheets/class07-review-for-quiz-d3.png)

## Diagram 4

![](/static/practice_worksheets/class07-review-for-quiz-d4.png)

