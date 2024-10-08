---
title: Lists, Dictionaries, and Loops Reinforcement Questions
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

These questions are meant to test your understanding from [Lists](/resources/practice/lists.html), [Dictionaries](/resources/practice/dicts.html), [for Loops](/resources/practice/for-loops.html). You should complete those before doing the questions below. 

# Questions

1. The following questions will refer to the list below:
```python
my_list: list[int] = list()
```
- 1a. Write line(s) of code that would add the number `8`, `0`, `3`, and `-1` to the list. 
- 1b. Write line(s) of code that removes `3` from the list.
- 1c. Write line(s) of code that assigns the variable `dog` to the element at the second index.
- 1d. Write line(s) of code that prints the amount of items in the list. 
- 1e. Change the value `8` to `0`. 
- 1f. We now have a function, `sum` that adds the elements of my_list and returns this amount. Write a line of code that instantiates a `list[int]` with the first value returned from calling `sum` on `my_list`. 

---

2. The following questions will refer to the dictionary below:

```python
my_dict: dict[int, str] = {}
```

- 2a. Write line(s) of code that would add the following key-value pairs to the dictionary: 
  - `8: 'eight'`
  - `0: 'zero'`
  - `3: 'three'`
  - `-1: 'negative one'`

- 2b. Write line(s) of code that removes value `three`.
- 2c. Write line(s) of code that assign the value associated with the key `0` in `my_dict` to a variable called `cat`.
- 2d. Write line(s) of code that print the number of keys in `my_dict`.
- 2e. Write line(s) of code that print the number of values in `my_dict`.
- 2f. Change the value associated with the key `8` to `'zero'`.
- 2g. Suppose we have a function `sum_dict_keys` that sums the keys of `my_dict` and returns this amount. Write a line of code that instantiates a `dict[str: int]` containing a single value, which is the result of calling `sum_dict_keys(my_dict)` and a key of "returned_amount".

---

3. The following questions will refer to the dictionary below:

```python
my_dict: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}
```

- 3a. What will print from the following code: 
```python
    for x in range(0, len(my_dict)): 
        print(my_dict[x])
```
(a) `dog, cat, mouse, bird, whale`
(b) `dog, cat, mouse, bird`
(c) `IndexOutOfRange`
(d) `0, 1, 2, 3, 4`

- 3b. What will print from the following code: 
```python
    for x in range(0, len(my_dict)): 
        print(x)
```
(a) `0, 1, 2, 3, 4`
(b) `dog, cat, mouse, bird, whale`
(c) `IndexOutOfRange`
(d) `1, 2, 3, 4`

- 3c. What will print from the following code: 
```python
    for x in my_dict: 
        print(my_dict[x])
```
(a) `dog, cat, mouse, bird, whale`
(b) `dog, cat, mouse, bird`
(c) `IndexOutOfRange`
(d) `0, 1, 2, 3, 4`

- 3d. What will print from the following code: 
```python
for x in my_dict: 
    print(x)
```
(a) `0, 1, 2, 3, 4`
(b) `dog, cat, mouse, bird, whale`
(c) `IndexOutOfRange`
(d) `1, 2, 3, 4`

- 3e. What will print from the following code: 
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

- 3f. What will print from the following code: 
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

---

4. The following questions will refer to the dictionary below:

```python
my_dict: dict[int, str] = {8: "dog", 1: "cat", 10: "mouse", 15: "bird", 0: "whale"}
```

- 4a. What will print from the following code: 
```python
for x in range(0, len(my_dict)): 
    print(my_dict[x])
```
(a) `whale, cat`
(b) `IndexOutOfRange`
(c) `dog, cat, mouse`
(d) `bird, whale`

- 4b. What will print from the following code: 
```python
for x in range(0, len(my_dict)): 
    print(x)
```
(a) `0, 1, 2, 3, 4`
(b) `0, 1, 2`
(c) `IndexOutOfRange`
(d) `1, 2, 3, 4`

- 4c. What will print from the following code: 
```python
for x in my_dict: 
    print(my_dict[x])
```
(a) `dog, cat, mouse, bird, whale`
(b) `whale, cat, mouse, bird, dog`
(c) `IndexOutOfRange`
(d) `0, 1, 2, 3, 4`

- 4d. What will print from the following code: 
```python
for x in my_dict: 
    print(x)
```
(a) `0, 1, 8, 10, 15`
(b) `dog, cat, mouse, bird, whale`
(c) `IndexOutOfRange`
(d) `0, 1, 2, 3, 4`

- 4e. What will print from the following code: 
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

- 4f. What will print from the following code: 
```python
x: int = 0
while x < len(my_dict): 
    print(my_dict[x])
    x += 1
```
(a) `whale, cat`
(b) `IndexOutOfRange`
(c) `dog, cat, mouse`
(d) `bird, whale`

---

5. The following questions will refer to the dictionary below:

```python
my_dict: dict[str, str] = {"cat": "dog", "dog": "cat", "bird": "mouse", "mouse": "bird", "while": "whale"}
```

- 5a. What will print from the following code: 
```python
for x in range(0, len(my_dict)): 
    print(my_dict[x])
```

(a) `IndexOutOfRange`
(b) `dog, cat, mouse`
(c) `TypeError`
(d) `bird, whale`

- 5b. What will print from the following code: 
```python
for x in range(0, len(my_dict)): 
    print(x)
```

(a) `0, 1, 2, 3, 4`
(b) `1, 2, 3, 4`
(c) `IndexOutOfRange`
(d) `0, 1, 2`


- 5c. What will print from the following code: 
```python
for x in my_dict: 
    print(my_dict[x])
```
(a) `dog, cat, mouse, bird, whale`
(b) `dog, cat, mouse, bird`
(c) `IndexOutOfRange`
(d) `cat, dog, bird`

- 5d. What will print from the following code: 
```python
for x in my_dict: 
    print(x)
```
(a) `cat, dog, bird, mouse, while`
(b) `dog, cat, mouse, bird`
(c) `IndexOutOfRange`
(d) `0, 1, 2, 3, 4`

- 5e. What will print from the following code: 
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

- 5f. What will print from the following code: 
```python
x: int = 0
while x < len(my_dict): 
    print(my_dict[x])
    x += 1
```
(a) `IndexOutOfRange`
(b) `dog, cat, mouse`
(c) `TypeError`
(d) `bird, whale`


