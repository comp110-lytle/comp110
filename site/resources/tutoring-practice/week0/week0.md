---
title: Week 0 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts on these Questions

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the second week (1.22 and Memory Diagrams).

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

## Objects and Data Types
1. There is a built-in function in Python to help you learn the type classification of an object. Could you write one line code using that function to check the data type of
`1 >>> 110 # What is the data type of this?`
`2 >>> “110” # What about this one?`

2. Try to evaluate the resulting data type of the following expression (might lead to error):
`>>> int(“20”)`
`>>> str(20)`
`>>> int(“twenty”)`
`>>> int(2.0) + 4 / int(“2”)`
`>>> int(2.0) + 4 / int(“2.0”)`

3. In Python, will the following two expressions result in the same value?
`>>> 1 + 2 * 3`
`>>> (1 + 2) * 3`

4. What is the name of the data type of the following values?
`>>> 0.25`
`>>> 10.0 / 3.0`
(For Elaboration): If you are interested in why, it is called that name, feel free to read the materials under the “Primitive Data Types” section from Lecture Notes of CL01

5. Will you be able to evaluate the output of the following codes relating to the string?
`1 >>> "str!"[0]`
`2 >>> "str!"[1]`
(For Elaboration): Think about how we can find the last item of the given string using an index. There are two methods to achieve this.

6. (True or false): `str` literals in Python can be surrounded in either single-quote characters or double-quote characters.

7. Are all of the following values considered Booleans in Python?
`>>> false`
`>>>TRUE`
`>>>True`

## Expressions

1. Do you think there is a difference between the Boolean value 'True' and the string ' "True" '?

2. When we are dealing with a mathematical expression in Python, what is the order that we are following? (Left-to-right rule or algebraic precedence rules?)

3. Be sure that you are familiar with the numerical operators in Python and trying to evaluate the following expressions:
`>>> 4 / 2`
`>>> 4.0 / 2.0`
`>>> 2 ** 3`
`>>> 5 % 5`
`>>> 5 // 2`
`>>> 5.0 // 2.0`
`>>> 2 + 4 / 2 * 2`
`>>> 2 + 5 // 2 * 2`

4. Consider the following 4 lines of codes:
`1 >>> x = 110`
`2 >>> y = 110`
`3 >>> x == y`
`4 >>> x = y`
For the above codes, is there any difference between line 3 and line 4? If so, can you tell the difference between them?

5. (Continue on Q3): Now, can you write codes which can 
- 1st: assign the value of x to y
- 2nd: check if y is NOT equal to x

6. Try to evaluate the following two expressions:
`>>> 220 >= int ((“1”+”1”+”0”) * 2)`
`>>> 110 >= int ((“1”+”0”+”0”) + “10”)`

7. Using subscription notation and concatenation, write an expression that evaluates to “Cs” using the following string: “Computer Scientists”.

8. Consider the following codes:
`1 >>> msg: str = "hello, world"`
`2 >>> msg.startswith("hello")` 
`3 >>> True`
With the above codes, will you be able to match the following terms to its referring 
part?
a. function call                
b. function name 
c. arguments                     
d. resulting value

## Variables and User Input
1. Is the following lines of code legal? If not, do you know why and how to modify it?
`1 >>> x: int = input("Give me a number")`
`2 >>> print(3 + 5 * input("Give me the multiplier"))`
`3 >>> print("Welcome back" + input("What is your name?"))`

2. Try to fill the following blank (They should be type declaration or type casting functions):
`x: ____ = input("What is your name")`
`print(3.0 + ____(input("Give me a number")))`
`x: ____ = "str" == input("COMP 110")`
`y: ____ = 110 == int(input("110"))`

## Conditionals
1. What is the output of the following codes?
~~~
x = 10
y = 5
if x > 5:
    if y > 0:
        print("A")
    else:
        print("B")
else:
    print("C")
~~~

2. (Continue on Question 1:) Can you change the value of x or y so that the final output can be A? What about B?

3. What is the output of the following codes?
~~~
a = True
b = False
c = True
if a and b or c:
    print("X")
else:
    print("Y")
~~~

4. (Continue on Question 3:) Change which one of a, b or c can let the codes in Q3 print another output? 


# Solutions

## Objects and Data Types
1. Use the built-in functions: type()

2. Try to evaluate the resulting data type of the following expression (might lead to error):
2.1 int
2.2 str
2.3 Error
2.4 int
2.5 Error

3. No, Python is following the same order of operations as common Maths

4. What is the name of the data type of the following values?
4.1 float
4.1 float

5. Will you be able to evaluate the output of the following codes relating to the string?
5.1 "s"
5.1 "t"
5.3 Method 1: "str"[-1] -- Last character has an index of -1
    Method 2: "str"[len("str")-1]

6. True


7. Are all of the following values considered Booleans in Python?
Only the last one is valid.

## Expressions

1. Yes, there data type are different. Even if we write conditional statement using them, the behind logic is also different.

2. Algebraic precedence rules

3. Be sure that you are familiar with the numerical operators in Python and trying to evaluate the following expressions:
3.1 2.0 float
3.2 2.0 float
3.3 8 int
3.4 0 int
3.5 2 int
3.6 2.0 float
3.7 6 int 
3.8 6 int

4. Consider the following 4 lines of codes:
`1 >>> x = 110`
`2 >>> y = 110`
`3 >>> x == y`
`4 >>> x = y`
Line 3 is a comparison whereas the line 4 is an assignment.

5. (Continue on Q3): Now, can you write codes which can 
- 1st: assign the value of x to y
~~~
>>> y = x
~~~
- 2nd: check if y is NOT equal to x
~~~
>>> print(y!= x)
~~~
6. Try to evaluate the following two expressions:
6.1 False
6.2 False

7. Using subscription notation and concatenation, write an expression that evaluates to “Cs” using the following string: “Computer Scientists”.
~~~
print("Computer Scientists"[0] + "Computer Scientists"[-1])
~~~


## Variables and User Input
1. Is the following lines of code legal? If not, do you know why and how to modify it?
`1 >>> x: int = input("Give me a number")`
Illegal
`2 >>> print(3 + 5 * input("Give me the multiplier"))`
Illegal
`3 >>> print("Welcome back" + input("What is your name?"))`
Legal

2. Try to fill the following blank (They should be type declaration or type casting functions):
`x: ____ = input("What is your name")`
str
`print(3.0 + ____(input("Give me a number")))`
float
`x: ____ = "str" == input("COMP 110")`
str
`y: ____ = 110 == int(input("110"))`
int







