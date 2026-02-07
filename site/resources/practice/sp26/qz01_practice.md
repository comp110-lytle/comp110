---
title: Quiz 01 General Practice
author:
- Alyssa Lytle
- Izzi Hinks
- Megan Zhang
- David Karash
- Viktorya Hunanyan
- Benjamin Eldridge
page: lessons
template: overview
---

# Quiz 01 Practice

## Boolean Expressions

1. What are the results of the following boolean expressions?

    1.1 `((not False) and True) == True`

    1.2 `(not False) or (True and False)`

    1.3 `True and (7 < 3 * 4 / 6)`

    1.4 `(not False) != True`

    1.5 `not (True and False) and (False or not False)`

    1.6. `"XYz" == "XYZ" or "B" == "C"`

    1.7. `5 ** 2 >= 5 * 5 and 110 % 10 == 0`

<details>
<summary>SHOW SOLUTIONS</summary>

1.1. `True`

1.2. `True`

1.3. `False`

1.4. `False`

1.5. `True`

1.6. `False`

1.7. `True`

</details>

&nbsp;

## Conditionals

### True/False

1. Every `if` statement must be followed by a paired `else` branch. (T/F)

2. For a conditional statement that involves `if`, `elif`, and `else` such as the one below, the statements under the `elif` and the `else` could both be executed under certain conditions when run once. (T/F)

```py
    if <condition>:
        <do something>
    elif <other condition>:
        <do a different thing>
    else:
        <do a third thing>
```

3. You can name a variable `else` in your program without Python confusing your variable's name and the `else` keyword. (If you are unsure, this is a good one to try yourself!) (T/F)

<details>
<summary>SHOW SOLUTIONS</summary>

1. `False`

2. `False`, for statements such as the example shown, only one of the indented lines of code under `if`, `elif`, or `else` will be executed.

3. `False`, and this is something to watch out for when naming variables in your exercises, as Python reserves many short words for special things like `and`, `else`, and `return` (and more that you will learn about!).

</details>

&nbsp;

### Conceptual

1. What does the condition of a conditional have to evaluate to in order to enter its then block?

2. What does the condition of a conditional have to evaluate to in order to enter its `else` block?

3. What happens when a return statement is encountered in the then block of an `if` statement?

<details>
<summary>SHOW SOLUTIONS</summary>

1. The condition must evaluate to `True`.

2. The condition must evaluate to `False`.

3. The return value is recorded in memory and the function is immediately exited. Any code after the conditional statement is not executed.

</details>

&nbsp;

### Code Snippet

```py
    def main() -> None: 
        x: str = "x"
        y: str = "y"
        z: str = x
        y = x
        x = "y"
  
        if not(x != y and x != "y"):
            print(f"x: {x}")
        else:
            print("'if' condition not met.")
  
    main()
```

1. What is the condition in this code?

2. What does the condition evaluate to? (This will be confusing to do in your head so try at least a partial memory diagram!)

3. What values would `x`, `y`, and/or `z` have to be assigned before the conditional statement in order for the `else` block to run (line 11)? Give at least one example, but also understand what would have to be true in general to make the `else` block run.

4. What other values can `x`, `y`, and/or `z` be assigned in order for the then block to run (line 9)? Similarly, give at least one example, but also understand what would have to be true in general to make the then block run.

<details>
<summary>SHOW SOLUTIONS</summary>

1. `not(x != y and x != "y")`

2. The condition evaluates to `True`.

3. To ensure the else block runs in the given code, the condition `x != y and x != "y"` must be true. This means `x` should be different from `y` and `x` should also be different from the string `"y"`. For example, setting `x = "a" and y = "b"` will satisfy this condition, making the else block execute.

4. To make the `if` block run, the condition `not(x != y and x != "y")` must be true, which happens when `x` is either the same as `y` or the same as `"y"`, or both. In the original code where `x = "y"`, `y = "x"`, and `z = "x"`, the `if` block runs as `not(x != y and x != "y")` evaluates to `True`.

</details>

&nbsp;

## f-strings

1. What are the printed outputs for the following `print` function calls?

    1.1. `print(f"{1 + 1}")`

    1.2. `print(f"C{'OM'}P {100 + 10}")`

    1.3. `print(f"This statement is {not (True or False)}!")`

    1.4. `print(f"Question: Is {55} even? Answer: {55 % 2 == 0}")`

<details>
<summary>SHOW SOLUTIONS</summary>

1.1. 2

1.2. COMP 110

1.3. This statement is False!

1.4. Question: Is 55 even? Answer: False

</details>

&nbsp;

## Local Variables

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
    def foo(num: int) -> None:
        """Fooey."""
        x: int = num * -1
        print(x)

    def main() -> None:
        """The main function."""
        foo(4)
        print(x)

    main()
```
<details>
<summary>SHOW SOLUTIONS</summary>

1. c: `name: str = "Michael Jordan"` The important part to notice is that we are giving it a type, which we only do during declaration.

2. b. `large_number = 2 ** 2025` Updating or assigning a value to a variable that has already been declared just uses the equal sign with the variable name on the left and the value on the right, and does not redeclare the type.

3. When this code is run, you will first enter the `main` function since it is called on line 11, then you will enter the `foo` function when it is called on line 8. Then the `foo` function will declare a local variable `x` and print it, outputting `-4`. Then we will return to line 8, then move on to line 9 where we attempt to print `x`. However, `x` was a local variable only in the `foo` frame, not in the `main` frame, so we will get a `NameError`.

</details>

## Positional vs. Keyword Arguments

1. (True or False) You can only use keyword arguments if the function has multiple parameters.

2. For the following code snippet, rewrite each of the function call expressions with arguments to use the other style of declaring arguments, that is if a function call is made with keyword arguments, rewrite it with positional arguments and vice-versa. The code should still run the same once rewritten.

```py
    def foo(x: int, y: int) -> int:
        """Number stuff."""
        if x < y:
            return y - x
        else:
            return x - y

    def bar(word: str) -> str:
        """Word doubler."""
        return word + word

    def main() -> None:
        """The main function."""
        number: int = foo(x = 4, y = 5)
        other_num: int = foo(-4, -5)
        # Make sure to rewrite both the inner and outer function call expressions below
        doubled: str = bar(word = str(foo(46, 2)))

    main()
```

<details>
<summary>SHOW SOLUTIONS</summary>

1. False, you can use keyword arguments even if there is just one parameter. It is just more common to use positional arguments in that case for brevity.

2. Refer to the rewritten code snippet below:

```py
    def foo(x: int, y: int) -> int:
        """Number stuff."""
        if x < y:
            return y - x
        else:
            return x - y

    def bar(word: str) -> str:
        """Word doubler."""
        return word + word

    def main() -> None:
        """The main function."""
        number: int = foo(4, 5)
        other_num: int = foo(x = -4, y = -5)
        doubled: str = bar(str(foo(x = 46, y = 2)))

    main()
```

</details>

## Recursion

### Conceptual

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

### Code Writing

Note: This function-writing question is more challenging than what will be on the quiz, but is still good practice for understanding recursion and will help you be very well prepared to answer other, less challenging function writing questions in a quiz environment.

1. **Challenge Question:** Write a recursive function named `sum` that has an `int` parameter `number` and returns an `int` that is the sum of all nonnegative integers up to and *including* `number` (`1 + 2 + ... + number`). For example, `sum(number=4)` should evaluate to `1 + 2 + 3 + 4 = 10`. If a negative argument for `number` is given, just return `-1` (What case is this?). It may help to come up with your base case and recursive case before beginning to write any code.

<details>
<summary>SHOW SOLUTIONS</summary>

1. The negative argument case is an edge case. Note: There are many equivalent ways this function could be written.

```py
    def sum(number: int) -> int:
        """Sum of all nonnegative integers up to and including number."""
        if number < 0: # Edge case
            return -1
        elif number > 0: # Recursive case
            return number + sum(number=number - 1)
        else: # Base case
            return 0
```

</details>

&nbsp;