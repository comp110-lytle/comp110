---
title: Week 13 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)
<br>

# Questions 

### Default Parameters

##### Conceptual Questions:

1. What is a default parameter in Python functions? Explain with a simple example.

2. Write a function with a default parameter. Demonstrate both the default behavior and overridden behavior by calling the function twice.

3. Consider the function definition below. What will be the output when calling this function without arguments, and why?
~~~
def print_values(x, y=10, z=20):
    print("X:", x, "Y:", y, "Z:", z)
~~~

4. Explain the order of parameters when using default and non-default parameters in a function. Why must non-default parameters precede default parameters?


##### Multiple Choices
1. What is the output of the following function call?
~~~
def display(a, b=4, c=6):
    return a + b + c
print(display(1))
~~~
A) 1 <br>
B) 11 <br>
C) Error <br>
D) None of the above <br>

2. Which of the following is true about default parameters in Python?
A) A non-default parameter cannot follow a default parameter. <br>
B) Default parameters can be placed in any order. <br>
C) Only one default parameter is allowed per function. <br>
D) Default parameters are evaluated at compile time. <br>

3. What will be the output of the following code?
~~~
def append_number(lst=[], number=1):
    lst.append(number)
    return lst
print(append_number())
print(append_number())
~~~
A) [1], [1] <br>
B) [1], [1, 1] <br>
C) [1, 1], [1, 1] <br>
D) [1], [2] <br>

4. Consider the following function definition:
~~~
def make_sentence(noun="dog", verb="barks"):
    return f"The {noun} {verb}."
~~~
Which function call correctly changes the verb while keeping the default noun?
A) make_sentence("runs") <br>
B) make_sentence(verb="runs") <br>
C) make_sentence("dog", "runs") <br>
D) make_sentence(noun="runs") <br>

##### True or False
1. (For elaboration)True or False: Default parameters are re-evaluated every time a function is called.


2. True or False: In Python, you can have default parameters followed by non-default parameters in a function definition.


3. True or False: It is considered good practice to use mutable objects like lists or dictionaries as default parameter values.


### Union Types

##### Conceptual Questions:

1. What is a Union type in Python and why is it used?

2. How do you specify that a function parameter can be either an integer or a string using type hints?

3. Explain the difference between using Union and using Optional in type hints.

##### Multiple Choices Questions:
1. How can you define a variable age that can either be an integer or a string using Python 3.10 or later?
A) age: int | str <br>
B) age: int or str <br>
C) age: Union[int, str] <br>
D) Both A and C are correct <br>

2. What does the Optional[int] type hint imply about the variable’s possible values?
A) The variable can be any number <br>
B) The variable can only be an integer <br>
C) The variable can be an integer or None <br>
D) The variable can be optional in function calls <br>

3. If a function parameter is annotated as Union[int, str], what does it mean?
A) The parameter can only accept integers <br>
B) The parameter can only accept strings <br>
C) The parameter can accept either an integer or a string <br>
D) The parameter can accept any type as Python is dynamically typed <br>

4. Consider the following function definition:
~~~
def process_data(data: Union[int, str]) -> str:
    return str(data)
~~~
What is the return type of the function?
A) int <br>
B) str <br>
C) Union[int, str] <br>
D) None <br>

5. What is the purpose of using Union types in the context of Python’s type hinting system?
A) To restrict function parameters to a single specified type
B) To specify that variables or parameters can be one of several types
C) To enhance the performance of Python applications
D) To convert values between different types automatically

### Magic Methods:
1. What is the purpose of magic methods in Python?

2. Explain the usage of __str__ magic methods.

3. If you want to implement operator overloading for the "+" operator in a custom class, which magic method would you use?
A) __add__ <br>
B) __sum__ <br>
C) __plus__ <br>
D) __concat__ <br>

4. What magic method would you implement to customize the behavior of the built-in function print() when it is called with an object of your class?
A) __print__
B) __str__

5. Which magic method is called when you use the del statement on an object?
A) __delete__
B) __del__
C) __remove__
D) __destruct__


<br>

# Solutions

### Default Parameters

##### Conceptual Questions:

1. A default parameter in Python functions is a parameter that assumes a default value if no value is provided for it during the function call.

2. 
~~~
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # By default
print(power(3, 3))  # Now you have overriden the default value
~~~

3. Since `x` does not have a default value, directly calling the function without parameters will raise an Error.

4. In Python function definitions, non-default parameters must precede default parameters. As otherwise will create errors for 1. positional argument assignment; 2. letting Python identify which parameter(s) are optional.



##### Multiple Choices
1. B

2. A

3. B

4. B

##### True or False
1. False

2. False

3. False

### Union Types

##### Conceptual Questions:

1. A Union type in Python allows a variable or function parameter to accept multiple types rather than just one single type.

2. `value: Union[int, str]` or `value: int | str`

3. Union refers that this variable can be with multiple types but still required, whereas the Optional refers that this variable is not required.

##### Multiple Choices Questions:
1. D

2. C

3. C

4. B

5. B

### Magic Methods:
1. Magic methods in Python are special methods that allow you to redefine or modify the default behaviors of Python objects. Often recognized by their double underscores at the beginning and end (e.g., __init__, __str__).

3. A

4. B

5. B
