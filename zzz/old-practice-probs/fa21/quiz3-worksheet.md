---
title: Quiz 03 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Concepts on Quiz 3

Before working through these practice questions, you should first carefully read this page on [Quiz Expectations](/resources/quiz-expectations.html).

Quiz 3 will cover the following concepts:

* Lessons 18 through 21

# Questions

The quiz itself will be similar in difficulty but longer in length than this practice worksheet.

Solutions for each problem can be found at the bottom of this page.

## Conceptual Questions

1. To access a value in a dictionary, you use the format `dictionary_name{key}`. (T/F)
2. Multiple keys can have the same value. (T/F)
3. The values in a dictionary cannot be changed after the dictionary is constructed. (T/F)
4. The `not in` operator can be used to check whether a specific key exists in a dictionary. (T/F)
5. For the purposes of this course, all values in a dictionary are of the same type. (T/F)
6. Dictionaries can have lists or other dictionaries as their _keys_. (T/F)
7. In a Jupyter Notebook, you may evaluate the cells in any order. (T/F)
8. You should write comments in a Python cell to narrate your code in a Jupyter Notebook. (T/F)
9. Cells will automatically print output below them if the final line of the code assigns a value to a variable. (T/F)
10. Restarting the Jupyter notebook’s kernel erases all of its variables that were previously assigned by running cells. (T/F)

## Memory Diagrams

11. Produce a memory diagram for the following code snippet, being sure to include its stack and output.
![](/static/practice_worksheets/fa21/qz03-question11.png)  
11.1 Describe in words what the `scan` function does.

12. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz03-question12.png)

## Function Writing

13. Write a function called `dict_transform`. Given a dictionary with `int` keys and `list[int]` values, `dict_transform` should return the dictionary with every value in a list multiplied by its corresponding key.  
Example: `dict_transform({ 2:[1,2] , 5:[3,4] })` returns `{ 2:[2,4] , 5:[15,20] }`.

14. Write a function called `average_grades`. Given a dictionary with `str` keys and `list[int]` values, `average_grades` should return a new dictionary of type `dict[str, float]` that maps each student to their average.  
Example: `average_grades({ ‘Bill’:[75, 94, 97] , ‘Annie’:[88, 93, 99] })` returns `{ ‘Bill’:88.67 , ‘Annie’:93.33 }`.


# Solutions

## Conceptual Questions

1. False
2. True
3. False
4. True
5. True
6. False
7. True
8. False
9. False
10. True

## Memory Diagrams

11. ![](/static/practice_worksheets/fa21/qz03-solution11.png)  
11.1 The `scan` function takes in a dictionary and returns a list of the names of people that are 21 and older.

12. ![](/static/practice_worksheets/fa21/qz03-solution12.png)

## Function Writing

13. ![](/static/practice_worksheets/fa21/qz03-solution13.png)

14. ![](/static/practice_worksheets/fa21/qz03-solution14.png)