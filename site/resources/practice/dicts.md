---
title: Dictionary Conceptual Questions
author:
- Alyssa Lytle
- Carmine Anderson-Falconi
page: lessons
template: overview
---

# Questions

## Conceptual

1. Dictionaries in Python can have duplicate keys. (T/F)
2. Dictionaries in Python can be nested, meaning a dictionary can contain another dictionary as a value. (T/F)
3. `[]` is to `list`s as ___ is to `dict`s.

## Basic Syntax

1. Create a new dictionary called `my_dictionary` with `str` keys and `float` values and initialize it as an empty dictionary.

2. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, access the *value* stored under key "Yall". 

3. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, increase the *value* stored under key "Yall" by 3.

4. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
remove the value "Alyssa", stored at key 100.

5. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
write a line of code to get the number of key/value pairs in the dictionary.

6. Using the following dictionary, `stock: dict[str, int] = {"carrots": 50, "beets": 20, "apples": 10}`, write a line of code to check if key "carrots" is in the dictionary.


# Answers

## Conceptul Questions

1. False
2. True
3. `{}`

# Syntax Solutions

1. `my_dictionary: dict[str, float] = {}` or `my_dictionary: dict[str, float] = dict()`

2. `msg["Yall"]`

3. `msg["Yall"] += 3` or `msg["Yall"] = 5`

4. `ids.pop(100)`

5. `len(ids)`

6. `carrots in stock`