---
title: Expressions Types Conceptual Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
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

