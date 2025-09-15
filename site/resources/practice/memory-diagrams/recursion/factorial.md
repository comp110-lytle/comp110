---
title: Practice Memory Diagram
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Snippet

Create a memory diagram for the following code snippet. Additionally, identify the lines where the edge case, base case, and recursive case occur (this will generally consist of a conditional statement, a return statement, and possibly more lines of code in between).


```py
1     """Recursion practice!"""
2 
3     def factorial(num: int) -> int:
4         """Calculate the factorial of num."""
5         if num <= 0:
6             return 1
7         elif num == 1:
8             return 1
9         else:
10            return num * factorial(num=num - 1)
11
12    def main() -> None:
13        """The main function."""
14        print(factorial(num=3))
15
16    main()
```

# Solution

The edge case occurs on lines 5-6, the base case occurs on lines 7-8, and the recursive case on lines 9-10.

<img class="img-fluid" src="/static/practice-mem-diagrams/factorial.png" alt="Memory diagram for factorial and main function code listing."  />

## Image Description 
*(Coming Soon)*
