---
title: Supplementary Final Exam Practice Questions
author:
- Izzi Hinks
- Alyssa Lytle
page: lessons
template: overview
---

Please note that these final exam practice questions are intended to *supplement* the Quiz 00-04 practice questions, your previous quizzes, LS/CQ/EX assignments, and lecture content as study materials. The final exam covers content from every unit/quiz, not solely the concepts covered in these questions. 


# Multiple Choice with Code Snippets

1. What does the following expression evaluate to?

    ```python
    13 % 4
    ```

    a. `0`

    b. `1`

    c. `3`

    d. `4`

    e. `9`

2. What is the output for the following code?

    ```python
    x: int = 4
    y: int = x
    x += 1
    print(y)
    ```

    a. `y`

    b. `5`

    c. `4`

    d. `x`

    e. `1`

3. Consider the following code snippet:

    ```python
    leaf: list[int] = [3]
    flower: list[int] = leaf
    flower.append(2)
    ```

    What would `print(flower)` output after the code snippet was executed?

    a. `[3]`

    b. `[3, 2]`

    c. `[5]`

    d. `[2]`

    e. `Error`

4. Consider the following code snippet (same as question 3):

    ```python
    leaf: list[int] = [3]
    flower: list[int] = leaf
    flower.append(2)
    ```

    What would `print(leaf)` output after the code snippet was executed?

    a. `[3]`

    b. `[3, 2]`

    c. `[5]`

    d. `[2]`

    e. `Error`

5. What is the printed output of the following code snippet? If there is an Error, select Error.

    ```python
    a: str = "swamp"
    b: int = 110
    print(a + b)
    ```

    a. `swamp110`

    b. `swamp + 110`

    c. `swamp`

    d. `Error`


6. What does the following expression evluate to? What is its data type?

    ```python
    "293874"[int("73198"[2])]
    ```

    a. `1`, int

    b. `1`, str

    c. `2`, int

    d. `2`, str

    e. `3`, int

    f. `3`, str

    g. `9`, int

    h. `9`, str

    i. `Error`

<details>
<summary>SOLUTIONS</summary>

1. b. `1`. Remember, the % (modulo) operator finds the remainder!

2. c. `4`. `y` was initialized to be `x`'s literal value at the time the second line was exected. Since integers are *primitive types*, x and y are not "linked" or referring to the same location in memory.

3. b. `[3, 2]`. 

4. b. `[3, 2]`. Because lists are *reference types*, the line, `flower: list[int] = leaf`,  caused `flower` to refer to the same exact `list[int]` stored in memory as `leaf`. If we did a memory diagram of this code listing, they would refer to the same ID in the heap! When a value was appended to `flower`, it inherently was appended to `leaf`'s list, too (because they refer to the *same* list).

5. d. `Error`. This code snippet would lead to a TypeError; a string and an integer cannot be concatenated together.

6. h. `9`, str. We would start with the inner-most parentheses for this question: `"73198"[2]`. Index 2 of the string has the character `"1"`. So, we can plug `"1"` in in place of that portion of the expression, giving us: `"293874"[int("1")]`. Now, the next step is to cast the string `"1"` to an int. After doing so, we have: `"293874"[1]`. Index 1 of the string has the character `"9"` (a str).

</details>

&nbsp;

# Looping Questions

Use the following list and dictionary in the questions below.

```py
acro: list[str] = ["n", "a", "s", "a"]
missions: dict[str, int] = {"Apollo": 11, "Voyager": 1, "Artemis": 2}
```

1. What will be printed? If it will result in an Error, write "Error."

    ```py
    for x in range(0, len(acro)):
        print(x)
    ```

2. What will be printed? If it will result in an Error, write "Error."

    ```py
    for x in range(0, len(acro)):
        print(acro[x])
    ```

3. What will be printed? If it will result in an Error, write "Error."

    ```py
    for x in range(1, len(missions)):
        print(x)
    ```

4. What will be printed? If it will result in an Error, write "Error."

    ```py
    for x in range(0, len(missions)):
        print(missions[x])
    ```

5. What will be printed? If it will result in an Error, write "Error."

    ```py
    for a in acro:
        print(a)
    ```

6. What will be printed? If it will result in an Error, write "Error."

    ```py
    for a in acro:
        print(acro[a])
    ```

7. What will be printed? If it will result in an Error, write "Error."

    ```py
    for m in missions:
        print(m)
    ```

8. What will be printed? If it will result in an Error, write "Error."

    ```py
    for m in missions:
        print(missions[m])
    ```

9. What will be printed? If it will result in an Error, write "Error."

    ```py
    if "COMP110" in missions:
        print("Found!")
    else:
        print("Not yet...")
    ```

10. What will be printed? If it will result in an Error, write "Error."

    ```py
    def go(m: dict[str, int]) -> str:
        for thing in m:
            return thing
        return "Other"

    print(go(m=missions))
    ```

<details>
<summary>SOLUTIONS</summary>

1. 

    ```py
    0
    1
    2
    3
    ```

2. 

    ```py
    n
    a
    s
    a
    ```

3. 

    ```py
    1
    2
    ```

4. `Error`

5. 

    ```py
    n
    a
    s
    a
    ```

6. `Error`

7. 

    ```py
    Apollo
    Voyager
    Artemis
    ```

8. 

    ```py
    11
    1
    2
    ```

9. 

    ```py
    Not yet...
    ```

10. In a function body, as soon as we reach a return statement and evaluate the expression to the right of `return`, we are exiting the function and returning the return value back to the line where the function was called (the return address)! This is why the repeat block of this for loop was only executed *once*. 

    ```py
    Apollo
    ```


</details>

&nbsp;