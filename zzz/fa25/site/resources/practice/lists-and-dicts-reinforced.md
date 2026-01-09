---
title: Lists, Dictionaries, and Loops Reinforcement Questions
author:
- Viktorya Hunanyan
- Mitchell Anderson
page: lessons
template: overview
---


## Extra Practice (Lists, Dictionaries, `for` loops)

1. The following questions will refer to the list below:
    ```python
        my_list: list[int] = list()
    ```
    1.1. Write line(s) of code that would add the number `8`, `0`, `3`, and `-1` to the list. 

    1.2. Write line(s) of code that removes `3` from the list.

    1.3. Write line(s) of code that assigns the variable `dog` to the element at the second index.

    1.4. Write line(s) of code that prints the amount of items in the list. 

    1.5. Change the value `8` to `0`. 

    1.6. We now have a function, `sum` that adds the elements of my_list and returns this amount. Write a line of code that instantiates a `list[int]` with the first value returned from calling `sum` on `my_list`. 



2. The following questions will refer to the dictionary below:

    ```python
        my_dict: dict[int, str] = {}
    ```

    2.1. Write line(s) of code that would add the following key-value pairs to the dictionary: 
    - `8: 'eight'`
    - `0: 'zero'`
    - `3: 'three'`
    - `-1: 'negative one'`

    2.2. Write line(s) of code that removes value `three`.

    2.3. Write line(s) of code that assign the value associated with the key `0` in `my_dict` to a variable called `cat`.

    2.4. Write line(s) of code that print the number of keys in `my_dict`.

    2.5. Write line(s) of code that print the number of values in `my_dict`.

    2.6. Change the value associated with the key `8` to `'zero'`.

    2.7. Suppose we have a function `sum_dict_keys` that sums the keys of `my_dict` and returns this amount. Write a line of code that instantiates a `dict[str: int]` containing a single value, which is the result of calling `sum_dict_keys(my_dict)` and a key of "returned_amount".



3. The following questions will refer to the dictionary below:

    ```python
        my_dict: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}
    ```

    3.1. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(my_dict[x])
    ```
    (a) `dog, cat, mouse, bird, whale`

    (b) `dog, cat, mouse, bird`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2, 3, 4`

    3.2. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(x)
    ```
    (a) `0, 1, 2, 3, 4`

    (b) `dog, cat, mouse, bird, whale`

    (c) `IndexOutOfRange`

    (d) `1, 2, 3, 4`

    3.2. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(my_dict[x])
    ```
    (a) `dog, cat, mouse, bird, whale`

    (b) `dog, cat, mouse, bird`

    (c) `IndexOutOfRange`

    (d) `0, 1, 2, 3, 4`

    3.3. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(x)
    ```
    (a) `0, 1, 2, 3, 4`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `IndexOutOfRange`
    
    (d) `1, 2, 3, 4`

    3.4. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(x)
            x += 1
    ```
    (a) `0, 1, 2, 3, 4`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `IndexOutOfRange`
    
    (d) `1, 2, 3, 4, 5`

    3.5. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(my_dict[x])
            x += 1
    ```
    (a) `dog, cat, mouse, bird, whale`
    
    (b) `dog, cat, mouse, bird`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2, 3, 4`



4. The following questions will refer to the dictionary below:

    ```python
    my_dict: dict[int, str] = {8: "dog", 1: "cat", 10: "mouse", 15: "bird", 0: "whale"}
    ```

    4.1. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(my_dict[x])
    ```
    (a) `whale, cat, KeyError`
    
    (b) `IndexOutOfRange`
    
    (c) `dog, cat, mouse`
    
    (d) `bird, whale`

    4.2. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(x)
    ```
    (a) `0, 1, 2, 3, 4`
    
    (b) `0, 1, 2`
    
    (c) `IndexOutOfRange`
    
    (d) `1, 2, 3, 4`

    4.3. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(my_dict[x])
    ```
    (a) `dog, cat, mouse, bird, whale`
    
    (b) `whale, cat, mouse, bird, dog`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2, 3, 4`

    4.4. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(x)
    ```
    (a) `8, 1, 10, 15, 0`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2, 3, 4`

    4.5. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(x)
            x += 1
    ```
    (a) `0, 1, 2, 3, 4`
    
    (b) `1, 2, 3, 4`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2`

    4.6. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(my_dict[x])
            x += 1
    ```
    (a) `whale, cat, KeyError`
    
    (b) `IndexOutOfRange`
    
    (c) `dog, cat, mouse`
    
    (d) `bird, whale`



5. The following questions will refer to the dictionary below:

    ```python
    my_dict: dict[str, str] = {"cat": "dog", "dog": "cat", "bird": "mouse", "mouse": "bird", "while": "whale"}
    ```

    5.1. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(my_dict[x])
    ```

    (a) `IndexOutOfRange`
    
    (b) `dog, cat, mouse`
    
    (c) `KeyError`
    
    (d) `bird, whale`

    5.2. What will print from the following code: 
    ```python
        for x in range(0, len(my_dict)): 
            print(x)
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `1, 2, 3, 4`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2`


    5.3. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(my_dict[x])
    ```
    (a) `dog, cat, mouse, bird, whale`
    
    (b) `dog, cat, mouse, bird`
    
    (c) `IndexOutOfRange`
    
    (d) `cat, dog, bird`

    5.4. What will print from the following code: 
    ```python
        for x in my_dict: 
            print(x)
    ```
    (a) `cat, dog, bird, mouse, while`
    
    (b) `dog, cat, mouse, bird`
    
    (c) `IndexOutOfRange`
    
    (d) `0, 1, 2, 3, 4`

    5.5. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(x)
            x += 1
    ```
    (a) `0, 1, 2, 3, 4`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `IndexOutOfRange`
    
    (d) `1, 2, 3, 4`

    5.6. What will print from the following code: 
    ```python
        x: int = 0
        while x < len(my_dict): 
            print(my_dict[x])
            x += 1
    ```
    (a) `IndexOutOfRange`
    
    (b) `dog, cat, mouse`
    
    (c) `KeyError`
    
    (d) `bird, whale`

<details>
<summary>SHOW SOLUTIONS</summary>

1. List Manipulations

```python
my_list: list[int] = list()

# 1.1. Add the numbers 8, 0, 3, and -1 to the list.
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)

# 1.2. Remove the number 3 from the list.
my_list.pop(2)

# 1.3. Assign the element at the second index to a variable named 'dog'.
dog = my_list[2]

# 1.4. Print the number of items in the list.
print(len(my_list))

# 1.5. Change the value 8 to 0.
my_list[0] = 0

# 1.6. Instantiate a list[int] with the first value returned from calling sum on my_list.
summed_list = [sum(my_list)]
```



2. Dictionary Manipulations

```python
my_dict: dict[int, str] = {}

# 2.1. Add key-value pairs to the dictionary.
my_dict[8] = 'eight'
my_dict[0] = 'zero'
my_dict[3] = 'three'
my_dict[-1] = 'negative one'

# 2.2. Remove the key-value pair where the value is 'three'.
my_dict.pop(3) # recall that pop takes an index and in the case of dictionaries or indicies are essentially our keys

# 2.3. Assign the value associated with the key 0 to a variable called 'cat'.
cat = my_dict[0]

# 2.4. Print the number of keys in the dictionary.
print(len(my_dict))

# 2.5. Print the number of values in the dictionary.
print(len(my_dict))

# 2.6. Change the value associated with the key 8 to 'zero'.
my_dict[8] = 'zero'

# 2.7. Instantiate a dict[str, int] with the key 'returned_amount' and the value from sum_dict_keys(my_dict).
result_dict = {'returned_amount': sum_dict_keys(my_dict)}
```



3. Dictionary Looping and Output
- 3.1: Output = (a) dog, cat, mouse, bird, whale
- 3.2: Output = (a) 0, 1, 2, 3, 4
- 3.3: Output = (a) dog, cat, mouse, bird, whale
- 3.4: Output = (a) 0, 1, 2, 3, 4
- 3.5: Output = (a) 0, 1, 2, 3, 4
- 3.6: Output = (a) dog, cat, mouse, bird, whale



4. Looping with Different Key Values
- 4.1: Output = (a) whale, cat, KeyError
- 4.2: Output = (a) 0, 1, 2, 3, 4
- 4.3: Output = (a) dog, cat, mouse, bird, whale
- 4.4: Output = (a) 0, 1, 8, 10, 15
- 4.5: Output = (a) 0, 1, 2, 3, 4
- 4.6: Output = (a) whale, cat, KeyError



5. Dictionary with String Keys
- 5.1: Output = (c) KeyError
- 5.2: Output = (a) 0, 1, 2, 3, 4
- 5.3: Output = (a) dog, cat, mouse, bird, whale
- 5.4: Output = (a) cat, dog, bird, mouse, while
- 5.5: Output = (a) 0, 1, 2, 3, 4
- 5.6: Output = (c) KeyError



</details>