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
1. There are two essential components of a recursive function, what are them (Hint: Phrase that ends with `case`)?

2. (Continue on Q1) Explain the importance of each of these two cases.

3. Is there a maximum recursion depth in Python by default? If so, do you know the reason for this limitation?

4. Can we write every loop using recursion? Why or why not?

5. (Continue on Q4) Think of the benefits of `loop` vs. `recursion` when do we prefer one over the other?

6. Think of the memory usage. Why might recursion lead to higher memory consumption compared to using `loops` for the same problem?

<br>

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
A) It runs indefinitely and lead to runtime error.
B) It throws an error before the code executed.
C) It executes the recursive case repeatedly.
D) It returns None.


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

<br>

##### Function Writing
1.  Write a recursive function in Python that calculates the sum of the first `n` negative integers.

2. Convert the following simple while loop to recursive function:
~~~
def print_numbers_while(n):
    i = 1
    while i <= n:
        print(i)
        i += 1
~~~

3. Convert the following simple recursive function to while loop
~~~
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
~~~
<br>

# Solutions

### Conceptual:
1. The two essential components of a recursive function are the `base case` and the `recursive case`.

2. The `base case` serves as the termination condition that stops the recursion from continuing indefinitely and eventually lead to stack overflow erro. The `recursive case` is where the function calls itself with different arguments, moving towards the base case.

3. Yes, there is a maximum recursion depth in Python by default, which is `typically set to 1000`. This limit is in place to prevent a stack overflow error.

4. Therodically, coversion between these two are possible. However, in the real life scenario, due to the overhead associated with recursive calls and the call stack limit, it is not practical to do this kind of conversion effectively everytime.

5. We prefer `recursion` over loops when the problem can be naturally expressed as smaller instances of the same problem, such as with factorial calculation, or the Fibonacci sequence. `Loops`, on the other hand, are more straightforward and therefore can be more friendly to use when dealing with complicated questions.

6. Since each recursive call adds a new layer to the call stack. Think of the `Memory Diagram`, you would create new function call frame in the stack for each recursive step.

### Multiple Choices:
1. B) A programming technique where a function calls itself to solve a problem.

2. B) Base case

3. A) It runs indefinitely and leads to runtime error.

4. B) Computes the product of integers from 1 to n.

5. A) n == 0

6. For the sum of digits in 12345, the printed result would be 15.

7. B) The recursive call is incorrect. The function should call factorial(n - 1) in the recursive case, not factorial(n), to ensure it makes progress toward the base case and avoids infinite recursion.

8. D) There is no bug; the function is correct.

### Function Writing
1. 
~~~
def sum_negative_integers(n):
    if n == 0:
        return 0
    else:
        return -n + sum_negative_integers(n - 1)
~~~

2. 
~~~
def print_numbers_recursive(n, i=1):
    if i <= n:
        print(i)
        print_numbers_recursive(n, i + 1)
~~~

3.
~~~
def factorial_iterative(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
~~~