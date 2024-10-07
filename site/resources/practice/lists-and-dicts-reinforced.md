---
title: Lists and Dictionaries Reinforcement Questions
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Questions

## List General Questions
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

2. The following questions will refer to the dictionary below:
```python
my_dict: dict[int: str] = {}
```
Here’s a revised version of your prompt that correctly references the dictionary rather than a list, and includes fixes to clarify the steps:

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
