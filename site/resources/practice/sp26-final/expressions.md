---
title: Expressions Practice Problems
author:
- Alyssa Lytle
- Team 110
- Izzi Hinks
- Benjamin Eldridge
page: lessons
template: overview
---


# Expressions

1. Give the *value* and *type* of the following expressions:

1.1 `int("20")`

1.2 `str(2023) + str(2023)`

1.3 `"440" + "20"`

1.4 `2 + 2 / 2 ** (2 * 0)`

1.5 `1.5 + 2`  

1.6 `"hehe" * 2`  

1.7 `len("110") ** 2`  

1.8 `float("100.0") / 20`  

1.9 `20 / 2 ** 2 + 3`  

1.10 `float("220") >= float("100" + "100")`  

1.11 `int("COMP 110"[5]) + 99.0`  

1.12 `(42 % 4) == (79 % 11)` 

<details>
  <summary><b>SHOW SOLUTIONS</b></summary>

1.1 value `20`, type `int`

1.2 value `"20232023"`, type `str`

1.3 value `"44020"`, type `str`

1.4 value `4.0`, type `float`

1.5 value `3.5`, type `float`

1.6 value `"hehehehe"`, type `str`

1.7 value `9`, type `int`  

1.8 value `5.0`, type `float`  

1.9 value `8.0`, type `float`  

1.10 value `False`, type `bool`  

1.11 value `100.0`, type `float`  

1.12 value `True`, type `bool` 
  </details>

2. Using subscription notation on `"nevermind"`, build an expression equal to `"nvm"`.

<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
2. `"nevermind"[0] + "nevermind"[2] + "nevermind"[5]`
</details>

3. What type do relational operators usually produce?

<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
`bool`
</details>

4. Write a line of code to get the middle character of any odd-length string `s` using `s` and `len()`

<details>
  <summary><b>SHOW SOLUTIONS</b></summary>
 `s[(len(s) - 1)/ 2]`

 or 
 
`s[len(s) // 2]`
</details>