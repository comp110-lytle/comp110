---
title: Local Variables 
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Questions


1. Which of the following properly *declares* a variable?

    a. `"Michael Jordan" = name`

    b. `large_number = 2 ** 2025`

    c. `name: str = "Michael Jordan"`

    d. `int: large_number = 2 ** 2025`

2. Which of the following properly *updates* or *assigns* a value to a variable (if it has already been declared)?

    a. `"Michael Jordan" = name`

    b. `large_number = 2 ** 2025`

    c. `name: str = "Michael Jordan"`

    d. `int: large_number = 2 ** 2025`

3. Refer to the following code snippet to answer this question. Describe what will happen if we run this code. Feel free to create a memory diagram to assist you.

```py
1     def foo(num: int) -> None:
2         """Fooey."""
3         x: int = num * -1
4         print(x)
5 
6     def main() -> None:
7         """The main function."""
8         foo(4)
9         print(x)
10
11    main()
```
<details>
<summary>SHOW SOLUTIONS</summary>

1. c: `name: str = "Michael Jordan"` The important part to notice is that we are giving it a type, which we only do during declaration.

2. b. `large_number = 2 ** 2025` Updating or assigning a value to a variable that has already been declared just uses the equal sign with the variable name on the left and the value on the right, and does not redeclare the type.

3. When this code is run, you will first enter the `main` function since it is called on line 11, then you will enter the `foo` function when it is called on line 8. Then the `foo` function will declare a local variable `x` and print it, outputting `-4`. Then we will return to line 8, then move on to line 9 where we attempt to print `x`. However, `x` was a local variable only in the `foo` frame, not in the `main` frame, so we will get a `NameError`.

</details>

&nbsp;
