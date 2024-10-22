---
title: Lists, Dictionaries, and Loops Reinforcement Questions
author:
- Viktorya Hunanyan
- Mitchell Anderson
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
- 4c: Output = (a) dog, cat, mouse, bird, whale
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

---

6. Solution below: 

```
def size_of_strings(strings: list[str]) -> list[int]:
    """Return a list of the size of each string in the input list."""
    result: list[int] = []
    for x in range(0, len(strings)):
        result.append(len(strings[x]))
    return result

# OR 

def size_of_strings(strings: list[str]) -> list[int]:
    """Return a list of the size of each string in the input list."""
    result: list[int] = []
    i = 0  # Initialize a counter for the while loop
    
    while i < len(strings):  # Loop until the end of the list
        string_length = 0  # Manually count the length of the string
        j = 0  # Initialize a second counter to measure string length
        
        while j < len(strings[i]):  # Measure the length of each string
            string_length += 1
            j += 1
        
        result.append(string_length)  # Append the calculated length to result
        i += 1  # Move to the next string in the list
    
    return result
```

---

7. Solution below: 

```
def sum_of_string_lengths(strings: list[str]) -> int:
    """Return the sum of the lengths of all strings in the list."""
    total_length: int = 0
    for string in strings:
        total_length += len(string)
    return total_length

# OR

def sum_of_string_lengths(strings: list[str]) -> int:
    """Return the sum of the lengths of all strings in the list."""
    total_length = 0
    i = 0
    while i < len(strings):
        total_length += len(strings[i])
        i += 1
    return total_length
```

---

8. Solution below:

```
def add_exclamation(strings: list[str]) -> None:
    """Add an exclamation point to each string in the input list."""
    for i in range(len(strings)):
        strings[i] += '!'
    
# OR

def add_exclamation(strings: list[str]) -> None:
    """Add an exclamation point to each string in the input list."""
    i = 0
    while i < len(strings):
        strings[i] += '!'
        i += 1
```

---

9. Solution below: 

```
def string_to_characters(input_string: str) -> list[str]:
    """Return a list where each element is a character from the input string."""
    result: list[str] = []
    for char in input_string:
        result.append(char)
    return result

# OR

def string_to_list(s: str) -> list[str]:
    """Convert a string into a list where each element is a character."""
    result: list[str] = []
    i = 0
    while i < len(s):
        result.append(s[i])
        i += 1
    return result
```

---

10. Solution below: 

```
def count_str(size: int) -> list[int]:
    """Create a list of the size of the input integer and assign it to a global variable."""
    result: list[int] = []
    for x in range(0, size):
        result.append(x)
    return result
size_list: list[int] = count_str(5)

# OR

def count_str(size: int) -> list[int]:
    """Create a list of the size of the input integer using a while loop."""
    result: list[int] = []
    x: int = 0
    
    while x < size:
        result.append(x)
        x += 1
        
    return result

size_list: list[int] = count_str(5)
```

---

11. Solution below: 

```
def insert_float(lst: list[float], index: int, num: float) -> list[float]:
    """Insert a float into the list at the specified index without using the insert function."""
    result: list[float] = []
    
    for x in range(0, len(lst)):
        if x == index:
            result.append(num)  # Add the new float at the specified index
            
        result.append(lst[x])  # Add the existing float
    
    # If the index is at the end, append the new float after the last element
    if index >= len(lst):
        result.append(num)

    return result

# OR

def insert_float(lst: list[float], index: int, num: float) -> list[float]:
    """Insert a float into the list at the specified index using a while loop."""
    result: list[float] = []
    x: int = 0
    
    while x < len(lst):
        if x == index:
            result.append(num)  # Add the new float at the specified index
        
        result.append(lst[x])  # Add the existing float
        x += 1  # Increment the index
    
    # If the index is at the end, append the new float after the last element
    if index >= len(lst):
        result.append(num)

    return result
```

---

12. Solution below: 

```
def only_evens(lst: list[int]) -> list[int]:
    """Return a new list with only the even numbers."""
    result: list[int] = []
    for x in range(0, len(lst)):
        if lst[x] % 2 == 0:
            result.append(lst[x])
    return result

# OR

def only_evens(lst: list[int]) -> list[int]:
    """Return a new list with only the even numbers using a while loop."""
    result: list[int] = []
    x: int = 0
    
    while x < len(lst):
        if lst[x] % 2 == 0:
            result.append(lst[x])  # Add even numbers to the result list
        x += 1  # Increment the index

    return result
```

---

13. Solution below: 

```
def only_a_strings(strings: list[str]) -> list[str]:
    """Return a new list with only the strings that contain the letter 'a' using a for loop."""
    result: list[str] = []
    
    for string in strings:
        if 'a' in string:  # Check if 'a' is in the current string
            result.append(string)

    return result

# OR

def only_a_strings(strings: list[str]) -> list[str]:
    """Return a new list with only the strings that contain the letter 'a'."""
    result: list[str] = []
    i: int = 0
    j: int = 0
    while i < len(strings):
        while j < len(strings[i]):
            if strings[i][j] == "a":
                result.append(strings[i])
            j += 1
        i += 1
    return result
```

---

14. Solution below: 

```
def largest_number(lst: list[int]) -> int:
    """Return the largest number in the input list."""
    result: int = lst[0]
    for x in range(0, len(lst)):
        if lst[x] > result:
            result = lst[x]
    return result

# OR

def largest_number(lst: list[int]) -> int:
    """Return the largest number in the input list using a while loop."""
    if len(lst) == 0:  # Handle empty list case
        raise ValueError("The list is empty")
    
    result: int = lst[0]
    x: int = 0
    
    while x < len(lst):
        if lst[x] > result:
            result = lst[x]
        x += 1  # Increment the index
    
    return result
```

---

15. Solution below: 

```
def count_vowels(string: str) -> dict[str, int]:
    """Return a dictionary with the count of each vowel in the input string."""
    result: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for x in range(0, len(string)):
        if string[x] in result:
            result[string[x]] += 1
    return result

# OR 

def count_vowels(string: str) -> dict[str, int]:
    """Return a dictionary with the count of each vowel in the input string using a while loop."""
    result: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    x: int = 0
    
    while x < len(string):
        if string[x] in result:
            result[string[x]] += 1
        x += 1  # Increment the index
    
    return result
```

---

16. Solution below: 

```
def same_nums(lst1: list[int], lst2: list[int]) -> list[int]:
    """Return a new list with the elements that appear in both lists."""
    result: list[int] = []
    for x in range(0, len(lst1)):
        for y in range(0, len(lst2)):
            if lst1[x] == lst2[y]:
                result.append(lst1[x])
    return result

# OR

def same_nums(lst1: list[int], lst2: list[int]) -> list[int]:
    """Return a new list with the elements that appear in both lists using while loops."""
    result: list[int] = []
    x: int = 0
    
    while x < len(lst1):
        y: int = 0
        found: bool = False  # To track if a match is found
        while y < len(lst2):
            if lst1[x] == lst2[y]:
                result.append(lst1[x])
                found = True  # Set found to True if a match is found
            y += 1  # Increment the inner index
        
        # Increment the outer index regardless of finding a match
        x += 1  
    
    return result
```

---

17. Solution below: 

```
def average_non_negative(lst: list[float]) -> float:
    """Return the average of the list, ignoring any negative numbers."""
    total: float = 0
    count: int = 0

    # Use a while loop to iterate through the list
    index: int = 0
    while index < len(lst):
        if lst[index] >= 0:  # Only consider non-negative numbers
            total += lst[index]
            count += 1  # Increment the count for valid numbers
        index += 1  # Move to the next element

    # Calculate and return the average
    if count > 0:  # Avoid division by zero
        return total / count
    return 0  # Return 0 if there are no non-negative numbers
```

---

18. Solution below: 

```
def sort_strings(strings: list[str]) -> list[str]:
    """Return a new list with the strings sorted by length in descending order."""
    result: list[str] = []
    while len(result) < len(strings):
        max_index = 0
        for i in range(1, len(strings)):
            if len(strings[i]) > len(strings[max_index]):
                max_index = i
        result.append(strings[max_index])
        strings[max_index] = ""

    return result

# OR 

def sort_strings(strings: list[str]) -> list[str]:
    """Return a new list with the strings sorted by length in descending order using while loops."""
    result: list[str] = []
    temp_strings: list[str] = []  # Initialize an empty list for manual copying
    
    # Manually copy the original list to temp_strings
    i: int = 0
    while i < len(strings):
        temp_strings.append(strings[i])
        i += 1  # Increment the index
    
    while len(result) < len(strings):
        max_index = 0
        j: int = 1
        
        while j < len(temp_strings):
            if len(temp_strings[j]) > len(temp_strings[max_index]):
                max_index = j
            j += 1  # Increment the inner index
        
        result.append(temp_strings[max_index])  # Append the longest string to result
        temp_strings[max_index] = ""  # Mark the string as used by replacing it with an empty string

    return result
```

---

19. Solution below: 

```
def strings_to_dict(strings: list[str]) -> dict[str, int]:
    """Return a dictionary where the keys are the strings and the values are the lengths of each string."""
    result: dict[str, int] = {}
    for x in range(0, len(strings)):
        result[strings[x]] = len(strings[x])
    return result

# OR

def strings_to_dict(strings: list[str]) -> dict[str, int]:
    """Return a dictionary where the keys are the strings and the values are the lengths of each string using a while loop."""
    result: dict[str, int] = {}
    x: int = 0
    
    while x < len(strings):
        result[strings[x]] = len(strings[x])  # Assign the string as key and its length as value
        x += 1  # Increment the index
    
    return result
```

---

20. Solution below: 

```
def count_chars(string: str) -> dict[str, int]:
    """Return a dictionary with the frequency of each character in the input string."""
    result: dict[str, int] = {}
    for x in range(0, len(string)):
        if string[x] in result:
            result[string[x]] += 1
        else:
            result[string[x]] = 1
    return result

# OR

def count_chars(string: str) -> dict[str, int]:
    """Return a dictionary with the frequency of each character in the input string using a while loop."""
    result: dict[str, int] = {}
    x: int = 0
    
    while x < len(string):
        if string[x] in result:
            result[string[x]] += 1  # Increment the count if the character already exists
        else:
            result[string[x]] = 1  # Initialize the count for the character
        x += 1  # Increment the index
    
    return result
```

---

21. Solution below: 

```
def group_strings_by_first_letter(strings: list[str]) -> dict[str, list[str]]:
    """Return a dictionary where the keys are the first letters and the values are lists of strings starting with that letter."""
    result: dict[str, list[str]] = {}

    # Use a while loop to iterate through the list of strings
    index: int = 0
    while index < len(strings):
        if strings[index]:  # Ensure the string is not empty
            first_letter: str = strings[index][0]  # Get the first letter

            # If the first letter is not in the result dictionary, add it with an empty list
            if first_letter not in result:
                result[first_letter] = []
            result[first_letter].append(strings[index])  # Add the string to the appropriate list
        index += 1  # Move to the next string

    return result

# OR

def find_first_letter(strings: list[str]) -> dict[str, list[str]]:
    """Return a dictionary with the first letter of each string as the key and a list of strings that start with that letter as the value."""
    result: dict[str, list[str]] = {}
    for x in range(0, len(strings)):
        if strings[x][0] in result:
            result[strings[x][0]].append(strings[x])
        else:
            result[strings[x][0]] = [strings[x]]
    return result
```

22. Solution below: 

```
def keys_with_even_values(d: dict[str, int]) -> list[str]:
    """Return a list of keys that have even values."""
    result: list[str] = [] 
    for key in d:
        if d[key] % 2 == 0:
            result.append(key)
    return result

# OR

def keys_with_even_values(d: dict[str, int]) -> list[str]:
    """Return a list of keys that have even values using a while loop."""
    result: list[str] = [] 
    keys: list[str] = []  # Initialize an empty list for keys
    x: int = 0

    # Manually collect keys from the dictionary
    for key in d:  # Use a for loop just to collect keys
        keys.append(key)

    while x < len(keys):
        if d[keys[x]] % 2 == 0:
            result.append(keys[x])  # Append the key if its value is even
        x += 1  # Increment the index
    
    return result
```

---

23. Solution below:

```
def key_with_largest_value(d: dict[str, int]) -> str:
    """Return the key with the largest value in the input dictionary."""
    largest_key: str = ""
    largest_value: int = 0

    # Use a for loop to iterate through the dictionary
    for key in d:
        if d[key] > largest_value:
            largest_value = d[key]  # Update largest value
            largest_key = key  # Update largest key

    return largest_key

# OR

def key_with_largest_value(d: dict[str, int]) -> str:
    """Return the key with the largest value in the input dictionary."""
    largest_key: str = ""
    largest_value: int = 0
    index: int = 0

    # Manually create a list of keys from the dictionary
    keys: list[str] = []
    
    # Populate keys manually
    while index < len(d):
        current_key = next(iter(d))  # Get the first key from the dictionary
        keys.append(current_key)  # Add the key to the list of keys
        d.pop(current_key)  # Remove the key from the dictionary to avoid duplicates
        index += 1

    # Use a while loop to find the key with the largest value
    x: int = 0  # Index for the keys
    while x < len(keys):
        key = keys[x]
        if key in d and d[key] > largest_value:
            largest_value = d[key]  # Update largest value
            largest_key = key  # Update largest key
        x += 1  # Increment the index

    return largest_key
```

---

24. Solution below: 

```
def merge_dicts(d1: dict[str, float], d2: dict[str, float]) -> dict[str, float]:
    """Merge two dictionaries into one, summing the values of common keys."""
    result: dict[str, float] = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result

# OR

def merge_dicts(d1: dict[str, float], d2: dict[str, float]) -> dict[str, float]:
    """Merge two dictionaries into one, summing the values of common keys using a while loop."""
    result: dict[str, float] = {}
    keys1: list[str] = []  # Manually create a list for keys in d1
    keys2: list[str] = []  # Manually create a list for keys in d2
    
    # Populate keys1 and keys2 manually
    for key in d1:
        keys1.append(key)
    for key in d2:
        keys2.append(key)

    x: int = 0  # Index for keys1
    # Use a while loop to add keys from d1 to the result
    while x < len(keys1):
        key = keys1[x]
        result[key] = d1[key]  # Add key and value from d1 to result
        x += 1  # Increment index

    y: int = 0  # Index for keys2
    # Use another while loop to process keys from d2
    while y < len(keys2):
        key = keys2[y]
        if key in result:
            result[key] += d2[key]  # Sum the values for common keys
        else:
            result[key] = d2[key]  # Add new keys and values to result
        y += 1  # Increment index

    return result
```

---

25. Solution below: 

```
def length_of_values(d: dict[str, list[float]]) -> dict[str, int]:
    """Return a dictionary with the lengths of the lists in the input dictionary."""
    result: dict[str, int] = {}
    for key in d:
        result[key] = len(d[key])
    return result
```

---

26. Solution below: 

```
def swap_keys_values(d: dict[float, int]) -> dict[int, float]:
    """Return a new dictionary with the keys and values swapped."""
    result: dict[int, float] = {}
    for key in d:
        result[d[key]] = key
    return result
```

---

27. Solution below: 

```
def find_above_85(d: dict[str, int]) -> dict[str, int]:
    """Return a new dictionary with only the students who scored above an 85."""
    result: dict[str, int] = {}
    for key in d:
        if d[key] > 85:
            result[key] = d[key]
    return result
```

