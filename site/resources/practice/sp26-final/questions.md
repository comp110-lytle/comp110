---
title: Practice Problems
author:
- Alyssa Lytle
- Team 110
page: lessons
template: overview
---


## Functions


A function's *return value* is whatever it evaluates to when called. If no explicit `return` is written, the function returns:
a) `0`
b) `""`
c) `None`
d) `False`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) `None`
</details>

In the signature `def add(x: int, y: int) -> int:`, the `-> int` specifies:
a) the types of the parameters
b) the type of the return value
c) a default value
d) a type error
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) the type of the return value
</details>

Parameters are the names in the function's definition. Arguments are the values passed in at the call site.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
a) True
</details>

When a function is called, Python creates a new ____ on the call stack to hold its local variables.
a) heap
b) frame
c) object
d) module
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) frame
</details>

Local variables declared inside a function are accessible from outside the function after it finishes.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) False
</details>

A function that only prints a value but does not return it will, when called in an expression, evaluate to:
a) the printed string
b) `None`
c) `0`
d) a `SyntaxError`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) `None`
</details>

The line that declares a function's name, parameters, and return type is called the function's:
a) body
b) docstring
c) signature
d) prototype
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) signature
</details>

## Scope


A variable defined at the top level of a `.py` file (outside any function) is said to be in:
a) local scope
b) global scope
c) nested scope
d) method scope
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) global scope
</details>

Two functions can each define a local variable named `x` without conflict.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
True
</details>

## Conditionals + Recursion


An `if` statement's body will execute exactly once if its condition is `True`.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
True
</details>

In a recursive function, the `________` case is the non-recursive stopping condition that halts the recursion.
a) terminal
b) base
c) final
d) recursive
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) base
</details>

Which of the following is NOT required for a correct recursive function?
a) A base case
b) A recursive case that makes progress toward the base case
c) A `while` loop inside the function body
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) A `while` loop inside the function body
</details>

A recursive function's recursive case typically calls:
a) A different function
b) Itself with the same arguments
c) Itself with arguments that are closer to the base case
d) `print()` and then itself
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) Itself with arguments that are closer to the base case
</details>

In an `if`/`else` block, the `else` branch runs when the `if` condition evaluates to:
a) `True`
b) `False`
c) `None`
d) Any non-`bool` value
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`False`
</details>

## While Loops


A `while` loop whose condition is always `True` and whose body never breaks out will:
a) raise a `SyntaxError`
b) run forever (infinite loop)
c) run once
d) skip its body entirely
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) run forever (infinite loop)
</details>

A `while` loop first evaluates its condition:
a) after each full iteration only
b) before every iteration (including the first)
c) only once at the start
d) only once at the end
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) before every iteration (including the first)
</details>

Combining a counter variable with a `while` loop lets you simulate a count-controlled loop to iterate over a data structure.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
a) True
</details>

Which of the following is most likely to cause an infinite loop?
a) A `while` whose condition is always `False`
b) A `while` whose body never changes the variables used in its condition
c) A `while` inside a function
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) A `while` whose body never changes the variables used in its condition
</details>

## Lists


Which of the following correctly declares `nums` as a list of integers?
a) `nums: list = [1, 2, 3]`
b) `nums: int[list] = [1, 2, 3]`
c) `nums: list[int] = [1, 2, 3]`
d) `nums: [int] = [1, 2, 3]`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) `nums: list[int] = [1, 2, 3]`
</details>

What does `my_list.append(x)` return?
a) the modified list
b) the length of the list
c) `None`
d) `x`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`None`
</details>

Two variables assigned to the same list literal (`a = [1, 2]`\n`b = [1, 2]`) refer to the same underlying list object in memory.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
False
</details>

## Dictionaries


You can use any immutable type (like `int`, `str`, or `tuple`) as a dictionary key.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
a) True
</details>

You can use `list`s as a value in a dictionary.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
a) True
</details>

You can use `list`s as a key in a dictionary.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) False
</details>

Given `d: dict[str, int] = {"a": 1, "b": 2}`, what does `len(d)` return?
a) `1`
b) `2`
c) `4`
d) `Error`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`2`
</details>

The `in` operator on a dictionary checks for membership of:
a) values
b) keys
c) key-value pairs
d) both keys and values
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) keys
</details>

## OOP


Two different instances of the same class always share the same attribute values.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) False
</details>

Which keyword is used to define a new class in Python?
a) `define`
b) `class`
c) `object`
d) `new`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`class`
</details>

When you write `floof: Cat = Cat("Fluffy")`, Python internally calls which method first?
a) `__str__`
b) `__new__`
c) `__init__`
d) `__class__`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) `__init__`
</details>

It is legal to assign a new attribute to an existing instance outside of `__init__` (e.g., `my_cat.color = "black"` after construction).
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
True
</details>

Constructors must take at least one parameter other than the self parameter
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) False
</details>

An instance's `__init__` method is typically responsible for initializing the instance's attributes
a)  True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
True
</details>

## Magic Methods


`[] == list()` evaluates to:
a) `True`
b) `False`
c) `None`
d) `Error`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`True`
</details>

`__str__` is called implicitly by which built-in functions?
a) `len`
b) `str`
c) `print`
d) `id`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
`str` and `print`
</details>

Magic methods are normally called *implicitly* by Python in response to syntax like `+`, `==`, `len(...)`, or `print(...)` rather than by explicit name.
a) True
b) False
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
True
</details>

## Runtime


A linear search through an unsorted list of length $n$ has what worst-case runtime?
a) $O(1)$
b) $O(\log n)$
c) $O(n)$
d) $O(n^2)$
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) $O(n)$
</details>

A nested `for` loop where both loops run $n$ times yields which runtime?
a) $O(n)$
b) $O(n \log n)$
c) $O(n^2)$
d) $O(2^n)$
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) $O(n^2)$
</details>

Big-O notation describes how runtime grows as input size $n$:
a) decreases
b) stays fixed
c) grows very large
d) changes by constant factor
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) grows very large
</details>

## Unit Tests


A pytest test function must be defined starting with the prefix:
a) `check_`
b) `verify_`
c) `test_`
d) `pytest_`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
c) `test_`
</details>

`assert x == y` will raise an `AssertionError` when:
a) `x == y` is `True`
b) `x == y` is `False`
c) `x is y` is `True`
d) `x` is `None`
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
b) `x == y` is `False`
</details>

Running `pytest` in a directory discovers tests by looking at:
a) files and functions whose names begin with `test_`
b) every `.py` file in the folder
c) only files ending in `_tests.py`
d) the contents of a `tests.json` manifest
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
a) files and functions whose names begin with `test_`
</details>
