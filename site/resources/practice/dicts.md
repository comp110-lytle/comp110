---
title: Dictionary Conceptual Questions
author:
- Alyssa Lytle
- Viktorya Hunanyan
- Carmine Anderson-Falconi
page: lessons
template: overview
---

# Questions

## Conceptual
For the following, you must prove your answer to each question. Prove using either memory diagrams or code in VS code.

1. Dictionaries in Python can have duplicate keys. (T/F)
2. Dictionaries in Python can be nested, meaning a dictionary can contain another dictionary as a value. (T/F)

## Dictionary Practice

1. Create a new dictionary called `my_dictionary` with `str` keys and `float` values and initialize it as an empty dictionary.

2. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, access the *value* stored under key "Yall". 

3. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, increase the *value* stored under key "Yall" by 3.

4. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
remove the value "Alyssa", stored at key 100.

5. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
write a line of code to get the number of key/value pairs in the dictionary.

6. Using the following dictionary, `inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}`, add a new key-value pair `"markers": 15`.

7. Using the following dictionary, `prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}`, update the value of `"milk"` to `2.50`.

8. Using the dictionary `scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}`, print out all the keys in the dictionary.

9. Using the dictionary `scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}`, write a line of code that returns the sum of all the values (scores) in the dictionary. Assume that we have a written a `sum` function that will do this for us when passing in a `dict`. Store this value in a variable `total_score`. 

- 9a. Write the same line of code except using key-word arguments assuming that the only parameter in `sum` is called `inp_dict`. 

10. Using the dictionary `fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}`, iterate over the key-value pairs and print them in the format "key: value". 

11. Create a new dictionary by combining the two dictionaries. Store this new object by assiging it's reference to a variable called `combo_dict`:

```python
    first_dict: dict[str, int] = {"a": 1, "b": 2}
    second_dict: dict[str, int] = {"c": 3, "d": 4}
```


# Answers

## Conceptul Questions

1. False
2. True

# Syntax Solutions

1. `my_dictionary: dict[str, float] = {}` or `my_dictionary: dict[str, float] = dict()`

2. `msg["Yall"]`

3. `msg["Yall"] += 3` or `msg["Yall"] = 5`

4. `ids.pop(100)`

5. `len(ids)`

6. `inventory["markers"] = 15`

7. `prices["milk"] = 2.50`

8. Code below:

```
for x in scores:
    print(x)
```

9. `total_score = sum(scores)`

- 9a. `total_score = sum(inp_dict=scores)`

10. Code below: 

```python
for boo in fruit_count:
    ghost = fruit_count[boo]
    print(f"{boo}: {ghost}")
```

11. `combo_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}`

