---
title: Recursive Functions
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

Recursion is not a difficult topic. It is simply the process of a function calling itself during its own execution to obtain a new value that will be used in the previous call. This concept is straightforward because we are already familiar with how to call functions and visualize function calls using diagrams.

The hard part is determining what to include in your function call and identifying the exact recursive step. How quickly you can do this depends on practice and the ability to spot patterns. 

For example, why can adults add numbers much faster than children who are just learning to count? It’s because adults have practiced recognizing patterns in numbers over years of experience. They’ve internalized shortcuts, like instantly knowing that 7 + 3 equals 10 without counting each number individually. 

Similarly, mastering recursion involves recognizing the structure of problems that can be broken down into smaller, self-similar subproblems and applying the recursive step effectively. All of you are capable of writing recursive functions once you are able identify the base case and recursive step and understand the algorithm! 

The problems below might initially seem challenging because recursion introduces a new way of thinking about pattern recognition. Hopefully, by the end of this problem set, you'll feel more confident and quicker at identifying the recursive step.

# Questions

1. Write a function, `factorial`, that will calculate the factorial of an input number. *We are aware we did this in class but lets see if you can do it on your own and are able to think through this without referring to any notes.* If you do not know what a factorial is, google it. [Solution](#question1)

2. Write a function, `sum_of_natural_numbers`, that given an input number, `n`, it will sum of the first `n` natural numbers. Below is an example usage of this function. [Solution](#question2)

<pre>
<div class="terminal">
>>> from test import sum_of_natural_numbers
>>> sum_of_natural_numbers(5)
15
>>> sum_of_natural_numbers(0) 
0
</div>
</pre>

3. Write a function, `sum_of_digits`, that will return the sum of digits of a number passed to the function. Below is an example usage of this function. [Solution](#question3)

<pre>
<div class="terminal">
>>> from test import sum_of_digits
>>> sum_of_digits(123)
6
>>> sum_of_digits(9876)
30
</div>
</pre>

4. Write a function, `power`, that will return the power of a number to some value passed. Below is an example usage of this function. [Solution](#question4)

<pre>
<div class="terminal">
>>> from test import power
>>> power(2, 3)
8
>>> power(5, 0)
1
>>> power(3, 4)
81
</div>
</pre>

5. Write a function, `gcd`, that will calculate the Greatest Common Divisor (GCD) (this will come in handy if you continue on in the major and chose to take Comp 283 or Math 381). Here is a [video](https://youtu.be/JUzYl1TYMcU?si=C0forteoqnqLT_nw) that will help you understand the algorithm that you need to implement. Below is an example usage of this function. [Solution](#question5)

<pre>
<div class="terminal">
>>> from test import gcd
>>> gcd(48, 18)
6
>>> gcd(56, 98)
14
</div>
</pre>

6. Write a function, `reverse_string`, that takes a string `s` as input and returns a new string that is the reverse of `s`. Below is an example usage of this function. [Solution](#question6)

<pre>
<div class="terminal">
>>> reverse_string("hello")
'olleh'
>>> reverse_string("a")
'a'
>>> reverse_string("")
''
</div>
</pre>

*Hint:* To solve the problem of reversing a string using recursion, you will need a helper function to manage the recursion properly. The reverse_string function can be responsible for starting the process, while the helper function will do the actual recursive work. 

The key reason we need the helper function is that recursion requires some form of state to be passed along with each recursive call. In this case, we need to keep track of the index we are working on as we move through the string. The reverse_string function, by itself, doesn’t have an easy way to track this index, so we use a helper function to handle that.

- `reverse_string`: This function is the starting point. It simply calls the helper function and passes the string along with the starting index (which is the last character of the string). The helper function should be called passing the last index of the input string as the index to be used in the helper function.
- `reverse_helper`: This function is responsible for the actual recursion. It keeps track of the current character by using the index parameter, and it reduces the index with each recursive call, effectively moving from the end of the string towards the beginning.

Here is a skeleton code if you are still stuck: 

```python
def reverse_string(s: str) -> str:
    return reverse_helper(s=?, index=?) # finish the function call

def reverse_helper(s: str, index: int) -> str:
    # your code here 

# Testing the function
print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string(""))
```

7. Write a function, `fibonacci`, that computes the n-th number in the Fibonacci sequence, where n is a number passed to the function. Here is a [video](https://youtu.be/pgWBbkqiUwQ?si=Dy7q72l2FuNDuCmc) that will help you understand the algorithm that you need to implement. Below is an example usage of this function. [Solution](#question7)

<pre>
<div class="terminal">
>>> fibonacci(5)
5
>>> fibonacci(0)
0
>>> fibonacci(6)
8
</div>
</pre>

<!-- 8. Write a function, `factorial_list`, that takes a list of non-negative integers and returns a new list where each element is the factorial of the corresponding element in the input list. Below is an example usage of this function. [Solution](#question8)

<pre>
<div class="terminal">
>>> my_list = [3, 4, 5]
>>> factorial_list(my_list)
[6, 24, 120]
</div>
</pre>

# Challenge Problems 
*You are fully capable of completing these*

It doesn't matter how long it takes you; thinking through these problems is far more important than getting the answer quickly. The process of problem-solving and truly understanding the concepts is more valuable than rushing to find the correct solution.

It’s incredibly rewarding to spend a couple of days wrestling with a problem that seems unsolvable, only to finally figure it out after persistent effort. This is far more fulfilling than simply looking at the answer after only a couple of attempts. If you need hints, that's completely okay. If you need to watch a video, that's okay too. What matters most is that you're putting in the effort to understand these problems. This effort is far more valuable than completing them quickly without fully grasping the concepts.

1. Write a recursive function `fibonacci_sequence` that generates the Fibonacci sequence starting from 0 and 1, and appends the next Fibonacci number to the list until it exceeds a given value up_to. 

The function should take two arguments:
- `up_to` (int): The value that the sequence should not exceed.
- `fib_list` (list[int]): A list that holds the Fibonacci numbers generated so far

The function should compute and return the Fibonacci sequence up to but not exceeding the up_to value. [Solution](#cquestion1)

<pre>
<div class="terminal">
>>> result = fibonacci_sequence(9, [0, 1])
>>> print(result)
[0, 1, 1, 2, 3, 5, 8]
</div>
</pre>

2. Implement a recursive binary search function, `binary_search`, to find if a target number exists in a sorted list of integers. Binary search works by repeatedly dividing the search interval in half and checking if the middle element matches the target, or if the target is smaller or larger than the middle element.

Write a function `binary_search` that takes:

- `arr` (list[int]): A sorted list of integers.
- `target` (int): The number to search for.
- `low` (int): The starting index of the current search range.
- `high` (int): The ending index of the current search range.

The function should return:

- The index of the target if it is found.
- -1 if the target is not found in the list.

The recursive approach should:
- Check if the middle element equals the target.
- If the target is smaller than the middle element, search the left half.
- If the target is larger than the middle element, search the right half.
- If the list is empty (when low exceeds high), return -1

[Solution](#cquestion2)

<pre>
<div class="terminal">
>>> arr = [1, 3, 5, 7, 9, 11]
>>> print(binary_search(arr, 7, 0, len(arr) - 1))
3
>>> print(binary_search(arr, 4, 0, len(arr) - 1))
-1
</div>
</pre> -->

# Solutions 

## Questions

##### 1. Code below: {#question1}

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
print(factorial(0))  # Output: 1 (base case)
```

##### 2. Code below: {#question2}

```python
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)

print(sum_of_natural_numbers(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)
print(sum_of_natural_numbers(0))  # Output: 0 (base case)
```

##### 3. Code below: {#question3}

```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_of_digits(9876)) # Output: 30 (9 + 8 + 7 + 6)
```

##### 4. Code below: {#question4}

```python
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 3))  # Output: 8 (2 * 2 * 2)
print(power(5, 0))  # Output: 1 (base case)
print(power(3, 4))  # Output: 81 (3 * 3 * 3 * 3)
```

##### 5. Code below: {#question5}

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
```

##### 6. Code below: {#question6}

```python
def reverse_string(s):
    return reverse_helper(s, len(s) - 1)

def reverse_helper(s, index):
    if index < 0:
        return ""
    return s[index] + reverse_helper(s, index - 1)

# Testing the function
print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string(""))
```

##### 7. Code below: {#question7}

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5 (0, 1, 1, 2, 3, 5)
print(fibonacci(0))  # Output: 0 (base case)
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)
```
<!-- 
##### 8. Code below: {#question8}

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_list(my_list):
    result = []
    for num in my_list:
        result.append(factorial(num))
    return result

# Example usage:
my_list = [3, 4, 5]
print(factorial_list(my_list))  # Output: [6, 24, 120]
```

## Challenge Questions 
##### 1. Code below: {#cquestion1}

```python
def fibonacci_sequence(up_to, fib_list):
    if len(fib_list) < 2:
        fib_list = [0, 1]
    next_value = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
    if next_value > up_to:
        return fib_list
    fib_list.append(next_value)
    return fibonacci_sequence(up_to, fib_list)

# To use the function:
result = fibonacci_sequence(9, [0, 1])
print(result)  # Output: [0, 1, 1, 2, 3, 5, 8]
```

##### 2. Code below: {#cquestion2}

```python
def binary_search(arr, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    return -1

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7, 0, len(arr) - 1))  # Output: 3 (index of 7)
print(binary_search(arr, 4, 0, len(arr) - 1))  # Output: -1 (not found)
``` -->