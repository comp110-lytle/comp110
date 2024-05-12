---
title: Quiz 00 Practice
author:
- Megan Zhang
- David Karash
- Catherine Roberts
page: lessons
template: overview
---

# Concepts on Quiz 0

Quiz 0 will cover the following concepts:

* Syllabus and course policies - be familiar with them!
* Lessons (LS) 00 through 05
* Challenge Questions (CQ) 00 and 01

# Questions

The quiz itself will be similar in difficulty but longer in length than these practice questions. In addition to these questions, you should review all of your lesson responses on Gradescope. The kinds of questions you responded to on Gradescope will also be on the quiz. 

Solutions for each problem can be found at the bottom of this page. (But if you're unsure, before looking up the solution, try it out in Visual Studio!)

## Memory Diagrams
1.	Produce a memory diagram for the following code snippet, being sure to include its stack and output.

![](/static/practice_worksheets/fa21/qz0-question13.png)

2. Produce a memory diagram for the following code snippet, being sure to include its stack and output.

![](/static/practice_worksheets/fa21/qz00-question14.png)

## Data Types
3. `str` literals in Python can be surrounded in either single-quote characters (`'like this'`) or double-quote characters (`"like this"`), though in COMP110 we prefer the latter. (T/F)
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

## Conditionals
15. Every `if` statement must be followed by a paired `else` branch. (T/F)
16. Lines contained in an `else` branch in Python do not have to be indented. (T/F)
17. You can name a variable `else` in your program without Python confusing your variable's name and the `else` keyword. (If you are unsure, this is a good one to try yourself!) (T/F)
18. Given the following code snippet, what is the printed output with the specified values for `x` and `y`?  
![](/static/practice_worksheets/sp22/qz00-question18.png)  
18.1. When x = 3, y = 5?  
18.2. When x = 5, y = 3?  
18.3. When x = -5, y = 1?  
18.4. When x = 13, y = 8?  
18.5. When x = 4, y = 3?
19. Every _then_ or _else_ block of an `if-then` statement is reachable by some value, regardless of the test conditions specified by the `if` statement.

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

## Conditionals
15. False
16. False
17. False
18. 
18.1. 16.0  
18.2. 2.0  
18.3. -3.0  
18.4. 3.0  
18.5. 1
19. False