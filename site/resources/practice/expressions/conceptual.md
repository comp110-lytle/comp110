---
title: Expressions Types Conceptual Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
- Benjamin Eldridge
page: lessons
template: overview
---

# Questions


## Conceptual

1. What is the resulting *value* and *data type* of the following expression? `int("20")`
2. What is the resulting *value* and *data type* of the following expression? `str(2023) + str(2023)`
3.	What is the resulting value of the following expression?
` type(9 / len( str(110)) `
4. What is the resulting value of the following expression? `"440" + "20"`
5. What value of x would cause the following expression to evaluate to `True`?
` (3 + x) == (55 % 2 ** 4) `
6. What value does the following expression result in, and what is its type? `2 + 2 / 2 ** (2 * 0)`
7.	Using subscription syntax and concatenation, write an expression that evaluates to `"tar"` using the following string: `“Saturday"`.
8.  What data type do expressions with *relational operators* typically evaluate to?
9.  What does the following expression evaluate to? `int("10" + "40") > 100 * 2`
10. What are the *types* of the following expressions and what *values* do they evaluate to? If an error would occur, just write `Error`.

    10.1. `1.5 + 2`

    10.2. `"hehe" * 2`

    10.3. `len("110") ** 2`

    10.4. `str(110) * 2.1`

    10.5. `float("100.0") / 20`

    10.6. `21 // 2 ** 2 + 3`

    10.7. `float("220") >= float("100" + "100")`

    10.8. `int("COMP 110"[5]) + 99.0`

    10.9. `(42 % 4) == (79 % 11)`

    10.10. `int(4.99)`

11. Which of the following expressions correctly *concatenates* two strings together?

    a. `"clam" * "chowder"`

    b. `"clam" + "chowder"`

    c. `"clam" , "chowder"`

    d. `"clam" : "chowder"`

12. When using subscription syntax, what *index* does Python start with?

    a. `-1`

    b. `0`

    c. `1`

    d. `""`

    e. `True`



13. Use subscription notation, string concatenation, and the string `"nevermind"` to write an expression that evaluates to `"nvm"`.

[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions

1. `20`, `int`
2. `"20232023"`, `str`
3. `<class 'float'>` (Or just `float` is sufficient on a quiz.)
4. `"44020"`
5. `4`
6. `4.0`
7. There are two possible answers:
    
    `"Saturday"[2] + "Saturday"[1] + "Saturday"[4]`

    or

    `"Saturday"[2] + "Saturday"[6] + "Saturday"[4]`

8. `bool`
9. `True`
10. 
    10.1. Type: `float` Value: `3.5`

    10.2. Type: `str` Value: `"hehehehe"`

    10.3. Type: `int` Value: `9`

    10.4. `TypeError`

    10.5. Type: `float` Value: `5.0`

    10.6. Type: `int` Value: `8`

    10.7. Type: `bool` Value: `False`

    10.8. Type: `float` Value: `100.0`

    10.9. Type: `bool` Value: `True`

    10.10. Type: `int` Value: `4`

11. B
12. B
13. `"nevermind"[0] + "nevermind"[2] + "nevermind"[5]`

