---
title: Quiz 00 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Concepts on Quiz 0

Quiz 0 will cover the following concepts:

* Syllabus and course policies - be familiar with them!
* Lessons 0 through 8 - with a **heavy emphasis on Lessons 4 - 8**

# Questions

The quiz itself will be similar in difficulty but longer in length than these practice questions. In addition to these questions, you should review all of your lesson responses on Gradescope. The kinds of questions you responded to on Gradescope will also be 

Solutions for each problem can be found at the bottom of this page.

## Memory Diagrams
1.	Produce a memory diagram for the following code snippet, being sure to include its stack and output.

![](/static/practice_worksheets/fa21/qz0-question13.png)

2. Produce a memory diagram for the following code snippet, being sure to include its stack and output.

![](/static/practice_worksheets/fa21/qz00-question14.png)

## Data Types
3. `str` literals in Python can be surrounded in either single-quote characters or double-quote characters, though in COMP110 we prefer the latter. (T/F)
4. `TRUE` and `FALSE` are valid bool values in Python. (T/F)
5. An `int` literal can begin with a zero, but cannot end with a zero. (T/F)
6. What function can we use to identify the type classification of any object in Python? 
7. What is the resulting data type of the following expression? `int("20")`

## Expressions
8.	What is the evaluation of the following expression?
` type(9 / len( str(110)) `
9. What is the result of the following expression? `"440" + "20"`
10. What value of x would cause the following expression to evaluate to `True`?
` (3 + x) == (55 % 2 ** 4) `
11. What value does the following expression result in, and what is its type? `2 + 2 / 2 ** (2 * 0)`
12.	Using subscription syntax and concatenation, write an expression that evaluates to `"tar"` using the following string: `“the brown, lazy dog!"`.
13.  What data type do expressions with relational operators evaluate to?
14.  What does the following expression evaluate to? `int("10" + "40") > 100 * 2`

# Solutions

## Memory Diagrams

1. ![](/static/practice_worksheets/fa21/qz0-solution13.png)
2. ![](/static/practice_worksheets/fa21/qz0-solution14.png)

## Data Types
3. T
4. F
5. F
6. `type()`
7. int
   
## Expressions
8. `<class 'float'>`
9. "44020"
10. 4
11. 4.0
12. “the brown, lazy dog!”[0] + “the brown, lazy dog!"[12] + “the brown, lazy dog!"[5]
13. bool
14. True
