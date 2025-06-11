---
title: Signature Writing Practice
author:
- Alyssa Lytle
- Viktorya Hunanyan
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Signature Writing

The following questions will have you practice signature writing.

1. Write the *signature* for a function called `name_eval` that takes as input someone's name as a string and returns `True` if the name has an even amount of letters and `False` if it has an odd amount of letters.

2. Write the *signature* for a function called `name_size` that takes as input someone's name as a string and returns the *length* of their name as an integer.

3. Write the *signature* for a function called `gcd` that takes two floats as input and returns the integer that is their greatest common divisor.


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

1. `def name_eval(id: str) -> bool:`

*(Note that I chose to call the parameter `id`, but you could've chosen any valid name!)*

2. `def name_size(id: str) -> int:`

*(Note that I chose to call the parameter `id`, but you could've chosen any valid name!)*

3. `def gcd(number_a: float, number_b: float) -> int:`

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