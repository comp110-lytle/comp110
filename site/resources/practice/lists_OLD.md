---
title: Lists Conceptual Questions
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Questions

## List General Questions
1. Explain in words how you modify elements in a list? How would you do this in python? Give an example. 

<details>
<summary>SHOW SOLUTIONS</summary>
In order to modify elements in a list, you first need to identify the element you want to change. Then you must find where the element is within your object. Once you have access to the element’s position, you then want to assign at that position in the list to the desired value. 
Lists in Python are ordered collections, which means each element has a specific index that starts from 0. You can access elements in a list using these indices.

To access an element, use the index inside square brackets []. 
To modify an element, you use the assignment operator =. 

For example: 

```python
    # example
    my_list: list[“bark”, “meow”, “tweet”] # Change “meow” to “moo”
```

Using the english explanation above, we can break this down: 
“First need to identify the element you want to change”
We want to change “meow” in my_list. 

“Find where the element is within your object” 
“meow” is at index 1. 

“Assign at that position in the list to the desired value”
```python
    my_list[1] = “moo”
```
</details>

2. Write the general formula of how you call a method on an object using the following. You might not need to use all and can use any multiple times: `<method_name>`, `()`, `<object_variable>`, `.` , `<arg>`. Give examples. 

<details>
<summary>SHOW SOLUTIONS</summary>
`<object_variable>`.`<method_name>`(`<arg>`)

For more arguments, you'd have

`<object_variable>`.`<method_name>`(`<arg>, <arg>`)

And so on.


```python
    # example
    my_list.pop(0)
    my_list.append(“Hello”)
```
</details>

3. Give two ways of instantiating an empty list. What are the components you need and what does each part do? Give an example for each. Your explanation should include the words 'function', 'constructor', 'variable', 'instantiate', 'assign', and 'reference'. 

<details>
<summary>SHOW SOLUTIONS</summary>
Two ways of instantiating an empty list:

- *Using the list constructor:*
   The `list()` function is a constructor that instantiates an empty list object. The constructor belongs to the `List` class. The constructor doesn't take any arguments for creating an empty list. You assign the result of this function to a variable, which will reference the newly created empty list.

   Example:
   ```python
   empty_list = list()
   ```
   - *Components:*
     - `list()`: The constructor function that creates a new list object.
     - `empty_list`: A variable that is assigned the reference to the new list object created by the `list()` constructor.

- *Using square brackets literal:*
   You can instantiate an empty list using a pair of square brackets `[]`. This directly creates and instantiates a new empty list object, which you then assign to a variable.

   Example:
   ```python
   empty_list = []
   ```
   - **Components:**
     - `[]`: This is shorthand syntax for creating and instantiating an empty list object.
     - `empty_list`: A variable that is assigned the reference to the newly instantiated empty list.
</details>

4. For the following code snippet: 

```python
    # code snippet
    names[0]
```

Explain what each component of the code means (i.e. what is `names`? What is `names[0]` refering to? Is this a value or a reference?) In your explanation include the words 'reference', 'list', 'object', 'variable', 'value', 'name', 'index', and 'zeroth'. Prove your answer using a memory diagram. Your explanation of your proof should include the words 'id number', 'variable', 'index', 'element', 'value' and 'reference'. 

<details>
<summary>SHOW SOLUTIONS</summary>
Explanation of `names[0]`:

- `names` is a variable. Variables store references to objects in memory, and in this case, `names` is a variable that references a list object. The name of this variable serves as a pointer to the list object.
- `names[0]`: Here, `names` refers to the list object, and the `[0]` is an index that specifies the position of the element you want to access. The `0` is the zeroth index of the list, which refers to the first element in the list.
- *Is this a value or a reference?* The expression `names[0]` retrieves the value stored at the zeroth index of the list. Although `names` holds a reference to the entire list object, `names[0]` directly returns the value located at that index.
</details>

5. How do you know when you are indexing versus instantiating a list as both use square brackets?

<details>
<summary>SHOW SOLUTIONS</summary>
To differentiate between creating a list and indexing a list when both use square brackets [], focus on how the brackets are used.

When creating a list, square brackets either contain comma-separated values or are empty. They are typically part of an assignment to a variable. For example, `my_list = []` creates an empty list, `while my_list = [1, 2, 3]` creates a list with values. The key difference is that you're using the brackets to define the contents of a new list.

In contrast, when indexing a list, square brackets are used *after a variable* that *references a list*, containing an index to access or modify a specific element. For instance, `first_item = my_list[0]` retrieves the first element, and `my_list[2] = 10` modifies the third element. In this case, the brackets indicate you're accessing a position within an existing list, rather than creating one.

In short, if square brackets are part of an assignment and define elements, you're creating a list. If they're used after a list variable with a number inside, you're indexing a list.

To prove the difference between *creating a list* and *indexing a list*, let’s use a memory diagram and walk through the steps. First let's instantiate the list with some elements. The type of these elements does not matter or the amount, as long as we have one element for the example.

```python
    # example list
    my_list: list[int] = [1]
```

- *List creation*: When this code runs, a list object `[1, 2, 3]` is created in heap memory. To bind, or reference this list object, the `my_list` variable, stored in the Globals frame of the Stack will hold a value. This value is a reference to the list object which we denote by an id number. This id number is a unique identifier in memory.

- *Variable assignment*: The variable `my_list` holds a *reference* to this list object, meaning that `my_list` points to the memory location of the list. It does not hold the object or the elements in the object.
- *Pseudo-Memory diagram*:
   - `my_list` → list[int] object `[1, 2, 3]` (id: 0)
     - *Index 0*: Element `1`
     - *Index 1*: Element `2`
     - *Index 2*: Element `3`

Here, the `my_list` *variable* holds a *reference* to the list object, and each *element* in the list is assigned an index value to mark it's position within the list object. 

</details>

## Conceptual Questions

6. Identify the arguments that pop() and append() take in these examples. Explain what they mean/what the methods will do with them:
```python
    my_list.pop(6)
    my_list.append(9)
```

<details>
<summary>SHOW SOLUTIONS</summary>
 For my_list.pop(6), my_list is the first argument and 6 is the second argument. my_list as the first argument of pop() means that the method will be performing a removal of an element on that list. 6 as the second argument of pop() means that the method will remove the value at the 6th index. 

For my_list.append(9), my_list is the first argument and 9 is the second argument. my_list as the first argument of append() means that the method will be adding an element to the end of that list. 9 as the second argument of append() means that the method will add the value 9. 

The pop() method and the append() method in Python lists work differently and have different requirements for their arguments.

The pop() method removes an element from a list based on its index. It takes an integer as an argument, which specifies the position of the element you want to remove. This is important because when a list contains multiple identical elements, pop() needs to know the exact location of the element you wish to remove. If pop() accepted a value instead of an index, it could potentially remove all instances of that value, which might not be the desired behavior.

Example:

```python
    fruits = ['apple', 'banana', 'cherry', 'banana']

    # Removes the element at index 1 ('banana')
    removed_element = fruits.pop(1)

    print(removed_element)  # Output: banana
    print(fruits)           # Output: ['apple', 'cherry', 'banana']
```

Why does it make sense to use an index?
By using an index, you can precisely control which element is removed, even if the list contains duplicate values. This ensures that only the element at the specified position is affected.

If pop() were to take a value instead of an index, it could introduce ambiguity in cases where multiple elements have the same value. Using an index eliminates this uncertainty.

Memory Tip: You can remember that .pop() requires an index by asking yourself, "How does .pop() know which element to remove?" The answer is that it uses the index you provide. If you call .pop() without an argument, it defaults to removing the last element in the list.
append(value): This method adds a new element to the end of the list. It takes a single argument, which is the actual value to be added. Since .append() always adds the element to the end of the list, providing an index doesn't make sense.

Memory Tip: You can remember that .append() does not require an index by thinking, "Where does .append() add the element?" The answer is always at the end, so you only need to specify the value itself.

</details>

## Lists in loops
7. For the following lists: 

```python
    x: list[int] = [9, -1, 8, 5]
    y: list[str] = [“cat”, “dog”, “turtle”, “elephant”, “fish”]
    z: list[str] = [“z”]
```

7a. Iterate through the lists and print out every element using a while loop. 



7b. Iterate through the lists and print out every element using a for loop. 



7c. Iterate through the lists and print out every element using a for.. in range() loop. 

<details>
<summary>SHOW SOLUTIONS</summary>
```python
    """
    Iterate through the lists and print out every element using a while loop. 
    Iterate through the lists and print out every element using a for loop. 
    Iterate through the lists and print out every element using a for.. in range() loop.
    """

    # TODO: While loops
    # List x
    x = [9, -1, 8, 5]
    i = 0
    while i < len(x):
        print(x[i])
        i += 1

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    i = 0
    while i < len(y):
        print(y[i])
        i += 1

    # List z
    z = ["z"]
    i = 0
    while i < len(z):
        print(z[i])
        i += 1


    # TODO: for loops
    # List x
    x = [9, -1, 8, 5]
    for element in x:
        print(element)

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    for element in y:
        print(element)

    # List z
    z = ["z"]
    for element in z:
        print(element)
    

    # TODO: for... in... range() loops
    # List x
    x = [9, -1, 8, 5]
    for i in range(0, len(x)):
        print(x[i])

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    for i in range(0, len(y)):
        print(y[i])

    # List z
    z = ["z"]
    for i in range(0, len(z)):
        print(z[i])
```
</details>

<!-- 7d. Compare and contrast the difference between the different types of loops. 

<details>
<summary>SHOW SOLUTIONS</summary>

</details>

7e. Modify your solutions for the above by also printing out the index values. You should not instantiate new variables in order to do this or use any built-in functions that we have not learned, only add a print statement and use the existing variables. 

<details>
<summary>SHOW SOLUTIONS</summary>
```python
    """
    Modify your solutions for the above by also printing out the index values. 
    You should not instantiate new variables in order to do this or use any 
    built-in functions that we have not learned, only add a print statement and use the existing variables. 
    """

    # TODO: While loops
    # List x
    x = [9, -1, 8, 5]
    i = 0
    while i < len(x):
        print(f"Index {i}: {x[i]}")
        i += 1

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    i = 0
    while i < len(y):
        print(f"Index {i}: {y[i]}")
        i += 1

    # List z
    z = ["z"]
    i = 0
    while i < len(z):
        print(f"Index {i}: {z[i]}")
        i += 1

    # OR...

    # List x
    x = [9, -1, 8, 5]
    i = 0
    while i < len(x):
        print(i)
        print(x[i])
        i += 1

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    i = 0
    while i < len(y):
        print(i)
        print(y[i])
        i += 1

    # List z
    z = ["z"]
    i = 0
    while i < len(z):
        print(i)
        print(x[i])
        i += 1

    # TODO: for... in... range() loops
    # List x
    x = [9, -1, 8, 5]
    for i in range(0, len(x)):
        print(f"Index {i}: {x[i]}")

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    for i in range(0, len(y)):
        print(f"Index {i}: {y[i]}")

    # List z
    z = ["z"]
    for i in range(0, len(z)):
        print(f"Index {i}: {z[i]}")

    # OR...

    x = [9, -1, 8, 5]
    for i in range(0, len(x)):
        print(i)
        print(x[i])

    # List y
    y = ["cat", "dog", "turtle", "elephant"]
    for i in range(0, len(y)):
        print(i)
        print(y[i])

    # List z
    z = ["z"]
    for i in range(0, len(z)):
        print(i)
        print(z[i])
```
</details>

7f. Which loops are you able to do this for? What does this tell you about these loops? Consider the benefits between one loop over another. 

<details>
<summary>SHOW SOLUTIONS</summary>

</details>

# Solutions

## List General Questions





3. 

4. 

5. 

## Conceptual Questions

6.

## Lists in loops

7 - 9. Please refer to the code below: 



10. *`While` Loops:*
Structure: The `while` loop continues as long as a specified condition is true.
Control: Requires manual control of loop variables, such as initialization and incrementing the index.

*`For` Loops:*
Structure: The `for` loop iterates directly over the elements of the list.
Usage: Ideal when you need to access each element without caring about the index.
Control: Provides a direct way to iterate over iterable objects like lists without needing an index.

*`For.. in Range()` Loop:*
Structure: Uses an index-based approach, iterating over a range object (set of integer numbers).

`While` loops and `for...in range()` loops both iterate over sequences, but they handle indexing differently. In a `while` loop, you need to manually create and update an index variable to manage iteration. In contrast, a `for...in range()` loop automatically handles the index (by the nature of a `for` loop), simplifying the code by managing the variable for you. This makes `for...in range()` loops more concise and less error-prone when you need straightforward index-based iteration.

11. Please refer to the code below: 



12. The `while` loops and `for … in range()` loops. This again reveals how closely similar these two loops are. Depending on the situation, if you wanted to keep track of index values you would use either a `for … range()` loop or a `while` loop. If you did not care for keeping track of these values then you would most likely lean towards using a for loop as it directly iterates over the elements of the list.  -->