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


# Function Writing

6. Write a function that will take a `list[str]` and returns a `list[int]` of the size of each string in the input list. 
7. Write a function that will take a `list[str]` and returns the sum of the lengths of all the strings. 
8. Write a function that will take a `list[str]` and mutates the list by adding a exclamation point to each string in the input list. Your function should not return anything. 
9. Write a function that takes a `str` input and returns a list with each element being a single character in the string input. 
10. Write a function that takes a `int` input and creates a list of the size of your input integer. Every element should be equal to their index value. When the function is called and finishes executing and the frame goes out of scope, the new list should still be avaiable for reference to a Global varibale. 
11. Write a function that take a `list[float]`, an `int`, and a `float` and inserts the `float` into the `list[float]` at the index specified by the `int` passed to the function. 
12. Write a function that takes a `list[int]` and returns a new list with only the even numbers.
13. Write a function that takes a `list[str]` and returns a new list with only the strings that contain the letter 'a'.
14. Write a function that takes a `list[int]` and returns the largest number.
15. Write a function that takes a `str` input and counts how many times of each vowel appears in the string and returns this as a summary in a dict[str, int].
16. Write a function that takes two `list[int]` and returns a new list with the elements that appear in both lists.
17. Write a function that takes a `list[float]` and returns the average of the list, ignoring any negative numbers.
18. Write a function that takes a `list[str]` and returns a new list with the strings sorted by length in descending order.
19. Write a function that takes a `list[str]` and returns a dictionary where the keys are the strings and the values are the lengths of each string.
20. Write a function that takes a `str` and returns a dict[str, int] that counts the frequency of each character in the string.
21. Write a function that takes a `list[str]` and returns a dictionary where the keys are the first letters of each string, and the values are lists of strings that start with that letter.
22. Write a function that takes a `dict[str, int]` and returns a list[str] of all the keys that have even values.
23. Write a function that takes a `dict[str, int]` and returns the key with the largest value.
24. Write a function that takes two `dict[str, float]` and merges them into one. If both dictionaries have the same key, sum their values.
25. Write a function that takes a `dict[str, list[float]]` where the keys are strings and the values are lists. The function should return a new dictionary where the keys are the original keys, but the values are the lengths of each list.
26. Write a function that takes a `dict[float, int]` and returns a new dictionary with the keys and values swapped.
27. Write a function that takes a dictionary of students' names as keys and their test scores as values, then returns a new `dict[str, int]` with only students who scored above an 85.


# Solutions
1. List Manipulations

```python
my_list: list[int] = list()

# 1a. Add the numbers 8, 0, 3, and -1 to the list.
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)

# 1b. Remove the number 3 from the list.
my_list.pop(2)

# 1c. Assign the element at the second index to a variable named 'dog'.
dog = my_list[2]

# 1d. Print the number of items in the list.
print(len(my_list))

# 1e. Change the value 8 to 0.
my_list[0] = 0

# 1f. Instantiate a list[int] with the first value returned from calling sum on my_list.
summed_list = [sum(my_list)]
```

---

2. Dictionary Manipulations

```python
my_dict: dict[int, str] = {}

# 2a. Add key-value pairs to the dictionary.
my_dict[8] = 'eight'
my_dict[0] = 'zero'
my_dict[3] = 'three'
my_dict[-1] = 'negative one'

# 2b. Remove the key-value pair where the value is 'three'.
my_dict.pop(3) # recall that pop takes an index and in the case of dictionaries or indicies are essentially our keys

# 2c. Assign the value associated with the key 0 to a variable called 'cat'.
cat = my_dict[0]

# 2d. Print the number of keys in the dictionary.
print(len(my_dict))

# 2e. Print the number of values in the dictionary.
print(len(my_dict))

# 2f. Change the value associated with the key 8 to 'zero'.
my_dict[8] = 'zero'

# 2g. Instantiate a dict[str, int] with the key 'returned_amount' and the value from sum_dict_keys(my_dict).
result_dict = {'returned_amount': sum_dict_keys(my_dict)}
```

---

3. Dictionary Looping and Output
- 3a: Output = (a) dog, cat, mouse, bird, whale
- 3b: Output = (a) 0, 1, 2, 3, 4
- 3c: Output = (a) dog, cat, mouse, bird, whale
- 3d: Output = (a) 0, 1, 2, 3, 4
- 3e: Output = (a) 0, 1, 2, 3, 4
- 3f: Output = (a) dog, cat, mouse, bird, whale

---

4. Looping with Different Key Values
- 4a: Output = (b) IndexOutOfRange
- 4b: Output = (a) 0, 1, 2, 3, 4
- 4c: Output = (b) whale, cat, mouse, bird, dog
- 4d: Output = (a) 0, 1, 8, 10, 15
- 4e: Output = (a) 0, 1, 2, 3, 4
- 4f: Output = (b) IndexOutOfRange

---

5. Dictionary with String Keys
- 5a: Output = (a) IndexOutOfRange
- 5b: Output = (a) 0, 1, 2, 3, 4
- 5c: Output = (a) dog, cat, mouse, bird, whale
- 5d: Output = (a) cat, dog, bird, mouse, while
- 5e: Output = (a) 0, 1, 2, 3, 4
- 5f: Output = (a) IndexOutOfRange

6 - 27. *Solutions coming soon.* 
=======
11. Write a function that take a `list[float]`, an `int`, and a `float` and inserts the `float` into the `list[float]` at the index specified by the `int` passed to the function. 
