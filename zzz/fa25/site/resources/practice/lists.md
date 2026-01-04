---
title: Lists
author:
- Viktorya Hunanyan
- Benjamin Eldridge
page: lessons
template: overview
---

## Lists

### Conceptual Questions
1. Explain in words how you modify elements in a list? How would you do this in python? Give an example. 

2. Write the general formula of how you call a method on an object (such as a list or dictionary) using the following. You might not need to use all and can use any multiple times: `<method_name>`, `()`, `<object_variable>`, `.` , `<arg>`. Give examples. 

3. Give two ways of instantiating an empty list. What are the components you need and what does each part do? Give an example for each. Your explanation should include the words 'function', 'constructor', 'variable', 'instantiate', 'assign', and 'reference'. 

<details>
<summary>SHOW SOLUTIONS</summary>

1. In order to modify elements in a list, you first need to identify the element you want to change. Then you must find where the element is within your object. Once you have access to the element’s position, you then want to assign at that position in the list to the desired value. Lists in Python are ordered collections, which means each element has a specific index that starts from 0. You can access elements in a list using these indices.

    To access an element, use the index inside square brackets `[]`. 
    To modify an element, you use the assignment operator `=`. 

    For example: 

    ```python
        # example
        my_list: list[“bark”, “meow”, “tweet”] # Change “meow” to “moo”
    ```

    In this example, we want to change "meow", which is at index 1, to "moo". Using the square brackets for subscription notation, we assign a new value at that index like this:

    ```python
        my_list[1] = “moo”
    ```

2. `<object_variable>`.`<method_name>`(`<arg>`)

    For more arguments, you'd have

    `<object_variable>`.`<method_name>`(`<arg>, <arg>`)

    And so on.


    ```python
        # example
        my_list.pop(0)
        my_list.append(“Hello”)
    ```

3. Two ways of instantiating an empty list:

    - *Using the list constructor:*
    The `list()` function is a constructor that instantiates an empty list object. The constructor belongs to the `List` class. The constructor doesn't take any arguments for creating an empty list. You assign the result of this function to a variable, which will reference the newly created empty list.

    Example:
    ```python
        empty_list: list[str] = list()
    ```
    - *Components:*
        - `list()`: The constructor function that creates a new list object.
        - `list[str]`: This is the type of `empty_list`, it is a `list` that will contain `str`s (it could also contain other types of data like `int`s). Always include a type when declaring a new variable!
        - `empty_list`: A variable that is assigned the reference to the new list object created by the `list()` constructor.

    - *Using square brackets literal:*
    You can instantiate an empty list using a pair of square brackets `[]`. This directly creates and instantiates a new empty list object, which you then assign to a variable.

    Example:
    ```python
        empty_list: list[str] = []
    ```
    - **Components:**
        - `[]`: This is shorthand syntax for creating and instantiating an empty list object.
        - `list[str]`: This is the type of `empty_list`, it is a `list` that will contain `str`s (it could also contain other types of data like `int`s). Always include a type when declaring a new variable!
        - `empty_list`: A variable that is assigned the reference to the newly instantiated empty list.
    </details>

