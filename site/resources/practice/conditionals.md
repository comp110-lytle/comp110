---
title: Conditionals 
author:
- Alyssa Lytle
- Viktorya Hunanyan
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## 1. Multiple Choice

1.1. Every `if` statement must be followed by a paired `else` branch. (T/F)

1.2. Lines contained in an `else` branch in Python do not have to be indented. (T/F)

1.3. You can name a variable `else` in your program without Python confusing your variable's name and the `else` keyword. (If you are unsure, this is a good one to try yourself!) (T/F)


<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
  

1.1. `False`
1.2. `False`
1.3. `False`

</details>

&nbsp;

<!-- 
## 2. Inputting a Value

 All subquestions of this problem will refer to this code snippet:

        x: int = int(input("Pick a number: "))
        y: int = 10
        z: int = 2
        x = x - 1
        if x < 10:
            print("A")
        else:
            if (x % z) == 0:
                print ("B")
        if x == (y + z):
            print("C")
        else: 
            print("D")

For the following subquestions, answer with a valid input value for `x` that would cause the given letter to print. It is OK for your input to cause other letters to print as well.
If there is no such value, write "Unreachable".

4.1 `A`

4.2 `B`

4.3 `C`

4.4 `D`

Now, answer with a valid input value for `x` that
would cause the *exact* given letter(s) to print (no other letters). 
If there is no such value, write "Unreachable".  
4.5 

`A` <br>
`C`

4.6 

`B` <br>
`C`


4.7 

`C`


4.8 

`D` -->

<!-- 
5. Write the format of a conditional using the following:
You might not need to use all and can use any multiple times: `if`, `else`, `==`, `<condition>`, `False`, `True`, `<do something>`.

6. Write the format of a conditional using the following:
You might not need to use all and can use any multiple times: `while`, `<condition>`, `==`, `False`, `True`, `<do something>`. -->


## 2. Conceptual 

2.1. What does the *condition* of a conditional have to evaluate to in order to enter its `then` block?

2.2. What does the *condition* of a conditional have to evaluate to in order to enter its `else` block?

2.3. What happens when a `return` statement is encountered?


<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
  

2.1. The condition must evaluate to `True`.

2.2. The condition must evaluate to `False`.

2.3. The return value is recorded in memory and the function is immediately exited.

</details>

&nbsp;


<!-- ## 3. Code Snippet 1

All subquestions of this problem will refer to this pseudo code snippet:

```
    if <condition1>:
        <do_something> # then block
    elif <condition2>:
        <do_something> # elif block
    else:
        <do_something> # else block
```

3.1. From the general format of a conditional with an `elif` block, what needs to be True and/or False in order for the `elif` block to evaluate?

3.2. Is `<condition1>` not being met the same as having `if <condition1> == False:`? -->

## 3. Code Snippet 

All subquestions of this problem will refer to this code snippet:

```python
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

3.1. What is the condition in this code?

3.2. What does the condition evaluate to? (Don’t do it in your head, draw a memory diagram!)

3.3. What values should x, y, and/or z have to be assigned to in order for the else block to run?

3.4. What other values can x, y, and/or z be assigned in order for the `if` block to run?



<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
  

3.1. `not(x != y and x != "y")`

3.2. The condition evaluates to `True`.

3.3. To ensure the `else` block runs in the given code, the condition `x != y and x != "y"` must be true. This means `x` should be different from `y` and `x` should also be different from the string `"y"`. For example, setting `x = "a"` and `y = "b"` will satisfy this condition, making the `else` block execute.

3.4. To make the `if` block run, the condition `not(x != y and x != "y")` must be true, which happens when `x` is either the same as `y` or the same as `"y"`, or both. In the original code where `x = "y"`, `y = "x"`, and `z = "x"`, the `if` block runs as `not(x != y and x != "y")` evaluates to true.


</details>

&nbsp;


<!-- ---


[solutions](#conceptual-solutions)

# Solutions 

## Conceptual Questions - Solutions

1.1. F
1.2. F
1.3. F -->

<!-- 4. 
    
    4.1 Any value < 11

    4.2 Any value >= 11 and odd. (Since `x % z == 0` must be True and `z` is 2, this means `x - 1` must be even.)

    4.3 13

    4.4 Any value != 13

    4.5 Unreachable

    4.6 13

    4.7 Unreachable

    4.8 Any value >= 11 and even -->
<!-- 
5. 
```python
    if <condition> == True:
        <do_something>
    else:
        <do_something>
```
OR
```python
    if <condition>:
        <do_something>
    else:
        <do_something>
```

6. 
```python
    while <condition> == True:
        <do_something>
```
OR
```python
    while <condition>:
        <do_something>
``` -->

<!-- 2.1. The condition must evaluate to `True`.

2.2. The condition must evaluate to `False`.

2.3. The return value is recorded in memory and the function is immediately exited. -->
<!-- 
3.1. `<condition1>` must not be met (condition should evaluate to `False`) AND `<condition2>` must be met (condition should evaluate to `True`).

3.2. In this case, yes. If we had something like this:
```python
if ("hello" == "hello") == False:
```
the `<condition>` in this case would be everything in between the `if` and the `:`. In the pseudo-code, we are separating the `<condition>` to be separate from the rest (`== False`), while in real code the condition is always everything after the `if` and before the `:`. -->

<!-- ---

3.1. `not(x != y and x != "y")`

3.2. The condition evaluates to `True`.

3.3. To ensure the `else` block runs in the given code, the condition `x != y and x != "y"` must be true. This means `x` should be different from `y` and `x` should also be different from the string `"y"`. For example, setting `x = "a"` and `y = "b"` will satisfy this condition, making the `else` block execute.

3.4. To make the `if` block run, the condition `not(x != y and x != "y")` must be true, which happens when `x` is either the same as `y` or the same as `"y"`, or both. In the original code where `x = "y"`, `y = "x"`, and `z = "x"`, the `if` block runs as `not(x != y and x != "y")` evaluates to true.

--- -->