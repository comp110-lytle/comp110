---
title: Signature Writing Practice
author:
- Alyssa Lytle
- Viktorya Hunanyan
- Megan Zhang
- David Karash
- Benjamin Eldridge
page: lessons
template: overview
---

# Questions

## Signature Writing

The following questions will have you practice signature writing.

1. What is a function signature, and why is it significant?

2. Write the function signature for a function called `pos_or_neg` that takes as input an integer and returns `"Positive"` if the integer is positive and returns `"Negative"` if the integer is negative. Use `number` as the name of the parameter.

3. Write the function signature for a function called `gcd` that takes two integers as input and returns the integer that is their greatest common divisor. Use `num_one` and `num_two` as your parameter names.

4. Write the *signature* for a function called `name_eval` that takes as input someone's name as a string and returns `True` if the name has an even amount of letters and `False` if it has an odd amount of letters.

5. Write the *signature* for a function called `name_size` that takes as input someone's name as a string and returns the *length* of their name as an integer.

6. Write the *signature* for a function called `gcd` that takes two floats as input and returns the integer that is their greatest common divisor.


[solutions](#signature-writing-solutions)

## Complete the function definition

1. Line 2 belongs within the body of a function. Add a line of code that will complete the entire function definition. 

```python
    
        return x * 2

    print(double(x=3))
```

2. Line 2 belongs within the body of a function. Add a line of code that will complete the entire function definition. The function's name is `my_string`. 

```python
    
        return "This is my word, " + word

```

3. Line 2 belongs within the body of a function. Add a line of code to complete the entire function definition. The function's name is `my_num` and `word` is a `float`. 

```python
    
        print("This is my number, " + str(word))

```


# Solutions

## Signature Writing Solutions

1. A function signature refers to the first line of a function definition, where the def keyword is used. Following the def keyword is the function name, and after the function name is a set of parentheses that enclose the parameter list. After the parameter list comes the return type. The function signature is important because it defines how the function can be called and what kinds of inputs and outputs are expected. Without a signature, you wouldn't know what parameters to provide or even how to call the function, since the function name would be missing.

2.
```python
def pos_or_neg(number: int) -> str:
```

3.
```python
def gcd(num_one: int, num_two: int) -> int:
```

4. `def name_eval(id: str) -> bool:`

*(Note that I chose to call the parameter `id`, but you could've chosen any valid name!)*

5. `def name_size(id: str) -> int:`

*(Note that I chose to call the parameter `id`, but you could've chosen any valid name!)*

6. `def gcd(number_a: float, number_b: float) -> int:`

*(Note that I chose to call the parameters `number_a` and `number_b`, but you could've chosen any valid name!)*


## Complete the function definition

1. **Complete function definition**

```python
    def double(x: int) -> int:  # Added this line
        return x * 2

    print(double(x=3))
```

2. **Complete function definition**

```python
    def my_string(word: str) -> str:  # Added this line
        return "This is my word, " + word
```

3. **Complete function definition**

```python
    def my_num(word: float) -> None:  # Added this line
        print("This is my number, " + str(word))
```