---
title: Recursion 
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Questions

## Conceptual

1. Which of the following are required in a recursive function that does not infinitely recur?

    a. A base case without a recursive function call

    b. Recursive case that progresses toward the base case

    c. Arguments changing in the recursive case

    d. All of the above

<details>
<summary>SHOW SOLUTIONS</summary>

1. d. All of the above

</details>

&nbsp;

## Code Writing

1. Write a recursive function named `sum` that has an `int` parameter `number` and returns an `int` that is the sum of all nonnegative integers up to and *including* `number` (`1 + 2 + ... + number`). For example, `sum(number=4)` should evaluate to `1 + 2 + 3 + 4 = 10`. If a negative argument for `number` is given, just return `-1` (What case is this?). It may help to come up with your base case and recursive case before beginning to write any code.

<details>
<summary>SHOW SOLUTIONS</summary>
1. The negative argument case is an edge case. Note: There are many equivalent ways this function could be written.

```py
1    def sum(number: int) -> int:
2        """Sum of all nonnegative integers up to and including number."""
3        if number < 0: # Edge case
4            return -1
5        elif number > 0: # Recursive case
6            return number + sum(number=number - 1)
7        else: # Base case
8            return 0
```

</details>

&nbsp;
