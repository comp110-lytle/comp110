---
title: Week 2 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the second week (1.22 and Memory Diagrams).

<br>

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

### Unicode, Emoji
1. We can also compare characters or even strings in Python, and try to figure out which side is greater among the following pairs"
1.1 `"cs" and "CS"`

1.2 `"comp" and "stor"`

1.3 `(One Uppercase letter) and (One Lowercase Letter)`

1.4 `"z" and "A"`

<br>

### String Escape Sequences
1. Can you write a "print()" statement that will have the output as `The computer said, "The course 'COMP 110' is a very good introduction course.`

2. For the following codes:
~~~
name = "John"
age = 25
print(f"\"{name}\" is {age} years old.")
~~~
Can you explain the purpose of the backslashes and what would the output be?

3. What is the output of `print("Hello\\World!")`? Is it the right code to make `Hello` and `World!` in two separate lines? If not, what is the right one?

<br>

### f-string
1. Rewrite this code using f-string print("I am in COMP" + str(course) + " right now!")`

2. With variable `x = 5` and variable `y = 10`, write the `print()`code that can have the output as `x + y = 15`. Please use `f-string` here.

<br>

### Memory Diagram
1. What are the two main areas of a Memory Diagram (not considering the "output" here.)

2. In the `stack` area, how do we specify that certain values are `str` type?

3. Based on what we have learned, we will write something in the `output` area usually after we see which function call.

## Solutions

### Unicode, Emoji
1. We can also compare characters or even strings in Python, and try to figure out which side is greater among the following pairs
1.1 `"cs" > "CS"`

1.2 `"comp" < "stor"`

1.3 `(One Uppercase letter) < (One Lowercase Letter)`

1.4 `"z" > "A"`


### String Escape Sequences
1. Can you write a "print()" statement that will have the output as `The computer said, "The course 'COMP 110' is a very good introduction course.`
~~~
print('The computer said, "The course \'COMP 110\' is a very good introduction course.')
~~~

2. For the following codes:
~~~
name = "John"
age = 25
print(f"\"{name}\" is {age} years old.")
~~~
Can you explain the purpose of the backslashes and what would the output be?

The backslashes (\) in the provided f-string are used as escape characters to include double quotes (") within the output string, instead of being considered as the end of the string.

3. What is the output of `print("Hello\\World!")`? Is it the right code to make `Hello` and `World!` in two separate lines? If not, what is the right one?
- Output: Hello\World!
- print("Hello\nWorld!") 


### f-string
1. Rewrite this code using f-string print("I am in COMP" + str(course) + " right now!")`
~~~
course = 110
print(f"I am in COMP{course} right now!")
~~~

2. With variable `x = 5` and variable `y = 10`, write the `print()`code that can have the output as `x + y = 15`. Please use `f-string` here.
~~~
x = 5
y = 10
print(f"{x} + {y} = {x + y}")
~~~

### Memory Diagram
1. What are the two main areas of a Memory Diagram (not considering the "output" here.)
Stack and Heap

2. In the `stack` area, how do we specify that certain values are `str` type?
Using double quotes as what we did when writing codes.

3. Based on what we have learned, we will write something in the `output` area usually after we see which function call.
print() function

