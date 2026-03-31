---
title: Practice Problems
author:
- Alyssa Lytle
- Team 110
- Izzi Hinks
- Benjamin Eldridge
page: lessons
template: overview
---


# Quiz 00 Practice Problems

The following questions will help solidify concepts learned in class, as well as prepare you for the quizzes and final!

If you feel overwhelmed by the number of questions here, start with just a couple from each section that you think would help fill in any knowledge gaps you have. Then, work through the remaining questions as needed for additional practice.

The quiz itself will be similar in difficulty to these practice questions. In addition to these questions, you should review all of your lesson responses and challenge questions on Gradescope. 

<!-- It is also recommended to complete the [practice memory diagrams](/resources/practice/MemDiagrams.html). -->

If you find yourself feeling lost, please ask for help in [office hours or tutoring](/support).

## Multiple Choice and True/False

1. What is a `bool` data type in Python?

    a. Data type for storing text

    b. Data type for storing whole numbers such as `-10`, `3`, or `100`

    c. Data type for storing True/False values

    d. Data type for storing any type of information

    e. Data type for storing numbers with a decimal point such as `1.0`, `3.14`, or `-0.1`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `C`.

</details>

&nbsp;

2. What is an `int` data type in Python?

    a. Data type for storing text

    b. Data type for storing whole numbers such as `-10`, `3`, or `100`

    c. Data type for storing True/False values

    d. Data type for storing any type of information

    e. Data type for storing numbers with a decimal point such as `1.0`, `3.14`, or `-0.1`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

3. What is a `str` data type in Python?

    a. Data type for storing text

    b. Data type for storing whole numbers such as `-10`, `3`, or `100`

    c. Data type for storing True/False values

    d. Data type for storing any type of information

    e. Data type for storing numbers with a decimal point such as `1.0`, `3.14`, or `-0.1`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `A`.

</details>

&nbsp;

4. An `int` literal can begin with any number of zeroes.

    a. True

    b. False

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

5. Which of the following literals are a `float`?

    a. `4`

    b. `"4"`

    c. `4.0`

    d. `"4.0"`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `C`.

</details>

&nbsp;

6. What function can you use to determine the type of an object in Python?

    a. `print()`

    b. `str()`

    c. `len()`

    d. `type()`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `D`.

</details>

&nbsp;

7. What is the *type* of the following expression?

    ```python
    1.5 + 2
    ```

    a. `int`

    b. `float`

    c. `str`

    d. `bool`

    e. `TypeError`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

8. What is the *type* of the following expression?

    ```python
    len("cottage")
    ```

    a. `int`

    b. `float`

    c. `str`

    d. `bool`

    e. `TypeError`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `A`.

</details>

&nbsp;

9. What is the result of the following expression?

    ```python
    "110" + "110"
    ```

    a. `220`

    b. `"110110"`

    c. `TypeError`

    d. `"220"`

    e. `"110""110"`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

10. What is the result of the following expression?

    ```python
    102 % 5
    ```

    a. `2`

    b. `20.4"`

    c. `"20"`

    d. `TypeError`

    e. `2.0`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `A`.

</details>

&nbsp;

11. What is the *type* of this value in Python?

    ```python
    "True"
    ```

    a. `bool`

    b. `str`

    c. `TypeError`

    d. `int`

    e. `float`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`. While this may look like a `bool`, the quotes make it a `str`!

</details>

&nbsp;

12. What *value* will the following expression evaluate to?

    ```python
    "map"[1]
    ```

    a. `"ap"`

    b. `"m"`

    c. `str`

    d. `"a"`

    e. `TypeError`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `D`. Don't forget, Python indexing begins at 0!

</details>

&nbsp;

13. What will the following expression evaluate to? 

    ```python
    int(3.8 + 1)
    ```

    a. `4.8`

    b. `5`

    c. `3.81`

    d. `4`

    e. `TypeError`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `D`. `3.8 + 1` evaluates to the `float` `4.8`, but when converted to an `int` by `int()`, the precision is removed/truncated.

</details>

&nbsp;

## Expressions

1. What are the *types* of the following expressions and what *values* do they evaluate to? If a `TypeError` occurs, just write `TypeError`.

    1.1. `1.5 + 2`

    1.2. `"hehe" * 2`

    1.3. `len("110") ** 2`

    1.4. `str(110) * 2.1`

    1.5. `float("100.0") / 20`

    1.6. `21 // 2 ** 2 + 3`

    1.7. `float("220") >= float("100" + "100")`

    1.8. `int("COMP 110"[5]) + 99.0`

    1.9. `(42 % 4) == (79 % 11)`

    1.10. `int(4.99)`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answers are: 

    1.1. Type: `float` Value: `3.5`

    1.2. Type: `str` Value: `"hehehehe"`

    1.3. Type: `int` Value: `9`

    1.4. `TypeError`

    1.5. Type: `float` Value: `5.0`

    1.6. Type: `int` Value: `8`

    1.7. Type: `bool` Value: `False`

    1.8. Type: `float` Value: `100.0`

    1.9. Type: `bool` Value: `True`

    1.10. Type: `int` Value: `4`

</details>

&nbsp;

2. Which of the following expressions correctly *concatenates* two strings together?

    a. `"Michael" * "Jordan"`

    b. `"Michael" + "Jordan"`

    c. `"Michael" , "Jordan"`

    d. `"Michael" : "Jordan"`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

3. When using subscription syntax, what *index* does Python start with?

    a. `-1`

    b. `0`

    c. `1`

    d. `""`

    e. `True`

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `B`.

</details>

&nbsp;

4. What value would you substitute for `x` to make the following expression True? Note: There is only one correct value here.

```python
(3 + x) == ((55 // 11) ** 2)
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `22`.

</details>

&nbsp;

5. Use subscription notation, string concatenation, and the string `"nevermind"` to write an expression that evaluates to `"nvm"`. Hint: Break this problem down into smaller pieces by first thinking of how you would write an expression using `"nevermind"` and subscription notation that evaluates to `"n"`.

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `"nevermind"[0] + "nevermind"[2] + "nevermind"[5]`.

</details>

&nbsp;

## Functions

1. What is a function call, and how does it differ from a function definition?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  A function definition is where you create the function and specify what it does. It includes the function signature and everything indented below it. The signature consists of the function name, parameters, the types of the parameters, and the return type. The function body contains the code block that executes when the function is called, and generally ends with a `return` statement. A function call occurs when you invoke or execute the function by writing the function name followed by parentheses. If the function accepts inputs, the parentheses will contain the values assigned to the parameters, also known as arguments. When a function definition is encountered, the function body is not executed; it is bypassed until the function is called. To call a function, you must first define it.

</details>

&nbsp;

2. What is the difference between parameters and arguments in the context of functions?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  Parameters are the variables listed in the function signature that define the expected inputs. Your parameters will hold the values passed into the function when the function is called. These values that are assigned to the parameters are called arguments. Arguments are the actual values passed to the function when it is called.

</details>

&nbsp;

3. When you call a function, once the function is executed, where do you return back to?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  After the function is executed, you will return back to the point in the code where the function was called. In your memory diagrams, this is called the "Return Address" or just "RA".

</details>

&nbsp;

4. If you never encounter a return statement in your function, what is your return value?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  If there is no return statement in a function, it returns None by default.

</details>

&nbsp;

5. What does the `len()` function do in Python?

    a. Converts a value to a string

    b. Rounds a number to the nearest whole number

    c. Returns the length of a sequence, such as a `str`

    d. Converts a string to a number
    
    e. Counts the digits in an int

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is `C`.

</details>

&nbsp;

6. Given the following function definition, answer the following questions.

    ```python
        def evaluate_length(name: str) -> int:
            """This function returns the length of the name."""
            return len(name)
    ```

    6.1. What is the result of the following function call? 
    `evaluate_length("airplane")`

    6.2. What is the *type* of the parameter `name`? What is the *return type* of this function?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answers are:

  6.1. `8`
  
  6.2. The type of `name` is `str` and the return type of the function is `int`.

</details>

&nbsp;

7. Given the following function definition, answer the following questions.

    ```python
        def tablespoons_to_teaspoons(tablespoons: int) -> str:
            """This functions tells you how many teaspoons are in the given number of tablespoons."""
            return str(tablespoons * 3) + " teaspoons"
    ```

    7.1. Write a function call to `tablespoons_to_teaspoons` that returns the string `"9 teaspoons"`.

    7.2. What is the *type* of the parameter `tablespoons`? What is the *return type* of this function?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answers are:

  7.1. `tablespoons_to_teaspoons(tablespoons=3)`
  
  7.2. The type of `tablespoons` is `int` and the return type of the function is `str`.

</details>

&nbsp;

## Function Signatures

1. What is a function signature, and why is it significant?

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  A function signature refers to the first line of a function definition, where the `def` keyword is used. Following the `def` keyword is the function name, and after the function name is a set of parentheses that enclose the parameter list. After the parameter list comes the return type. The function signature is important because it defines how the function can be called and what kinds of inputs and outputs are expected. Without a signature, you wouldn't know what parameters to provide or even how to call the function, since the function name would be missing.

</details>

&nbsp;

2. Write the function signature for a function called `pos_or_neg` that takes as input an integer and returns `"Positive"` if the integer is positive and returns `"Negative"` if the integer is negative. Use `number` as the name of the parameter. Note: You are not writing the body of this function so do not worry about how it would actually work on the inside for this question.

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is: 

  ```python
  def pos_or_neg(number: int) -> str:
  ```

</details>

&nbsp;

3. Write the function signature for a function called `gcd` that takes two integers as input and returns the integer that is their greatest common divisor. Use `num_one` and `num_two` as your parameter names. Note: You are not writing the body of this function so do not worry about how it would actually work on the inside for this question.

<details>
  <summary><b>SHOW SOLUTION</b></summary>
  
  The correct answer is:

  ```python
  def gcd(num_one: int, num_two: int) -> int:
  ```

</details>