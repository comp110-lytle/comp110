---
title: Practice Memory Diagram
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Snippet

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


<img class="img-fluid" src="/static/practice-mem-diagrams/factorial.png" alt="Memory diagram for factorial and main function code listing."  />

## Image Description 
*(Coming Soon)*
