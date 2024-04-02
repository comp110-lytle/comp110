---
title: Week 11 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)
<br>

# Questions 

### Recursion
##### Conceptual:
1. There are two essential components of a recursive function, what are them?

2. (Continue on Q1) Among these two essential components, one of them is the most necessary one. Identify it.

3. Is there a maximum recursion depth in Python by default? If so, do you know the reason for this limitation?

4. Can we write every loop using recursion? Why or why not?

5. (Continue on Q4) Can we write every recusion using loop? Why or why not?

##### Multiple Choices:
1. What is recursion?
A) A loop construct in Python.
B) A programming technique where a function calls itself to solve a problem.
C) A data structure used for storing hierarchical data.
D) A type of sorting algorithm.

2. Which of the following components is essential for a recursive function?
A) Loop condition
B) Base case
C) Iteration
D) Break statement

3. What happens if a recursive function lacks a base case?
A) It runs indefinitely.
B) It throws an error.
C) It executes the recursive case repeatedly.
D) It returns None.
Answer: A) It runs indefinitely.

4. 
~~~
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
~~~
What is this recursive function trying to do?
A) Computes the sum of integers from 1 to n.
B) Computes the product of integers from 1 to n.
C) Computes the power of n.
D) Computes the Fibonacci sequence.

5. What is the base case for a recursive function that calculates the factorial of a positive integer n?
A) n == 0
B) n == 1
C) n <= 1
D) n > 1
Answer: A) n == 0

6. 
~~~
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_number = n // 10
        return last_digit + sum_of_digits(remaining_number)
~~~
What would be printed if we call `sum_of_digits(12345)`

7.
~~~
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n)
~~~
Is there any bug in the above code?
A) The base case is missing. 
B) The recursive call is incorrect. 
C) The function should return n instead of n * factorial(n). 
D) There is no bug; the function is correct.

8. 
~~~
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
~~~
Is there any bug in the above code?
A) The base case should be a == 0. 
B) The function should return b for the base case. 
C) The recursive call should be gcd(a, b) instead of gcd(b, a % b). 
D) There is no bug; the function is correct.

